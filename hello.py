#!/usr/bin/env python3  # Use the system's Python 3 interpreter

from datetime import datetime  # Import the datetime module to get the current date and time

# Open the file 'cron_log.txt' located in the user's home directory in append mode
# If the file doesn't exist, it will be created
with open("/home/grey_dad/cron_log.txt", "a") as f:
    # Write a line to the file with the current timestamp
    # Each time this script runs, a new line is added showing the date and time
    f.write(f"Cron ran at: {datetime.now()}\n")

