import json
import os
import requests
import asyncio
import logging
from flask import Flask, jsonify, request
from ain.ain import Ain
from ain.types import ValueOnlyTransactionInput

# inference 8080
INFERENCE_URL = "http://localhost:8080"
# management 8081
MANAGEMENT_URL = "http://localhost:8081"
# AIN private key
AINIZE_INTERNAL_PRIVATE_KEY = os.environ['AINIZE_INTERNAL_PRIVATE_KEY']
PROVIDER_URL = os.environ['PROVIDER_URL']
chainId = 1 if 'mainnet' in PROVIDER_URL else None # FIXME(hyeonwoong): If ain-py is updated, change chainId from None to 0.
ain = Ain(PROVIDER_URL, chainId=chainId) # if PROVIDER_URL is mainnet, chainId is 1.
ain.wallet.addAndSetDefaultAccount(AINIZE_INTERNAL_PRIVATE_KEY)
# model name
MODEL_NAME = os.environ['MODEL_NAME']

# processing required?
text2text_model = ['gpt-2-ko-small-finetune', 'gpt-3-ko-6B-finetune']
processing_required = MODEL_NAME not in text2text_model

app = Flask(__name__)

async def set_value(ref, value):
    await ain.db.ref(ref).setValue(
        ValueOnlyTransactionInput(
            value=value,
            nonce=-1,
        )
    )

def predict(text, num_samples, length, model_name):
    data = {
        'text': text,
        'num_samples': num_samples,
        'length': length,
    }
    headers = { 'Content-Type': 'application/json; charset=utf-8' }
    path = f"{INFERENCE_URL}/predictions/{model_name}"
    res = requests.post(path, headers=headers, data=json.dumps(data))
    res = res.json()
    return res

def preprocessing(text):
    res = requests.post('https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/preprocess',
        headers={ 'Content-Type': 'application/json' },
        data=json.dumps({ "context": text })
    )
    res = res.json()
    return json.loads(res)

def postprocessing(vectors):
    res = requests.post('https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/postprocess',
        headers={ 'Content-Type': 'application/json' },
        data=json.dumps(vectors)
    )
    res = res.json()
    return res['0']['text']
    

@app.route("/predictions/<model_name>", methods=["POST"])
def predictions(model_name):
    try:
        if request.is_json:
            content = request.get_json()
            text = content['text']
            num_samples = content['num_samples']
            length = content['length']
            result = predict(text, num_samples, length, model_name)
            return jsonify(result), 200
        return jsonify(json.dumps([-1])), 400
    except Exception as e:
        print(e)
        return jsonify(json.dumps([-1])), 400

# for trigger api
@app.route("/trigger", methods=["POST"])
def trigger():
    req = json.loads(request.data.decode('utf-8'))
    if (not req.get('transaction') or
            not req['transaction'].get('tx_body') or
            not req['transaction']['tx_body'].get('operation')):
        return f'Invalid transaction : {req}', 400
    transaction = req['transaction']['tx_body']['operation']
    tx_type = transaction['type']
    if tx_type != 'SET_VALUE':
        return f'Not supported transaction type : {tx_type}', 400
    value = transaction['value']

    try:
        if processing_required:
            encodedText = preprocessing(value)
            predictedText = predict(encodedText, 1, 50, MODEL_NAME)
            result = postprocessing(predictedText)
        else:
            result = predict(value, 1, 50, MODEL_NAME)
        result_ref = transaction['ref'].split('/')[:-1]
        result_ref.append('result')
        result_ref = '/'.join(result_ref)
        asyncio.run(set_value(result_ref, result))
    except Exception as e:
        logging.error(f'Failed : {e}')
        return f'Failed : {e}', 500
    return '', 204

@app.route("/model_status", methods=["GET"])
def model_status():
    model_name = request.args.get("model_name")
    path = f"/models/{model_name}"
    get_path = MANAGEMENT_URL + path
    res = requests.get(get_path)

    if res.status_code != 200:
        return jsonify({
            "code": res.status_code,
            "status": "UNKNOWN"
        })

    models_status = res.json()

    num_workers = len(models_status)
    if num_workers == 0:
        return jsonify({
            "code": res.status_code,
            "status": "LOADING"
        })
    model_status = models_status[0]

    if len(model_status["workers"]) == 0:
        return jsonify({
            "code": res.status_code,
            "status": "LOADING"
        })

    # if model is loaded, then return "READY"
    return jsonify({
            "code": res.status_code,
            "status": model_status["workers"][0]["status"]
    })

@app.route("/ping", methods=["GET"])
def ping():
    path = "/ping"
    get_path = INFERENCE_URL + path
    res = requests.get(get_path)

    if res.status_code != 200:
        return jsonify({
            "health": "No Healthy!",
            "code": res.status_code
        })

    result = res.json()
    result["code"] = res.status_code
    return jsonify(result)
    


if __name__ == "__main__":
    app.run(debug=False, port=8000, host="0.0.0.0", threaded=True)
