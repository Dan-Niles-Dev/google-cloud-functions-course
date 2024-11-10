 def send_mail(request):
 
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    from flask import abort

    request_json = request.get_json(silent=True)
    parameters = ('sender', 'reciever', 'subject', 'message')
    sender, reciever, subject, message = '', '', '', '' 

    if request_json and all(k in request_json for k in parameters):
       sender = request_json['sender']
       reciever = request_json['reciever']
       subject = request_json['subject']
       message = request_json['message']
    else:
       abort(400)
    message = Mail(
        from_email=sender,
        to_emails=reciever,
        subject=subject,
        html_content=message)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        return e, 400
