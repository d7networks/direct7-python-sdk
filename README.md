# Direct7 Python SDK

This Python SDK provides a convenient and easy-to-use interface to the Direct7 REST API. The SDK allows you to perform
all the operations that are available through the REST API.

## Installation

The SDK is available on PyPI and can be installed using `pip`:

```bash
pip install direct7
```

## Usage

The SDK is designed to be easy to use. To get started, you need to create a client instance:


### Send SMS

```python
from direct7 import Client

client = Client(api_token="Your API token")

message_payload = {
    "messages": [
            {
                "channel": "sms",
                "recipients": ["9715090XXXXXX"],
                "content": "Greetings from D7 API",
                "msg_type": "text",
                "data_coding": "text"
            }
    ], 
    "message_globals": {
        "originator": "SignOTP",
        "report_url": "https://the_url_to_recieve_delivery_report.com"
    }
}

client.sms.send_message(message_payload)
```


### Get Request Status

```python
from direct7 import Client

client = Client(api_token="Your API token")

# request_id is the id returned in the response of send_message
client.sms.get_status(request_id="0012c7f5-2ba5-49db-8901-4ee9be6dc8d1")
```

## FAQ

### How do I get my API token?

You can get your API token from the Direct7 dashboard. If you don't have an account yet, you can create one for free.

### Supported Python versions

The SDK supports Python 3.6 and higher.

### Supported APIs

As of now, the SDK supports the following APIs:

| API                    |        Supported?        |
|------------------------|:------------------------:|
| SMS API                |            ✅             |
| Verify API             |            ❌             |
| Whatsapp API           |            ❌             |
| Number Lookup API      |            ❌             |
| Viber API              |            ❌             |
| Slack API              |            ❌             |

### How do I get started?

You can find the platform documentation @ [Direct7 Docs](https://d7networks.com/docs/).

### How do I get help?

If you need help using the SDK, you can create an issue on GitHub or email to support@d7networks.com

## Contributing

We welcome contributions to the Direct7 Python SDK. If you have any ideas for improvements or bug fixes, please feel
free to create an issue on GitHub.