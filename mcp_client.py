import requests

def fetch_emails_from_mcp():
    url = "http://127.0.0.1:5001/emails"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
