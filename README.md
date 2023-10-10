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

client.sms.send_message(recipients = ["+97150900XXXX","+97845900XXX"], content = "Greetings from D7 API", originator = "SignOTP", report_url = "https://the_url_to_recieve_delivery_report.com", unicode: False)
```


### Get Request Status

```python
from direct7 import Client

client = Client(api_token="Your API token")

# request_id is the id returned in the response of send_message
client.sms.get_status(request_id="0012c7f5-2ba5-49db-8901-4ee9be6dc8d1")
```

### Send OTP

```python
from direct7 import Client

client = Client(api_token="Your API token")

client.verify.send_otp(originator="SignOTP", recipient="+97150900XXXX", content = "Greetings from D7 API, your mobile verification code is: {}", expiry = 600, data_coding = "text")
```

### Re-Send OTP

```python
from direct7 import Client

client = Client(api_token="Your API token")

client.verify.resend_otp(otp_id="0012c7f5-2ba5-49db-8901-4ee9be6dc8d1")
```

### Verify OTP

```python
from direct7 import Client

client = Client(api_token="Your API token")

client.verify.verify_otp(otp_id="0012c7f5-2ba5-49db-8901-4ee9be6dc8d1", otp_code="1425")
```

### Get Request Status

```python
from direct7 import Client

client = Client(api_token="Your API token")

# otp_id is the id returned in the response of send_otp
client.verify.get_status(otp_id="0012c7f5-2ba5-49db-8901-4ee9be6dc8d1")
```

### Send Viber Message

```python
from direct7 import Client

client = Client(api_token="Your API token")

client.viber.send_viber_message(recipients=["+97150900XXXX","+97845900XXX"], content="Greetings from D7 API", label="PROMOTION", originator="INFO2WAY", report_url="https://the_url_to_recieve_delivery_report.com")
```


### Get Request Status

```python
from direct7 import Client

client = Client(api_token="Your API token")

# request_id is the id returned in the response of send_viber_message
client.viber.get_status(request_id="0012c7f5-2ba5-49db-8901-4ee9be6dc8d1")
```

### Send Slack Message

```python
from direct7 import Client

client = Client(api_token="Your API token")

client.slack.send_slack_message(content="Greetings from D7 API", work_space_name="WorkspaceName", channel_name="ChannelName", report_url="https://the_url_to_recieve_delivery_report.com")
```


### Get Request Status

```python
from direct7 import Client

client = Client(api_token="Your API token")

# request_id is the id returned in the response of send_slack_message
client.slack.get_status(request_id="0012c7f5-2ba5-49db-8901-4ee9be6dc8d1")
```

### Search Your Number details

```python
from direct7 import Client

client = Client(api_token="Your API token")

client.number_lookup.search_number_details(recipient="+914257845XXXX")
```

### Send Whatsapp Free-form Message (Contact Details)

```python
from direct7 import Client

client = Client(api_token="Your API token")

client.whatsapp.send_whatsapp_freeform_message(originator="91906152XXXX", recipients="str", message_type="CONTACTS", first_name="Amal", last_name="Anu", display_name="Amal Anu", phone="91906152XXXX", email = "amal@gmail.com")
```

### Send Whatsapp Templated Message.

```python
from direct7 import Client

client = Client(api_token="Your API token")

client.whatsapp.send_whatsapp_templated_message(originator="91906152XXXX", recipient="91906152XXXX", message_type="TEMPLATE", template_id="monthly_promotion", body_parameter_values={"0": "promotion"})
```

### Get Request Status

```python
from direct7 import Client

client = Client(api_token="Your API token")

# request_id is the id returned in the response of send_message
client.whatsapp.get_status(request_id="0012c7f5-2ba5-49db-8901-4ee9be6dc8d1")
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
| Verify API             |            ✅             |
| Whatsapp API           |            ✅             |
| Number Lookup API      |            ✅             |
| Viber API              |            ✅             |
| Slack API              |            ✅             |

### How do I get started?

You can find the platform documentation @ [Direct7 Docs](https://d7networks.com/docs/).

### How do I get help?

If you need help using the SDK, you can create an issue on GitHub or email to support@d7networks.com

## Contributing

We welcome contributions to the Direct7 Python SDK. If you have any ideas for improvements or bug fixes, please feel
free to create an issue on GitHub.
