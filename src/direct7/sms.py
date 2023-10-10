import logging

log = logging.getLogger(__name__)


class SMS:

    def __init__(self, client):
        self._client = client

    def send_message(self, recipients: list, content: str, originator: str, report_url: str = None,
                     unicode: bool = False):
        """
        Send a message to a single/multiple recipient.
        :param recipients: list - Mobile Numbers to send SMS seperated by comma in an array.
        :param content: str - The message content is being sent.
        :param originator: str - The Sender/Header of a message.
        :param report_url: str - receive delivery status.
        :param unicode: boolean - To know the msg contain unicode data or not.
        :return:
        """

        message = {
            "channel": "sms",
            "recipients": recipients,
            "content": content,
            "msg_type": "text",
            "data_coding": "unicode" if unicode else "text"
        }
        message_globals = {
            "originator": originator,
            "report_url": report_url
        }
        response = self._client.post(self._client.host(), "/messages/v1/send", params={"messages": [message], "message_globals": message_globals})
        log.info("Message sent successfully.")
        return response

    def get_status(self, request_id: str):
        """
        Get the status for a message request.
        :param params:
        request_id : str - The request ID of the message request.
        :return:
        """
        response = self._client.get(
            self._client.host(),
            f"/report/v1/message-log/{request_id}"
        )
        log.info("Message status retrieved successfully.")
        return response
