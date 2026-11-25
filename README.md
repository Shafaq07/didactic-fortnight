# Stay Here

## 1. Upload
Create a public GitHub repository and upload all these files.
Hidden folders often get skipped. If `.github` is missing: Add file > Create new file,
name it `.github/workflows/remind.yml`, paste the contents, commit.

## 2. Put the app online
Settings > Pages > Deploy from a branch > main, / (root) > Save.
Open the link on your phone, then browser menu > Add to Home screen.

## 3. Notifications
1. Install the **ntfy** app (Play Store / App Store) and allow notifications.
2. Subscribe to a long, hard to guess topic, e.g. `stay-` plus 15 random letters and numbers.
   Anyone who knows the name can read or send to it, so keep it private.
3. GitHub repo: Settings > Secrets and variables > Actions > New repository secret.
   Name: `NTFY_TOPIC`. Value: your topic name only.
4. Actions tab > Reminders > Run workflow. Your phone should buzz.

## Good to know
- GitHub may send a few minutes late, sometimes longer.
- GitHub pauses schedules after 60 days without repository activity. Re-enable in the Actions tab.
- For once a day, delete one `cron` line. Times are in UTC (India time minus 5:30).
