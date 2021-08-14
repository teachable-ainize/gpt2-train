# gpt2-train
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://github.com/SKT-AI/KoGPT2/blob/master/LICENSE)

Auto-generated github repository by [Ainize Teachable NLP](https://ainize.ai/teachable-nlp)
## Health Check
Using `curl` in the terminal:
```
$ curl --request GET 'https://train-64pm3hoackglp7ahfkq0-gpt2-train-teachable-ainize.endpoint.ainize.ai/ping'
{
  "status": "Healthy"
}
```
## Prediction Test
### Prediction
Using `curl` in the terminal:
```
$ curl --request POST 'https://train-64pm3hoackglp7ahfkq0-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "text": "근육이 커지기 위해서는",
    "num_samples": 5,
    "length": 8
  }'
[
  "근육이 커지기 위해서는 반드시 필요한 것이다.\n한번이라도 비염",
  "근육이 커지기 위해서는 자신의 몸을 따뜻하게 유지해야 한다.\n그러다",
  ...,
  "근육이 커지기 위해서는 △유능해질 수 있는 환경과 더불어"
]
``` 

