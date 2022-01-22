#!/usr/bin/env python3

# Extracts the dates from schedule.md marked Lecture
# and writes those dates - 1 to schedule.txt

# Feels silly to import all of pandas just to read a 
# markdown table, but oh well.

import argparse, os, subprocess
from email.utils import parsedate
from urllib import response
from utils import read_markdown_table
from dateutil.parser import parse as dateparse
from dateutil.relativedelta import relativedelta
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument("schedule_file")
parser.add_argument("email")


args = parser.parse_args()
today = date.today()

schedule = read_markdown_table(args.schedule_file)
# just get the dates for lectures
dates = schedule[schedule["Form"].str.contains("Lecture")]["Date"] 
# now get the future dates
future = dates[dates.apply(dateparse) > dateparse(str(today))]
next_lecture = future.iloc[0]
# now get the reminders already sent
# we exepect to execute the cron job daily, but 
# over weekends that means we might send more than one reminder
# Let's ensure we only send one between now and the next date
if not os.path.exists(".schedule"):
    with open(".schedule", "w") as f:
        # get the last date 
        pass

last_emailed = None
with open(".schedule", "r") as f:
    lines = f.readlines()
    if len(lines) > 0:
        last_emailed = parsedate(lines[-1])

email_text = """From: Emma.Tosch@uvm.edu
To: {to_email}
Subject: Blogging for Lecture ({lecture_date})

@Artificial Intelligence (202201-NE-Crosslisted) CS295A/CS395D The next opportunity to 
blog is for lecture on {lecture_date}. Please respond to this message by 9pm on 
{response_date} if you would like to create a blog post for lecture on {lecture_date}.

See the blogging guidelines for more information:
https://uvm.edu/~etosch/CS295A-S22/blogging_guidelines.html
""".format(
        to_email = args.email,
        lecture_date = next_lecture,
        response_date = (dateparse(next_lecture) + relativedelta(days=-1)).strftime("%a, %b %d"))

print(email_text)
# if the last email wasn't about this lecture, send
if last_emailed != next_lecture:
    subprocess.run(["sendmail", args.email, email_text])
    # write the date to .schedule
    with open(".schedule", "w") as f:
        f.write(str(next_lecture)+"\n")    