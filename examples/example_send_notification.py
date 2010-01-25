"""
Example for sending notifications with pynotifikationnu.
"""
from notifikation_nu import NotifikationNu

# Dummy API key
api_key = '1234567890123456789012345678901234567890'
# Dummy notification ID
notification_id = '1000'
# Notification message
message = 'Test notification'
# Another notification
message2 = 'Test notification 2'

notifikation_nu = NotifikationNu(api_key)
try:
    notifikation_nu.send_notification(notification_id, message)
    notifikation_nu.send_notification(notification_id, message2)
    print 'Successfully sent two notifications'
except Exception, e:
    print e
