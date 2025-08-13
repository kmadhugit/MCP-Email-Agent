from openai import OpenAI
from mcp_client import fetch_emails_from_mcp
from alert_payment_due import alert_payment_due
from alert_meeting import alert_meeting
from alert_package_delivery import alert_package_delivery

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "alert_payment_due",
            "description": "Trigger when an email contains payment due information",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "object"}
                },
                "required": ["email"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "alert_meeting",
            "description": "Trigger when an email contains meeting information",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "object"}
                },
                "required": ["email"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "alert_package_delivery",
            "description": "Trigger when an email contains package delivery information",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "object"}
                },
                "required": ["email"]
            }
        }
    }
]

def main():
    emails = fetch_emails_from_mcp()
    for email in emails:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI that detects types of alerts from emails and calls the right tool."},
                {"role": "user", "content": f"Email: {email}"}
            ],
            tools=tools
        )

        if response.choices[0].message.tool_calls:
            for tool_call in response.choices[0].message.tool_calls:
                name = tool_call.function.name
                args = tool_call.function.arguments
                if name == "alert_payment_due":
                    alert_payment_due(email)
                elif name == "alert_meeting":
                    alert_meeting(email)
                elif name == "alert_package_delivery":
                    alert_package_delivery(email)

if __name__ == "__main__":
    main()
