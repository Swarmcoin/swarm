# X automation: API, rules and tools (research, 6 October 2026)

Collected from search excerpts and registries; developer.x.com and vendor pricing pages were not
directly reachable from the research sandbox. Verify prices on the live pages before budgeting.

## X API access: tiers are gone, pay per use

- Since 6 February 2026 X sells **pay-per-use credits** to new developers; no subscriptions.
  Credits are bought in the Developer Console, with spend caps and optional auto top-up.
- Rate card (docs.x.com/x-api/getting-started/pricing, read via excerpts): post create
  **$0.015 per request**; post create **with a URL $0.20**; reply to a mention $0.010;
  user interaction create (like, follow, repost) about $0.015 (inferred, not confirmed);
  reads: post $0.005 per resource, user $0.010, like $0.001; reads capped around 3M a
  month before Enterprise.
- Free tier discontinued for new sign-ups; legacy Free accounts got a one-time $10 voucher.
- Legacy subscriptions (existing subscribers only, being migrated during 2026): Basic $200
  a month, 3,000 posts per user per month, 15,000 reads; Pro $5,000 a month.
- No endpoint is tier-gated any more; everything is billed per call.
- **Cost of this campaign at the planned cadence**: about 90 calendar posts (a third with a
  link), roughly 150 replies, and mention and search reads every 30 minutes come to
  roughly $15 to $30 a month. Links cost thirteen times a plain post, so the calendar keeps
  them to the posts where a link does work.

## X Automation Rules (help.x.com/en/rules-and-policies/x-automation)

Allowed: scheduled original posts; automated replies **only to people who opted in** by
mentioning or messaging the account first, one reply per interaction; several related,
non-duplicative accounts.

Prohibited: automated replies triggered by keyword search alone; automated or bulk
following and unfollowing; bulk or indiscriminate automated likes; posting about or
manipulating trending topics; duplicate or near-duplicate posts; unsolicited mentions or
DMs. Enforcement is account suspension and API termination.

This is why the agent in `../agent` answers mentions on its own but only *proposes* replies to
anything found by search or on a target account's timeline.

## Metricool (the connector attached to this workspace)

- Public REST API exists but only on the Advanced and Custom plans
  (app.metricool.com/resources/apidocs). The Metricool MCP (scheduling, analytics, best time
  to post) works on every plan, including Free.
- **X is a paid add-on: about $5 a month per X account, on Starter or higher.** The Free
  plan cannot connect X.
- Metricool does publishing and analytics for X. Its inbox shows X DMs only; it does not
  show or answer public replies and mentions, and it has no like or follow automation. So
  Metricool is the calendar, and the agent is the conversation.
- Without X Premium a post is limited to 280 characters; with Premium up to 25,000. Threads
  of up to 80 posts are supported.
- The account linked today is the owner's personal brand (Instagram, LinkedIn, TikTok). The
  @swarm_coin X account has to be added as a brand (or to that brand) before the calendar
  can be pushed there.

## Alternatives, in case Metricool is not the long-term home

| Tool | Price | API | X threads | Engagement automation |
| --- | --- | --- | --- | --- |
| Typefully | Free; Pro about $10 to $12.50; Business/Team about $20 to $39 | Yes, plus MCP | Yes | Auto-plug only |
| Buffer | Free (3 channels); Essentials $6 per channel | New GraphQL API (May 2026); REST retires 1 Feb 2027 | No | No |
| Publer | From $5; API on Business from $10 | Yes | Yes | No |
| Postiz (open source) | Self-host free; cloud $29 to $99 | Yes | Yes | Auto-repost only |
| Mixpost (open source) | Lite free; Pro $299 once | Yes (Pro), engagement MCP | Yes | Replies module |
| Ayrshare | $149 to $599 | API-first | Yes | Comment and reply endpoints; bring your own X keys since March 2026 |
| Late | Free to $999 | API-first | Unverified for X | Not found |
| Hypefury, Tweet Hunter | $29 to $199 | No | Yes | Auto-DM, auto-plug (Hypefury reportedly dropped X in mid-2026) |

## Libraries and auth

- Python: tweepy 4.17.0 (2 July 2026). Node: twitter-api-v2 1.29.1 (4 August 2026).
- Posting needs user context. For a single owned account, OAuth 1.0a (API key and secret,
  access token and secret) is the simplest: no refresh tokens. OAuth 2.0 PKCE with
  `tweet.write users.read tweet.read offline.access` (plus `like.write`) is the alternative.
  An app-only bearer token cannot post.
