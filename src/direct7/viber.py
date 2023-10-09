import logging

log = logging.getLogger(__name__)


class VIBER:

    def __init__(self, client):
        self._client = client

    def send_viber_message(self, params: dict):
        """
        Send a viber message to a single/multiple recipient.
        :param params: dict - The message request parameters.
        :return:
        """
        response = self._client.post(
            self._client.host(),
            "/viber/v1/send",
            params=params
        )
        log.info("Message sent successfully.")
        return response

    def get_status(self, request_id: str):
        """
        Get the status for a viber message request.
        :param params:
        request_id : str - The request ID of the viber message request.
        :return:
        """
        response = self._client.get(
            self._client.host(),
            f"/report/v1/viber-log/{request_id}"
        )
        log.info("Message status retrieved successfully.")
        return response