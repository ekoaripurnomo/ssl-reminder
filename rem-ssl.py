# Maintained by ekoaripurnomo@gmail.com

import ssl, socket, time, datetime, requests

# Telegram settings monitoring
TOKEN = "12345678901:AABBCCddeeff_gghhiijjkk"
chat_id = "-888888888"

# domain name to be scan

url = ['online.hokben.net', 'pettycash.hokben.net', 'www.hokben.co.id' ]

# iterate thru list
for hostname in url:

    # send SSL request
    ctx = ssl.create_default_context()
    s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
    # there is no need that your ssl server runs on port 443. If you e.g. want to validdate a imaps connection, change the port here.
    s.connect((hostname, 443))
    cert = s.getpeercert()

    # get certificate expiration date
    valid = cert['notAfter']

    # process string date to date format
    validdate = datetime.datetime.fromtimestamp(int(time.mktime(datetime.datetime.strptime(valid, "%b %d %H:%M:%S %Y %Z").timetuple())))
    # get date from today
    today= datetime.datetime.now()

    # calculate difference between
    # difference = int((validdate - today).days)
    difference = (validdate - today).days

    # print(difference + 1)

    # simple process to alert 30, 14, 3, and 1 day in advance
    # if difference is 30 or difference is 14 or difference is 3 or difference is 1:

    # content for the email
    content = "Hello! \n\n" \
                "The certificate for your domain "+hostname+" is about to expire in "+str(difference)+" days.\n" \
                "The exact date is: "+str(validdate)+"\n\n" \
                "Please update the certificate as soon as possible.\n\n" \
                "Best regards\n" \
                "Certicate Checkbot - SSLChecker"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={content}"

    # send reminder if SSL will be expired under 30 days
    if difference <= 171:
        # send out message
        try:
            print(today)
            print(requests.get(url).json()) # this sends the message
            # print ("Successfully sent telegram message") # status message handled by telegram
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
