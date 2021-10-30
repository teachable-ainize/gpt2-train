# gpt2-train
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/openai/gpt-2/blob/master/LICENSE)

Auto-generated github repository by [Ainize Teachable NLP](https://ainize.ai/teachable-nlp)

## Health Check
Using `curl` in the terminal:
```shell
$ curl --request GET 'https://train-2vyrv4jijbr2gd6v8voc-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/ping'
{
  "status": "Healthy"
}
```

## Prediction Test

### Pre-processing for API
```
$ curl --request POST 'https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/preprocess' \
	--header 'Content-Type: application/json' \
	--data-raw '{
		"context": "there is a boy"
	}'

"[8117, 318, 257, 2933]"
```


### Prediction
Using `curl` in the terminal:
+ method 1: 
```shell
$ curl --request POST 'https://train-2vyrv4jijbr2gd6v8voc-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/gpt-2-en-small-simple-api-finetune' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "text": "there is a boy",
    "num_samples": 2,
    "length": 8,
    "input-as-text": true,
    "output-as-text": true,
  }'

[
  'there is a boy in this room.")\n\n"What',
  'there is a boy who needs to be changed and who may'
]
``` 

+ method 2: (need to use preprocessing - prediction - postprocessing)
```shell
$ curl --request POST 'https://train-2vyrv4jijbr2gd6v8voc-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/gpt-2-en-small-simple-api-finetune' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "text": [3666, 1438, 318, 14200, 11, 314, 16486, 1850, 287, 13851, 3783],,
    "num_samples": 2,
    "length": 8,
  }'

[
  [
    3666, 1438, 318, 14200, 11, 314, 16486, 1850, 287, 13851, 3783, 11, 314, 1101, 422, 262, 1294, 11, 523
  ],
  [
    3666, 1438, 318, 14200, 11, 314, 16486, 1850, 287, 13851, 3783, 379, 262, 2059, 286, 520, 26414, 11, 543
  ]
]
``` 


### default options
| option key  | default value  | description |
| :------------ |:---------------:| -----:|
| ```input-as-text```     | false    |
| ```output-as-text```     | false    | 
| ```num_samples```   | 1       | 
| ```length```        | 64      | new generated number of tokens



### Post-processing for API
```
$ curl --request POST 'https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/postprocess' \
	--header 'Content-Type: application/json' \
	--data-raw '[[8117, 318, 257, 2933]]'
  
{
   "0":{
      "text":"there is a"
   }
}
```
