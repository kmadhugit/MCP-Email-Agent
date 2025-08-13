def alert_package_delivery(email):
    print(f"[PACKAGE ALERT] Package delivery detected: {email['subject']} - {email['body']}")
