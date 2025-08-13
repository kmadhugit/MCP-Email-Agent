from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/emails', methods=['GET'])
def get_emails():
    # Mock email data
    emails = [
        {"subject": "Payment Due Reminder", "body": "Your electricity bill of $100 is due tomorrow."},
        {"subject": "Team Meeting", "body": "The project meeting is scheduled for 3 PM today."},
        {"subject": "Package Delivery", "body": "Your Amazon package will be delivered by 5 PM today."}
    ]
    return jsonify(emails)

if __name__ == "__main__":
    app.run(port=5001)
