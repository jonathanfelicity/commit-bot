import os
import subprocess
import time
from datetime import datetime, timedelta

# Set the path to the file that you want to commit
file_path = "file.txt"

# Set the start date to January 1st
start_date = "2022-01-01"

# Set the current date to the start date
current_date = start_date

# Set the end date to the current date
end_date = time.strftime("%Y-%m-%d")

# Calculate the number of days between the start and end dates
start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
num_days = (end_datetime - start_datetime).days + 1

for i in range(num_days):
    # Set the commit message
    commit_message = f"Commit {i+1} of {num_days}"

    # Add the commit message to the file
    with open(file_path, "a") as f:
        f.write(f"\n{commit_message}")

    # Add the file to the staging area
    subprocess.run(["git", "add", file_path])

    # Set the commit date to the current date
    os.environ["GIT_AUTHOR_DATE"] = current_date + " 12:00:00"
    os.environ["GIT_COMMITTER_DATE"] = current_date + " 12:00:00"

    # Commit the file with the specified date and message
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push the commit to GitHub
    time.sleep(2)
    subprocess.run(["git", "push"])

    # Increment the current date by one day
    current_datetime = datetime.strptime(current_date, "%Y-%m-%d")
    current_datetime += timedelta(days=1)
    current_date = current_datetime.strftime("%Y-%m-%d")
