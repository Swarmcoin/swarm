# Owner setup for the @swarm_coin agent (verified 9 October 2026)

What you, and only you, do so that `swarm-social` can run from GitHub Actions. Agents never hold
these tokens, never set the variables and never read the secrets. Every step below was checked
on 9 October 2026 against docs.x.com, help.x.com and docs.github.com; a step marked **(not
verified)** could not be seen without signing in and is written from the docs' description of the
screen. If a screen looks different, stop and say so; do not improvise.

Costs: pay-per-use, no subscription. At the planned cadence about 15 to 30 USD a month for X
plus a few cents a cycle for Claude. The first saved card earns 20 USD of free X credits.

## 0. Before you start

- You are signed in to x.com as **@swarm_coin** in the browser you use for all of this. The
  developer account, the app and the tokens must belong to @swarm_coin, not to a personal
  account: the OAuth 1.0a access token posts as the account that owns the app.
- Repository: https://github.com/Swarmcoin/swarm. The workflow is on the branch
  `claude/swarm-social-campaign-n4g676` (pull request 1, draft). The cron only runs on the
  default branch, so the PR has to be merged (step 5) before the first scheduled run.
- Have a password manager open. X shows each credential **once**; a lost credential has to be
  regenerated, which invalidates the old one.

## 1. Developer account and app (docs.x.com, "Getting access", "Apps")

The portal is the **Developer Console** at https://console.x.com (docs.x.com now names only
this address; the older developer.x.com/en/portal links redirect there, **not verified**).

