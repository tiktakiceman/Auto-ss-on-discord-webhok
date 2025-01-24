Auto-Screenshot-and-Discord-Uploader
This Python script automatically captures screenshots every 10 seconds, saves them in date-based folders, and uploads them to a Discord channel via a webhook. The screenshots are timestamped for easy tracking. The script can run invisibly in the background and be set to start automatically on boot, ideal for monitoring or logging tasks.

Features
Automatic Screenshot Capture: Takes a screenshot every 10 seconds.
Date-based Folder Organization: Creates folders named after the current date (in DD_MM_YYYY format) and saves the screenshots in these folders.
Custom Timestamped Filenames: Each screenshot is saved with a filename in the format shot_HHH_MMM_SSS_AMPM.png (e.g., shot_H09_M16_S22AM.png), including hours, minutes, seconds, and AM/PM.
Discord Webhook Integration: Automatically uploads each screenshot to a specified Discord channel via a webhook with a custom message containing the time the screenshot was taken.
Runs in the Background: Can be set to run at startup using pythonw, so it works without a console window.
