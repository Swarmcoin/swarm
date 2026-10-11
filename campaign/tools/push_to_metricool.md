# Pushing the calendar to Metricool

Metricool is the planner the team already uses, and it is connected to this workspace as a
connector. Two ways to get the 56 posts and 5 threads in:

## 1. Through the connector (recommended; handles threads)

Prerequisite: the @swarm_coin X account is connected in Metricool (X is a paid add-on on the
Starter plan or higher; the Free plan cannot connect X). Today the brand "bjornseiz" has
Instagram, LinkedIn and TikTok but no X.

Once X is connected, ask the assistant in this workspace:

> Push campaign/x/calendar.json to Metricool for the brand with X connected, as drafts first.

It will call `createScheduledPost` once per calendar entry with `providers: [{network: "twitter"}]`,
the `text`, the thread posts as `descendants`, the `media` URL where there is one, and the
`publicationDate` converted to the brand's timezone. Posts can be created as drafts
(`draft: true`) for a last look in the planner, then switched on.

Then set the repository variable `SWARM_SOCIAL_SCHEDULER=0`, so the agent's scheduler does
not publish the same posts a second time.

## 2. CSV import (no threads)

`x/metricool-import.csv` has one row per post with the local date and time (brand timezone,
America/Santo_Domingo). Metricool's bulk importer wants its own column layout; open their
template in the planner, paste the columns across, import, and add the five threads by hand
from the "Thread" column (they are the Wednesday 16:00 UTC posts).

## Checking the schedule

`getScheduledPosts` for the brand shows what is in the planner; compare against
`x/calendar.md`. The build tool (`python tools/build_calendar.py`) rebuilds the JSON, CSV and
Markdown from `x/calendar.yaml` after every edit and refuses anything that breaks the policy.
