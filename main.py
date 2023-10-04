from direct7 import Client

if __name__ == "__main__":
    client = Client(api_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoLWJhY2tlbmQ6YXBwIiwic3ViIjoiMzA5NzAwM2MtZjE2My00ODM0LTliODYtNzI0ZWJhNGNjNzBhIn0.XOvVnJimiVogSo3tQPAwm9e5K4_ihQKsbehiNRYDrzI")
data = {
    "messages": [
            {
                "channel": "sms",
                "recipients": ["971509001994"],
                "content": "Greetings from D7 API",
                "msg_type": "text",
                "data_coding": "text"
            }
    ], 
    "message_globals": {
        "originator": "SignOTP",
        "report_url": "https://webhook.site/c4c6109a-c134-4094-89d7-b23c710dace5"
    }
}
result  = client.sms.send_message(data)
print(result)