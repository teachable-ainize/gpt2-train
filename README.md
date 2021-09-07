# Xangle Disclosure Writer
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Auto-generated github repository by [Ainize Teachable NLP](https://ainize-dev.herokuapp.com/teachable-nlp)
## Health Check
Using `curl` in the terminal:
```
$ curl --request GET 'https://train-wclfh1dlnbmur204y53t-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/ping'
{
  "status": "Healthy"
}
```
## Prediction Test
### Prediction 
Using `curl` in the terminal:
```
$ curl --request POST 'https://train-wclfh1dlnbmur204y53t-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/xangle-summary' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "context": "We are pleased to announce that Bitfinex will list Pluton (PLU). Deposits are now open as of 28/11/20 at 09:00 AM UTC. Trading and withdrawals of PLU will commence on 2/12/20 at 12:00 PM UTC.\nMore information about Pluton can be found at https://plutus.it.\nPLU can be traded with US Dollars (PLU/USD).",
    "docType": "New Listing"
  }'
{
  "Exchange Name": "Bitfinex", 
  "Date (Estimated Date)": "2020-12-02T00:00:30", 
  "Details": {
    "Name": "Pluton", 
    "Symbol / Ticker": "PLU", 
    "Key Dates": {
      "Wallet creation and deposit requests opening date": "November 28, 2020 at 9:00 AM UTC", 
      "Trading opening date": "December 2, 2020 at 12:00 PM UTC", 
      "Withdrawal opening date": "December 2, 2020 at 12:00 PM UTC"
    }, 
    "Initial Fees and Pricing": {
      "Withdrawal fee": "-", 
      "Announced listing pairs": "PLU/USD", 
      "Listing price": "-"
    }, 
    "Trading": {
      "Minimum Trade/Purchase Amount": "-", 
      "Minimum Price Movement": "-", 
      "Minimum Order Size": "-"
    }, 
    "Other info": {
      "Exchange promoted listing/airdrop event": "-"
    }
  }
}
``` 

