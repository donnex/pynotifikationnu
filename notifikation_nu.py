import urllib
import json

class NotifikationNuApiError(Exception):
    pass

class NotifikationNu(object):
    """A library that provides a python interface to the
    Notifikation.nu API

    Example:
        notifikation_nu = NotifikationNu('API_KEY_FROM_NOTIFIKATION.NU')
        notifikation_nu.send_notification(ID, 'Notification message...')

    Both api key and notification id can be found on your account page on
    http://notifikation.nu
    """

    def __init__(self, api_key):
        self.api_key = api_key
        if len(self.api_key) != 40:
            raise ValueError('API key must be 40 characters.')

    def send_notification(self, notification_id, message):
        """Send a notification to the notification_id with message as
        notification content.
        """
        self.api_url = 'http://notifikation.nu/api/%s/send_notification/' % self.api_key
        self.post_data = {
            'id': notification_id,
            'message': message,
        }
        
        params = urllib.urlencode(self.post_data)
        self.api_reply_content = urllib.urlopen(self.api_url, params).read()
        self.api_reply = json.loads(self.api_reply_content)

        if not self.api_reply['status']:
            raise NotifikationNuApiError(self.api_reply['message'])
