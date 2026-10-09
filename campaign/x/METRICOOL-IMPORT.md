# Importing the X calendar into Metricool

For the owner. Every post goes in as a draft. Nothing is published until the owner switches a draft on.

- The calendar starts on Monday 12 October 2026 at 07:30 UTC, which is 03:30 local time in America/Santo_Domingo.
- The two exact-time posts are on 31 October and 1 November 2026 at 15:42 UTC, which is 11:42 local time.
- The files were built on 9 October 2026 from calendar.json by `make_metricool_csv.py` in this folder.

Files in this folder:

- `metricool-template-part1.csv`: the first 28 posts in time order.
- `metricool-template-part2.csv`: the remaining 29 posts.
- `metricool-threads.md`: the five threads and the first replies, added by hand.

## What Metricool's help article says

Source: https://help.metricool.com/en/article/how-to-schedule-posts-in-batch-with-a-csv-file-in-metricool-3wihqx/ (read on 9 October 2026).

- The import is in the Planning calendar, in the calendar options menu, under "Import CSV".
- In the window that opens, "Download template" gives Metricool's own template.
- The article says: "Don't delete or add columns".
- Networks and options are written as TRUE or FALSE.
- Draft = TRUE imports the post as a draft.
- The date example is "YYYY-MM-DD" and the time example is "00:00:00".
- During the import you must pick the same date and time format in the drop-down as in the file. A mismatch is the common error.
- Media must be a public direct link.
- The file must be saved as UTF-8.
- There is no hard limit, but up to 50 posts per file are recommended. That is why the calendar is split into two files.
- To import, you click "Import CSV", then "CSV File", and add the file. A window then shows errors, a preview and the import button.
- The article does not mention X threads at all. It covers single posts and polls only.

Our files use the date format YYYY-MM-DD and the time format HH:MM:SS (for example 03:30:00).

## Steps

### Before anything else

1. Open Metricool and select the SWARM brand.
2. Open Connections.
3. Click X and connect it to @swarm_coin. X is a paid add-on on the Starter plan or higher. The owner signs in to X; no agent holds the password (owner item 314).
4. Open the brand settings and read the brand's timezone. The CSV times are written for America/Santo_Domingo. If the brand uses another timezone, tell the session and it regenerates the files. Assumption: the brand timezone is America/Santo_Domingo, as an earlier session found; this needs checking.

### Check the template

5. Open the Planning calendar.
6. Open the calendar options menu.
7. Click "Import CSV".
8. Click "Download template" and save Metricool's template.
9. Open the downloaded template and our `metricool-template-part1.csv` side by side and compare the first line (the header line) of both.
10. If the header lines are the same, go on to step 11. If they differ, keep Metricool's template and paste our Text, Date, Time, Draft, Twitter/X, Picture Url 1 and First Comment Text columns into it, then save it as CSV UTF-8. Assumption: the article lists the columns but does not print the header text, so our header line is built from that list.

### Import part 1

11. In the Planning calendar, open the calendar options menu.
12. Click "Import CSV".
13. Click "CSV File".
14. Add `metricool-template-part1.csv`.
15. In the date format drop-down, pick YYYY-MM-DD.
16. In the time format drop-down, pick the format with seconds (00:00:00).
17. Read the error list and the preview. Check that the first row is on 2026-10-12 at 03:30:00 and that every post is a draft.
18. Click the import button.

### Import part 2

19. Open the calendar options menu again.
20. Click "Import CSV".
21. Click "CSV File".
22. Add `metricool-template-part2.csv`.
23. Pick YYYY-MM-DD in the date format drop-down.
24. Pick the format with seconds (00:00:00) in the time format drop-down.
25. Read the error list and the preview. Check that the posts on 2026-10-31 and 2026-11-01 show 11:42:00.
26. Click the import button.

### Threads and first replies

27. Open `metricool-threads.md`. It lists five threads with the local date and time, the UTC time, the opening post, the numbered follow-up posts and the first reply.
28. In the planner, open the first imported opening post that has a thread.
29. Add the follow-up posts as a thread, in the numbered order from `metricool-threads.md`. Assumption: the planner's X composer supports threads.
30. Save the post as a draft.
31. Repeat steps 28 to 30 for the other four threads.
32. Open one imported post that has a First Comment Text and check whether that text shows as the first reply for X. Assumption: Metricool applies the First Comment Text column to X.
33. If it did not become the first reply, add the first replies by hand from `metricool-threads.md` (for the threads) and from the First Comment Text column of the CSV files (for the other posts).

### Publishing stays with the owner

34. Leave every post as a draft. The owner switches drafts on, post by post or day by day. Nobody else publishes.
35. Once Metricool publishes the calendar, set the repository variable SWARM_SOCIAL_SCHEDULER to 0, so the agent's scheduler never publishes the same posts twice.

## If the Metricool connector is enabled in the session instead

The session pushes every post as a draft, with its thread and first reply, through the connector's createScheduledPost and then reports the count. The owner still switches the drafts on.
