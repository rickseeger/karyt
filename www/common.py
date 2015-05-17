import random
import sendgrid

# This script uses the SendGrid Python Library
# https://github.com/sendgrid/sendgrid-python


def rand_string(length):
    txt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    s = ''
    for i in range(length):
        idx =  random.randint(0,len(txt)-1)
        s += txt[idx-1:idx]
    return(s)


def send_confirmation(email_address, confirm_key):
    api_user = 'rseeger'
    api_key = 'cyber1ad'

    email_to = email_address
    email_bcc = 'rick.seeger@gmail.com'
    email_from = 'noreply@kar.yt'
    subject = '[ACTION REQUIRED] Confirm your new kar.yt address'
    body = 'Thank you for registering a Karyt address<p>'
    body += 'Click the following link to complete your registration:<p>'
    body += 'http://kar.yt/confirm/' + confirm_key
    
    sg = sendgrid.SendGridClient(api_user, api_key)
    message = sendgrid.Mail()

    message.add_to(email_to)
    message.add_bcc(email_bcc)
    message.set_from(email_from)
    message.set_subject(subject)
    message.set_html(body)

    print 'Sending confirmation email to:', email_to
    (http_status_code, message) = sg.send(message)
    print 'http_status_code:', http_status_code
    print 'server_response:', message
