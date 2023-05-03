## SSL Reminder use python - telegram

System Requierements : 
    - Crontab
    - pyhton 3
    - internet connection

created crontab as do you need

run on shell : python rem-ssl.py

on log :
----------------------------------------------------------
2023-05-03 13:10:32.358051
{'ok': True, 'result': {'message_id': 25, 'from': {'id': 6105186413, 'is_bot': True, 'first_name': 'xxxxxxx Reminder', 'username': 'xxxxxxBot'}, 'chat': {'id': -88888888, 'title': 'xxxxxxx Reminder', 'type': 'group', 'all_members_are_administrators': True}, 'date': 1683094233, 'text': 'Hello! \n\nThe certificate for your domain xxxxxx.com is about to expire in 171 days.\nThe exact date is: 2023-10-22 07:27:44\n\nPlease update the certificate as soon as possible.\n\nBest regards\nCerticate Checkbot - SSLChecker', 'entities': [{'offset': 41, 'length': 16, 'type': 'url'}]}}
----------------------------------------------------------

on telegram :
----------------------------------------------------------
Hello! 

The certificate for your domain www.xxxxxxxx.co.id is about to expire in 171 days.
The exact date is: 2023-10-22 07:27:44

Please update the certificate as soon as possible.

Best regards
Certicate Checkbot - SSLChecker
----------------------------------------------------------
