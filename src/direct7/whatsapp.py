import logging

log = logging.getLogger(__name__)


class WHATSAPP:

    def __init__(self, client):
        self._client = client

    def send_whatsapp_message(self, params: dict):
        """
        Send a whatsapp message to a single/multiple recipient.
        :param params: dict - The message request parameters.
        :return:
        """
        response = self._client.post(
            self._client.host(),
            "/whatsapp/v1/send",
            params=params
        )
        log.info("Message sent successfully.")
        return response


    def get_status(self, request_id: str):
        """
        Get the status for a whatsapp message request.
        :param params:
        request_id : str - The request ID of the whatsapp message request.
        :return:
        """
        response = self._client.get(
            self._client.host(),
            f"/whatsapp/v1/report/{request_id}"
        )
        log.info("Message status retrieved successfully.")
        return response
