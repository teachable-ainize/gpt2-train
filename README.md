# Xangle Disclosure Writer
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Auto-generated github repository by [Ainize Teachable NLP](https://ainize-dev.herokuapp.com/teachable-nlp)
## Health Check
Using `curl` in the terminal:
```
$ curl --request GET 'https://train-xkkcpc9vsae6r5vc5mhy-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/ping'
{
  "status": "Healthy"
}
```
## Prediction Test
### Prediction 
Using `curl` in the terminal:
#### New Listing
```
$ curl --request POST 'https://train-xkkcpc9vsae6r5vc5mhy-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/xangle-summary' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "context": "We are pleased to announce that Bitfinex will list Pluton (PLU). Deposits are now open as of 28/11/20 at 09:00 AM UTC. Trading and withdrawals of PLU will commence on 2/12/20 at 12:00 PM UTC.\nMore information about Pluton can be found at https://plutus.it.\nPLU can be traded with US Dollars (PLU/USD).",
    "docType": "new_listing"
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

#### New Partnership
```
$ curl --request POST 'https://train-xkkcpc9vsae6r5vc5mhy-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/xangle-summary' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "context": "Verasity announces its partnership with Transak to power its fiat gateway and credit card fiat-to -crypto deposits from within Verasity's VeraWallet.\nVerasity's Co-Founder, RJ Mark said\n\"Fiat on-ramps will play a huge role in the scaling and adoption for VRA & VRAB. The partnership with Transak will make all the difference in being able to promote mass VRA/VRAB usage in our GameStore for game developers and publishers and we especially appreciate the geographic scope they are covering\".\nTransak's Co-Founder, Sami Start said\n\"I'm excited to work with Verasity's 60k+ community of users and followers to help grow the adoption of their platform. Their dev team provided an impressive integration of the Transak API. It's a fantastic example of a truly integrated experience that flows with the Verasity user experience. We are excited to see this boost conversion rates for Verasity's gaming and video platform\"\nAbout Transak\nTransak is a single integration for applications to accept fiat-to-crypto deposits and withdrawals from a global user base. It does this by aggregating fiat on-ramps from around the world and abstracting away the complexity of local compliance, payment methods, and operations. The Transak product is a widget integration that can be integrated into an app in just a few lines of code. You can buy VRA with Transak here, or integrate into your app here. Transak is backed by Consensys and graduated from the Tachyon accelerator program.\nAbout Verasity\nIf you are a video publisher and want to grow your audience and revenue by 500%, click the link below to talk to the team:\nhttps://verawallet.tv/publisher-form\nVerasity is a leading company providing rewarded video player technology to major publishers and game developers across the globe. The patent-pending video player enables tokenized rewards (VRA) as well as loyalty schemes within a video player wallet. The unique technology is already available by SDK to most of the major video players that support over 2 million video publishers and brings engagement and revenues back to publishers' sites. Our SDK products integrate directly with publishers so that neither publishers nor users have to change their workflow or habits.\nVerasity's attention-based model creates a thriving VRA token economy between viewers, video & game publishers and advertisers. Verasity is the future of online video.\nVerasity products launched include: VeraWallet, Triviata gaming app; SDKs for the following video players on publishers' sites: YouTube, Twitch, Vimeo, JWPlayer, Brightcove, iVideoSmart, Kaltura, VideoJS, Flowplayer, and Ooyala which represents over 95% of all the video players utilized and Proof of View (PoV) TBA.\nVerasity has announced partnerships with hundreds of gaming publishers to be launched on a new gaming portal. Gamers will utilize VRA through watching ads, subscriptions, cost to play, competing and betting against other VRA holders as well as Brand store vouchers. Publishers purchase VRA at exchanges to fund their campaigns.\n📈 Find where VRA/VRAB (ticker) is trading on CoinMarketCap\nVRA and VRAB can be staked for 36.5% annual interest at https://verawallet.tv.\nFollow Us:\nMedium: https://medium.com/verasity\nTwitter: https://twitter.com/verasitytech\nWebsite: https://verasity.io\nTelegram Token Discussion: http://t.me/verasitychat\nTelegram Token Announcements: https://t.me/verasity\nVerasity Mobile Telegram: https://t.me/verasity_mobile\nKakao: https://open.kakao.com/o/gh8ZK0cb\nFacebook: https://facebook.com/verasitytech\nLinkedIn: https://www.linkedin.com/company/verasity\nReddit: https://www.reddit.com/r/verasity\nBlockfolio Signals: Follow VRA/VRAB to receive updates straight from the team\nJoin our local groups, we have support in the following languages\nRussian chat — https://t.me/VerasityRU\nKorean chat 🇰🇷 — https://open.kakao.com/o/gh8ZK0cb\nTurkish chat — https://t.me/VerasityTR\nVietnamese chat — https://t.me/Verasity_Vietnam\nBrazilian chat — https://t.me/Verasity_BR\nSpanish Chat — https://t.me/verasity_spanish\nPersian Chat — https://t.me/verasity_irn\nJapanese Chat — https://t.me/verasityjapanese\nWeChat — PM @cryptomeo on Telegram",
    "docType": "new_partnership"
  }'
{
  "Partner's Name": "Defi Money Market",
  "Counterparty Website": "https://explorer.defimoneymarket.com/",
  "Counterparty Details": "DeFi Money Market (DMM) is building a vibrant global community to provide a decentralized, transparent and permissionless environment to empower all citizens to once again earn interest on their currency backed by real-world assets represented on-chain. DeFi Money Market (DMM) acts as a bridge between Ethereum digital assets and real-world assets, allowing digital asset holders to earn interest completely on-chain in the way they are accustomed to, but driven by a secure and uncorrelated basket of real-world assets.",
  "Does this partnership generate any kind of revenue?": "NO",
  "Applicable Date(s)": "2020-03-02T00",
  "Partnership Details": "Chainlink is closely collaborating with DMME Team.Chainlink's role is to reliably and securely obtain accurate information about the assets that back the DMME and publicize it on-chain. Chainlink's decentralized oracle network extends the blockchain's security guarantees to the oracle layer by decentralizing the data delivery mechanism (multiple oracle nodes retrieve the same data point) and data source (oracles retrieve information from multiple data sources). Chainlink oracles greatly enhance the overall functionality of the DMM smart contracts, yet maintain the utmost security standards to ensure DMM remains highly secure, reliable, and trustworthy."
}
```

#### Milestone Achivement
```
$ curl --request POST 'https://train-xkkcpc9vsae6r5vc5mhy-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/xangle-summary' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "context": "Introduction\nWe are excited to announce that B.Protocol is live on the Ethereum mainnet, and available at https://bprotocol.org/app.\nUsers of B.Protocol are able now to make more with their MakerDAO Vaults, earn a share from liquidation proceeds, take part of B.Protocol future upgrading decisions, and help make MakerDAO more resilient to Black Thursday-like events.\nWe are sharing here the full details about the protocol's launch, to enable everyone to learn the details and choose how and when to get involved.\nWhat users get\nUsers who manage their MakerDAO Vaults with B.Protocol smart contract interface accumulate a user rating score. The earliest you start using B.Protocol, the more rating score you get. After a 6 month period, part of the liquidators' proceeds are distributed to the users, proportional to the rating score they have accumulated.\nThe protocol was seeded with $10,000 in ETH to guarantee a minimum of the sum of distributed rewards. After 6 months the same time, users could start to vote on the future proceeds distribution model, and their voting power is proportional to their score.\nDuring the first month, the user rating accumulation speed will be x2 higher.\nThe score is given only to users, and no score was pre-allocated to VCs or the team.\nThe score is non transferable and not even an ERC20 token. Hence it cannot be traded, and can never be traded.\nWhile we technically cannot prevent future governance from tokenizing it, we will not actively support any outcome that will violate the applicable regulatory framework.\nSecurity model\nB.Protocol was designed as a thin layer on top of MakerDAO CDP system, and to make user funds as secure as they are when using MakerDAO directly. The user pays the same interest rate, and the same liquidation penalty.\nThe code was audited by Solidified. Wil Barnes and Lucas Manuel, who are among the people that are most familiar with MakerDAO smart contract code, also reviewed it.\nBoth reports did not find any major issues, and confirmed our analysis regarding the security of user funds.\nThe problem we solve\nOver $10B in DeFi assets crucially relies on an adequate liquidation process for their security. The Dai ecosystem, lending platforms like Compound and Aave, synthetic asset platforms, and margin trading platforms all rely on liquidations to remain solvent.\nWhenever a user debt is about to exceed its collateral, a liquidation process is triggered, in which a liquidator pays the user's debt in return for a part of their collateral. All major DeFi platforms currently outsource this service to the entire Ethereum community, by allowing every Ethereum account to participate in the liquidation process, and offer a discount of 3–8% on the liquidated collateral in order to incentivize liquidators to participate.\nThis is in general a fair approach, but as we have covered in a previous blog, it brings up two major issues — 1) Gas wars that lead to MEV growth that will eventually mark down liquidation incentives to zero, and 2) lack of committed liquidators as the uncertainty of potential profits is too high. Both of these issues are critical to the stability of the DeFi ecosystem on any given day, and in particular on severe market conditions as occurred on Black Thursday in March earlier this year.\nB.Protocol is a new DeFi lego primitive aiming to make decentralized lending platforms more stable by introducing a backstop liquidity solution. We incentivize liquidity providers (keepers) to share their proceeds with the platform users in return for getting a priority in the liquidation process. By that, we bring more committed liquidators to the platform and help to shift back miners extracted profits (aka MEV) to the community.\nHow does it work?\nWe integrate B.Protocol with existing lending platforms, MakerDAO being the first. We let users interact with the lending platforms via a dedicated smart contract interface. B.Protocol liquidators get a priority in the liquidation process by providing a cushion to the user account when it is getting close to the liquidation price. You can read more about how B.Protocol achieves fairness in its liquidation process here.\nSimplified flow of B.Protocol\nUsers are getting a Rating score according to their usage of the protocol (borrowing Dai for a certain time period). Any liquidation that is being processed by B.Protocol's Liquidators over MakerDAO is being divided, and 50% of the liquidation discount is going into the Jar. After 6 months the Jar is being distributed among the Users of B.Protocol according to their Rating score.\nWho Benefits from using B.Protocol\nEveryone (but miners…)!\nMakerDAO users can get added value from their MakerDAO Vaults, sharing a part in the liquidation proceeds with no added risk*.\nMakerDAO as a lending platform gets new and committed professional liquidators that bring more stability to the platform. In the long run, a more stable platform could enable a lower collateral ratio.\nLiquidators get better risk management and prediction capabilities. This incentivise them to build better adjusted tools for DeFi lending platforms, and in return for the decline in uncertainty, to share their proceeds with the users of the platform.\nThe Ethereum ecosystem get another way to mitigate MEV and to shift value from miners back to users.\nThe Details\nRating Score\nRating Score calculation: A user's Rating Score is determined by the amount of DAI s/he borrowed and the time that elapsed before returning the loan. Formally, for every debt of 1,000 DAI (*), a user will receive 1 point daily (* the actual debt is normalized by dividing by the MakerDAO cumulative rate, which is currently 1.2).\nFor example, if a user has a (normalized) debt of 5000 DAI for a period of 7 days, then his/her score is added with 35 points.\nThe user Rating Score is not transferable during the first 6 months.\nFair Launch principles — No VCs & no pre-mine of Rating Scores to anyone. Including Dev.\nIn order to incentivize the bootstrapping of the protocol, Rating Scores will be calculated with an x2 factor for the first month from launch.\nJar\nLiquidation proceeds sharing: 50% of the premium of every liquidation (In the time of writing, this is 6.5% of the liquidation size) goes into the JAR smart contract.\nJAR Rewards Distribution: After 6 months, the content of the JAR will be distributed among the users of B.Protocol in proportion to their Rating Score.\nImportant stuff\n6 months after launch, 100% of the control of B.Protocol on top of MakerDAO will be handed to the community who will have the power to decide about its future path. A decision by 51% of the users, according to their Rating Score, will be able to set an adjusted incentive model.\nThe Jar has been subsidized by B.Protocol and has been injected with a $10k worth of ETH, so participants will benefit from migrating to or using B.Protocol even if only few liquidations will take place during the 6 months period till the Jar will be distributed.\nHow to start with B.Protocol\nB.Protocol (https://bprotocol.org/app) is an alternative Vault management system. Users are getting the exact same conditions as if they were using MakerDAO, plus the ability to share the liquidation proceeds with B.Protocol liquidators.\nImport your Vault to B.Protocol with a single click, using the import widget.\nIf you do not have a Vault on MakerDAO — Open one through B.Protocol by deposit ETH and Borrow Dai.\nYour Rating score will keep on growing as long as you hold a debt.\nAfter 6 months from launching, the Jar balance, which is where liquidation proceeds are being kept, will be distributed among users according to their rating score.\n*For a full tutorial on how to use B.Protocol head over to https://medium.com/b-protocol/how-to-use-b-protocol-4f13591e33dc.",
    "docType": "milestone_achievement"
  }'
{
  "Name": "B.Protocol is LIVE",
  "Date": "2020-10-27",
  "Accomplished": "YES",
  "Details": "B.Protocol is live on the Ethereum mainnet, and available at https://bprotocol.org/app. Users of B.Protocol are able now to make more with their MakerDAO Vaults, earn a share from liquidation proceeds, take part of B.Protocol future upgrading decisions, and help make MakerDAO more resilient to Black Thursday-like events. B.Protocol was designed as a thin layer on top of MakerDAO CDP system, and to make user funds as secure as they are when using MakerDAO directly. The user pays the same interest rate, and the same liquidation penalty.B.Protocol is an alternative Vault management system. Users are getting the exact same conditions as if they were using MakerDAO, plus the ability to share the liquidation proceeds with B.Protocol liquidators.6 months after launch, 100% of the control of B.Protocol on top of MakerDAO will be handed to the community who will have the power to decide about its future path. A decision by 51% of the users, according to their Rating Score, will be able to set an adjusted incentive model.The overview of B.Protocol can be accessed via the link or attachment below."
}
```

#### Major use-case
```
$ curl --request POST 'https://train-xkkcpc9vsae6r5vc5mhy-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/xangle-summary' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "context": "Today, Crypto.com announced it has begun shipping its MCO Visa Cards to 31 countries in Europe, making it the only crypto card provider offering cards in Asia, the full EU, and the United States.\nCrypto.com's MCO Visa card was one of the first on the market when it launched in Singapore in 2018, and is now the most widely available card in the world. Since then the market for crypto cards has accelerated, as a wide range of companies have expanded their offerings or released cards of their own. Starting today, Crypto.com is now shipping its cards to 31 markets in Europe, including all 27 EU member states, an addressable market of nearly 530 million people.\nKris Marszalek, Co-founder and CEO of Crypto.com said: \"Since we first shipped our MCO Visa card in 2018, we have been rapidly moving into new markets and growing our user base. Crypto.com has separated itself from the pack by focusing on building an end-to-end crypto ecosystem that features high levels of security. Our user-friendly app acts as a single hub to manage all of your crypto financial needs; once cards are paired with the app, users can buy, sell, and earn crypto and get an instant loan.\"\nCrypto.com has seen significant traction in Europe recently and has taken a number of steps to expand its presence, including hiring Mariana Gospodinova as general manager of the region. The team has bolstered its regulatory compliance within the complex payments ecosystem and launched local communities supporting most EU local languages for better access to instant feedback and support. Additionally, the company earlier this month announced a new $100M insurance policy that brings Crypto.com's total crypto insurance to an industry-record $360M, providing an additional layer of protection for its 2+ million user base. Crypto.com has already seen thousands of reservations for the MCO Visa card from users across the EU and the Crypto.com app has reached top 50 in the Finance category in the UK, France, Italy and Spain\nCrypto.com's broad European card launch comes after successful card launches in the UK and the United States. The U.S. card supports both crypto and fiat top ups and is now compatible with Apple and Google Pay. Fiat top ups give users a choice to hold onto their crypto portfolio. But by spending fiat, one can earn up to 5% of cash back in crypto. Addressing the needs facing COVID-19, the card program has increased essential purchases cash back up to 10% for the metal card tier and 5% for the plastic card tier.\nCrypto.com offers five tiers of MCO Visa cards that feature no annual or monthly fees, 100% rebate on Spotify, Netflix and Amazon Prime, airport lounge access for select cards, no fee ATM withdrawals, tap-and-pay functionality, and competitive interbank rates.\nMCO Visa Card is issued by Wirecard Card Solutions Ltd (\"WDCS\") pursuant to licence from Visa. WDCS is authorised by the Financial Conduct Authority to conduct electronic money service activities under the Electronic Money Regulations 2011 (Ref: 900051)",
    "docType": "major_use_case"
  }'
{
  "Title": "MCO Visa Card Shipping in Europe",
  "Applicable Date(s)": "2020-05-15T00",
  "Type": "business",
  "Category": "payment platforms",
  "Main Participant": {
      "Main Participant's Name": "Crypto.com",
      "Main Participant's Website": "http://www.crypto.com/"",
      "Main Participant's Sector": "financials",
      "Main Participant's Details": "Crypto.com accelerates the transition to crypto by putting cryptocurrency in every wallet with a strong focus on real-life use cases. Crypto.com is building an outstanding and defensible platform to solve access and usability challenges in the blockchain industry, and power redefined financial services to improve our customers' lives. The Crypto.com includes the Crypto.com App (to buy, exchange, send and track cryptocurrency) and the MCO Visa Card (to spend your cryptocurrency in the real world).",
  },
  "List of others involved": {
      "Involved Entity's Name": "-",
      "Involved Entity's Website": "-",
  },
  "Details": "On May 15th, Crypto.com announced it has begun shipping its MCO Visa Cards to 31 countries in Europe, making it the only crypto card provider offering cards in Asia, the full EU, and the United States.Starting today, Crypto.com is now shipping its cards to 31 markets in Europe, including all 27 EU member states, an addressable market of nearly 530 million people.Crypto.com has seen significant traction in Europe recently and has taken a number of steps to expand its presence, including hiring Mariana Gospodinova as general manager of the region. Additionally, the company earlier this month announced a new $100M insurance policy that brings Crypto.com's total crypto insurance to an industry-record $360M, providing an additional layer of protection for its 2+ million user base. Crypto.com has already seen thousands of reservations for the MCO Visa card from users across the EU and the Crypto.com app has reached top 50 in the Finance category in the UK, France, Italy and Spain.",
}
```

#### Delisting
```
$ curl --request POST 'https://train-xkkcpc9vsae6r5vc5mhy-gpt2-train-teachable-ainize.endpoint.dev.ainize.ai/predictions/xangle-summary' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "context": "Fellow Binancians,\nAs per the MCO Swap Program, the MCO token will officially stop being supported by the project team and lose all functionality at 2020/11/03 00:00 AM (UTC).\nAs Binance has not been given the option by the project team to directly swap MCO to CRO tokens for our users, we will keep MCO withdrawals open until 2021/02/02 8:00 AM (UTC) and allow users to withdraw.\nHowever, as the MCO token itself will lose its functionality, Binance will delist MCO and cease trading on the remaining MCO/ETH trading pair at 2020/11/02 08:00 AM (UTC).\nPlease note:\nAll trade orders will be automatically removed after trading ceases.\nTo view your MCO tokens after trading ceases, please ensure you have not selected \"Hide small assets\" in your Funds page.\nThanks for your support!\nBinance Team\n2020/10/27",
    "docType": "delisting"
  }'
{
  "Exchange Name": "Binance",
  "Date (Estimated Date)": "2020-11-03",
  "Details": {
    "Name": "MCO",
    "Symbol": "MCO",
    "Key Dates": {
        "Deposit deadline": "-",
        "Trading deadline": "Nov 3, 2020, at 00:00 am UTC",
        "Withdrawal deadline": "Feb 2, 2021 at 8:00 am UTC",
    },
    "Reason": ""As per the MCO Swap Program, the MCO token will officially stop being supported by the project team. As Binance has not been given the option by the project team to directly swap MCO to CRO tokens for our users, we will keep MCO withdrawals open until the deadline and allow users to withdraw. However, as the MCO token itself will lose its functionality, Binance will delist MCO and cease trading on the remaining MCO/ETH trading pair at 2020/11/02 8:00 am UTC.Please note:All trade orders will be automatically removed after trading ceases.To view your MCO tokens after trading ceases, please ensure you have not selected \"Hide small assets\" in your Funds page.",
  }
}
```