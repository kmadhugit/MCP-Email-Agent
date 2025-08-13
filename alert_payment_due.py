def alert_payment_due(email):
    print(f"[PAYMENT ALERT] Payment due detected in email: {email['subject']} - {email['body']}")
