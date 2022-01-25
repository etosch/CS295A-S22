#! /usr/bin/bash
set -e

REPO_DIR="/users/e/t/etosch/CS295A-S22"
SCRIPT_DIR="$REPO_DIR/scripts"

cd $REPO_DIR
git pull 
cd - 

echo "Generate emails"
chmod +x $SCRIPT_DIR/email_notifications.py 
source $REPO_DIR/venv/bin/activate
# this one sends to the test channel
#python $SCRIPT_DIR/email_notifications.py $SCRIPT_DIR/../src/schedule.md 43f7098c.uvmoffice.onmicrosoft.com@amer.teams.ms
python $SCRIPT_DIR/email_notifications.py $SCRIPT_DIR/../src/schedule.md 3ff19c61.uvmoffice.onmicrosoft.com@amer.teams.ms

echo "Send email"
chmod +x ~/.send_email.sh
~/.send_email.sh

