#! /usr/bin/bash
cd /users/e/t/etosch/CS295A-S22
make build
source venv/bin/activate
cd - 
chmod +x /users/e/t/etosch/CS295A-S22/scripts/email_notifications.py
/users/e/t/etosch/CS295A-S22/scripts/email_notifications.py /users/e/t/etosch/CS295A-S22/src/schedule.md 43f7098c.uvmoffice.onmicrosoft.com@amer.teams.ms
chmod +x ./.send_email.sh
./.send_email.sh
