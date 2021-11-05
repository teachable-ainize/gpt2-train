# gpt2-train


Auto-generated github repository by [Ainize Teachable NLP](https://ainize.ai/teachable-nlp)
## Health Check
Using `curl` in the terminal:
```
$ curl --request GET 'https://train-j7ncn8nxocqlqb5y6n8f-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/ping'
{
  "status": "Healthy"
}
```
## Prediction Test
### Prediction
Using `curl` in the terminal:
```
$ curl --request POST 'https://train-j7ncn8nxocqlqb5y6n8f-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/testpr' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "text": "He (she) had black thick wires.",
    "src_language": "en_XX", 
    "tgt_language": "ko_XX"
  }'
[
  ['그(그녀)는 검은색 굵은 와이어을(를) 가지고 있었습니다.']
]
``` 

## language type 
1. src_language and tgt_language must one of following,
2. "X" means wildcard matching (i.g, ko_XX == ko_KR, kX_XX == kk_KZ or ko_KR)
3. must include single "_"
4. do not change letter case
```json
[
  'ar_AR', 'cs_CZ', 'de_DE', 'en_XX', 'es_XX', 'et_EE', 'fi_FI', 'fr_XX', 'gu_IN', 'hi_IN', 'it_IT', 'ja_XX', 'kk_KZ', 'ko_KR', 'lt_LT', 'lv_LV', 'my_MM', 'ne_NP', 'nl_XX', 'ro_RO', 'ru_RU', 'si_LK', 'tr_TR', 'vi_VN', 'zh_CN', 'af_ZA', 'az_AZ', 'bn_IN', 'fa_IR', 'he_IL', 'hr_HR', 'id_ID', 'ka_GE', 'km_KH', 'mk_MK', 'ml_IN', 'mn_MN', 'mr_IN', 'pl_PL', 'ps_AF', 'pt_XX', 'sv_SE', 'sw_KE', 'ta_IN', 'te_IN', 'th_TH', 'tl_XX', 'uk_UA', 'ur_PK', 'xh_ZA', 'gl_ES', 'sl_SI'
]
```