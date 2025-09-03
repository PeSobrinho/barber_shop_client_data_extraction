def send_email(sendgrid_api_key, client, client_email):
    
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail       

    with open('./configs/layout_email.html', 'r') as file:
        email_body = file.read()

    # Configurar o e-mail
    message = Mail(
        from_email = os.getenv('FROM_EMAIL'),  # E-mail do remetente
        to_emails = client_email,  # E-mail do destinatário
        subject = f'{client}, vamos conversar?',  # Assunto do e-mail
        html_content = email_body.format(nome = client)  # Corpo do e-mail (pode ser texto simples)
    )

    message.bcc = os.getenv('BCC_EMAIL')

    # Enviar o e-mail
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print('E-mail enviado com sucesso!')
        print('Status Code:', response.status_code)
        print('Resposta:', response.body)
        print(f'E-mail enviado para: {client} ({client_email})')
    except Exception as e:
        print("Erro ao enviar o e-mail:", str(e))

if __name__ == '__main__':  
    import data_extract as de
    
    import os
    from dotenv import load_dotenv

    load_dotenv() 

    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT', '5432')
    database = os.getenv('DATABASE')
    schema = os.getenv('SCHEMA')
    
    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')

    clients_data = de.extract_data(user, password, host, port, database)

    for _, row in clients_data.iterrows():
        client = row['nm_cliente']
        client_email = row['email_ficticio']
        send_email(sendgrid_api_key, client, client_email)