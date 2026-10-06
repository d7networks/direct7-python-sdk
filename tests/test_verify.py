from unittest.mock import patch

from src.direct7 import Client

client = Client(api_token='Your API Token')
OTP_ID = "0012c7f5-2ba5-49db-8901-4ee9be6dc8d1"


@patch.object(Client, "post")
def test_verify_v1_post_paths_unchanged(mock_post):
    client.verify.send_otp(originator="SignOTP", recipient="+97150900XXXX",
                           content="Your code is: {}", expiry=600, data_coding="text")
    client.verify.resend_otp(otp_id=OTP_ID)
    client.verify.verify_otp(otp_id=OTP_ID, otp_code="1425")
    paths = [c.args[1] for c in mock_post.call_args_list]
    assert paths == ["/verify/v1/otp/send-otp", "/verify/v1/otp/resend-otp", "/verify/v1/otp/verify-otp"]
    assert mock_post.call_args_list[0].kwargs["params"] == {
        "originator": "SignOTP", "recipient": "+97150900XXXX",
        "content": "Your code is: {}", "expiry": 600, "data_coding": "text"}


@patch.object(Client, "get")
def test_verify_v1_get_status_path_unchanged(mock_get):
    client.verify.get_status(otp_id=OTP_ID)
    assert mock_get.call_args.args[1] == f"/verify/v1/report/{OTP_ID}"


@patch.object(Client, "post")
def test_verify_v2_post_paths(mock_post):
    client.verify.v2.resend_otp(otp_id=OTP_ID)
    client.verify.v2.verify_otp(otp_id=OTP_ID, otp_code="1425")
    paths = [c.args[1] for c in mock_post.call_args_list]
    assert paths == ["/verify/v2/otp/resend-otp", "/verify/v2/otp/verify-otp"]
    assert mock_post.call_args_list[1].kwargs["params"] == {"otp_id": OTP_ID, "otp_code": "1425"}


@patch.object(Client, "post")
def test_verify_v2_send_otp(mock_post):
    client.verify.v2.send_otp(recipient="+97150900XXXX", flow_id="login_flow")
    assert mock_post.call_args.args[1] == "/verify/v2/otp/send-otp"
    assert mock_post.call_args.kwargs["params"] == {
        "recipient": "+97150900XXXX", "flow_id": "login_flow"}


@patch.object(Client, "get")
def test_verify_v2_get_status_path(mock_get):
    client.verify.v2.get_status(otp_id=OTP_ID)
    assert mock_get.call_args.args[1] == f"/verify/v2/report/{OTP_ID}"
