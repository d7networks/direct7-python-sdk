import logging

log = logging.getLogger(__name__)


class VERIFY:

    def __init__(self, client):
        self._client = client

    def send_otp(self, params: dict):
        """
        Send an otp to a single recipient.
        :param params: dict - The message request parameters.
        :return:
        """
        response = self._client.post(
            self._client.host(),
            "/verify/v1/otp/send-otp",
            params=params
        )
        log.info("OTP Message sent successfully.")
        return response

    def resend_otp(self, params: dict):
        """
        Re-send an otp to a single recipient.
        :param params: dict - The message request parameters.
        :return:
        """
        response = self._client.post(
            self._client.host(),
            "/verify/v1/otp/resend-otp",
            params=params
        )
        log.info("OTP Message Re-sent successfully.")
        return response

    def verify_otp(self, params: dict):
        """
        Verify an otp.
        :param params: dict - The message request parameters.
        :return:
        """
        response = self._client.post(
            self._client.host(),
            "/verify/v1/otp/verify-otp",
            params=params
        )
        log.info("OTP Message verified successfully.")
        return response

    def get_status(self, otp_id: str):
        """
        Get the status for a otp request.
        :param params:
        request_id : str - The OTP ID of the message request.
        :return:
        """
        response = self._client.get(
            self._client.host(),
            f"/verify/v1/report/{otp_id}"
        )
        log.info("OTP Message status retrieved successfully.")
        return response
