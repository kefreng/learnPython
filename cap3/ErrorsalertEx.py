alert_system = 'console'
error_severity = 'critial'
error_message = 'OMG!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == ' critial':
        #send_email('admin@example.com', error_message)
        print(error_message)
    elif error_severity == 'medium':
        #send_email('suppprt.1@example.com', error_message)
        print(error_message)
    else:
        #send_email('support.1@example.com', error_message)
        print(error_message)