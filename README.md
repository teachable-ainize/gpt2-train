# Xangle Telegram Sentiment Analyzer 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Auto-generated github repository by [Ainize Teachable NLP](https://ainize-dev.herokuapp.com/teachable-nlp)
## Health Check
Using `curl` in the terminal:
```
$ curl --request GET 'https://train-wkozyk81hseyjbxdvvbv-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/ping'
{
  "status": "Healthy"
}
```
## Prediction Test
### Prediction 
Using `curl` in the terminal:
```

$ curl --request POST 'https://train-wkozyk81hseyjbxdvvbv-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/xangle-classification' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "sentence": "Time to take some profits again😎"
  }'
{
  "negative": 0.047603052109479904, 
  "neutral": 0.25028911232948303, 
  "positive": 0.7021079063415527
}
``` 