1. Open https://console.x.com and sign in with @swarm_coin.
2. Accept the **Developer Agreement and Policy** (docs: "Review and accept the Developer
   Agreement and Policy").
3. Complete the profile: "Provide basic information about how you'll use the API". Plain text
   suggestion: *Scheduled posts and replies to people who mention @swarm_coin, for the SWARM
   project (swarm.green). Single owned account, no third-party users.*
4. Click **New App** (the docs use both "New App" and "Create App"). Name: `swarm-social`.
   Description: *Scheduled posts and guarded replies for @swarm_coin.* Use case: the same text
   as step 3.
5. The console generates the credentials. **Copy every one into the password manager now**:
   API Key, API Key Secret, Bearer Token, and (if shown here) Access Token and Access Token
   Secret. Docs: "Save credentials immediately—they're only shown once."
6. **Permissions must be Read and write** before the access token is generated. In the app's
   **Settings** (docs: "Configure authentication, permissions, and callback URLs") set the OAuth
   1.0a permission to **Read and write** (the three levels are "Read only", "Read and write",
   "Read, write, and DMs"; never the third: the agent never sends DMs). If a **User
   authentication settings** form asks for app type and URLs **(not verified)**: type
   *Automated App or bot*, website `https://swarm.green`, callback `https://swarm.green/`.
   The agent does not use the callback; the form only requires a value.
7. If the permission was changed after the Access Token was generated, **regenerate** the
   Access Token and Secret in the app's **Keys and tokens** tab (docs: "Changing permissions
   requires users to re-authorize your app to get new tokens"). The token pair generated
   under *Read only* cannot post, and the agent will fail with HTTP 403 on its first reply.
8. Keys and tokens tab, in the words of the docs: "Navigate to the Developer Console; expand
   the 'Apps' dropdown in the sidenav; open the App; navigate to the Keys and tokens tab."
   From there you can regenerate any credential later.

What the five credentials are (docs.x.com, "Getting access", step 3):

| Credential | Repository secret | Used for |
| --- | --- | --- |
| API Key | `X_API_KEY` | identifies the app (OAuth 1.0a consumer key) |
| API Key Secret | `X_API_SECRET` | signs requests |
| Access Token | `X_ACCESS_TOKEN` | acts as @swarm_coin ("Acting as yourself": "These tokens represent the account that owns the app") |
| Access Token Secret | `X_ACCESS_SECRET` | signs those requests |
| Bearer Token | `X_BEARER_TOKEN` | app-only reads; optional, the agent reads with the user tokens when it is missing |

## 2. Credits (docs.x.com, "Pricing", "Free credits", "Usage and billing")

1. In the Developer Console open **Billing**. Add a payment method under **Billing information
   → Add payment method**, or buy credits and keep the card on file. A credit or debit card
   (not prepaid) that has never been used on an X developer account earns **20 USD of free
   credits** at that moment (docs: "Earn $20 in free X API credits when you save your first
   eligible payment card"). The free credits expire after three months and are spent first.
2. Buy **10 USD** of credits for the first month (docs: no minimum spend; "Purchase credits
   upfront in the Developer Console"). With the free 20 USD that covers the dry run and the
   first review weeks.
3. **Spending limits**: set the cap to **40 USD per billing cycle**. Requests are blocked when
   the cap is reached, which is the behaviour we want from a bot.
4. **Auto-recharge**: leave it off for now. (If you switch it on later, the first automatic
   recharge is matched with free credits up to 50 USD; it needs a saved card and a threshold.)
5. The rate card the estimate rests on (docs.x.com pricing, 9 October 2026): create a post
   0.015 USD; create a post with a URL 0.200 USD; read a post 0.005 USD per post returned
   (deduplicated per UTC day); read a user 0.010 USD; "User Interaction: Create" (like,
   repost) 0.015 USD. Reads are capped at 3 million posts a month, far above our use.

## 3. Claude key (console.anthropic.com)

Create an API key at https://console.anthropic.com/settings/keys named `swarm-social`
**(not verified today; the console page may have moved)**. Put it into the password manager.
It becomes the secret `ANTHROPIC_API_KEY`. Set a monthly spend limit in the console if it
offers one; the agent costs a few cents per cycle, most cycles end early.

## 4. Repository secrets (docs.github.com, "Using secrets in GitHub Actions")

On https://github.com/Swarmcoin/swarm, in the words of the docs:

1. Under the repository name, click **Settings**. If you cannot see it, open the **More**
   dropdown, then **Settings**.
2. In the "Security" section of the sidebar, select **Secrets and variables**, then click
   **Actions**.
3. Click the **Secrets** tab, then **New repository secret**.
4. **Name** exactly as in the table, **Secret** the value from the password manager, **Add
   secret**. Six times:

| Name | Value |
| --- | --- |
| `X_API_KEY` | API Key |
| `X_API_SECRET` | API Key Secret |
| `X_ACCESS_TOKEN` | Access Token (generated under Read and write) |
| `X_ACCESS_SECRET` | Access Token Secret |
| `X_BEARER_TOKEN` | Bearer Token (optional) |
| `ANTHROPIC_API_KEY` | the Claude key |

A saved secret cannot be read back, only replaced. Names are case-sensitive; the workflow
reads exactly these six.

## 5. Merge the pull request

Review and merge https://github.com/Swarmcoin/swarm/pull/1 (your click; agents do not merge).
Until it is on the default branch, the 30-minute cron does not exist; "Run workflow" on the
branch still works for a manual test.

## 6. Variables, in this order (docs.github.com, "Store information in variables")

Same place: **Settings → Secrets and variables → Actions**, now the **Variables** tab, **New
repository variable**, Name, Value, **Add variable**. To change one later, open it from the
same list and edit the value.

**Stage 1, dry run (days 1 to 3).** Create nothing, or create `SWARM_SOCIAL_LIVE` with value
`0`. Every run reads mentions and targets for real (that costs reads), writes what it *would*
have sent into the step summary and into `campaign/agent/state/`, and sends nothing. The
agent session reads three days of summaries and reports.

| Variable | Value | Meaning |
| --- | --- | --- |
| `SWARM_SOCIAL_LIVE` | `0` | dry run (the default when the variable is missing) |
| `SWARM_SOCIAL_APPROVAL` | `review` | everything waits for a human (the default) |
| `SWARM_SOCIAL_SCHEDULER` | `0` **if** Metricool publishes the calendar, otherwise leave it unset | prevents double posting |

**Stage 2, review mode.** Only after the agent session recommends it in writing: set
`SWARM_SOCIAL_LIVE` to `1`. Mentions are still answered only after your approval: once a day
you get the list (id, who, the proposed reply, why) and answer "approve: id id" or "reject:
id"; the session runs **Actions → Social: X → Run workflow** with the `approve` field, or you
do. Likes are also queued, never automatic.

**Stage 3, auto mode.** Set `SWARM_SOCIAL_APPROVAL` to `auto` **and** `SWARM_SOCIAL_X_AI_APPROVAL`
to the reference of X's written approval (date or ticket). Without that second variable the
agent stays in review mode and says so in every summary. Why: X's Automation Rules (updated
April 2026, section II.B.3) say "the deployment or operation of any AI reply bot requires prior
written and explicit approval from X. Contact your dedicated point of contact or submit a
request through the developer portal for review." The request is yours to submit (Developer
Console, support or the platform help form; the exact entry point is **not verified**). The
agent session recommends auto mode only after a week of review mode with no rejected mention
reply, and only once that approval exists.

Optional, for the label X offers bot accounts: on @swarm_coin, **Settings → Your account →
Automation**, link a managing account (docs.x.com "Automated account labels"). This marks the
whole account as automated. Our account is mostly human; decide yourself. **(not verified)**

## 7. What the agent never does, whatever is set

Follows nobody, sends no DM, likes nothing on its own, never replies to a post that did not
mention @swarm_coin (those are proposals for you), never replies twice to the same post, never
answers a person who asked it to stop, and refuses any text that breaks `policy.yaml`: no price,
no promise, no testnet, no "anonymous", no "copy of Zcash", no multilevel words, no download
link off swarm.green, network named beside every address, the ASIC sentence on every mining
call.

## 8. If something goes wrong

- Rotate a credential: Developer Console → Apps → swarm-social → Keys and tokens → Regenerate;
  then replace the repository secret. The old value stops working at once.
- Stop everything: set `SWARM_SOCIAL_LIVE` to `0`, or disable the workflow (Actions → Social: X
  → "…" → Disable workflow). Nothing is sent from the next run on.
- Suspended app: X mails the account; appeal with the Platform Help Form (docs.x.com, "App
  suspended").
