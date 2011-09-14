import urllib
try:
    import json
except ImportError:
    import simplejson as json

class NotifikationNuApiError(Exception):
    pass

class NotifikationNu(object):
    """A library that provides a python interface to the
    Notifikation.nu API
    """

    def __init__(self, api_key):
        self.api_key = api_key
        if len(self.api_key) != 40:
            raise ValueError('API key must be 40 characters.')

    def send_notification(self, notification_id, message, category='', event=''):
        """Send a notification to the notification_id with message as
        notification content. Category and event will override the
        values set on notifikation.nu.
        """
        self.api_url = 'http://notifikation.nu/api/%s/send_notification/' % (self.api_key,)
        self.post_data = {
            'id': notification_id,
            'message': message,
            'category': category,
            'event': event,
        }

        params = urllib.urlencode(self.post_data)
        self.api_reply_content = urllib.urlopen(self.api_url, params).read()
        self.api_reply = json.loads(self.api_reply_content)

        if not self.api_reply['status']:
            raise NotifikationNuApiError(self.api_reply['message'])
