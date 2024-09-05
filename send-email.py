import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.office365.com'
smtp_port = 587
email = 'seu_email'
password = 'sua_senha'


msg = MIMEMultipart()
msg ['From'] = email
msg ['To'] = 'destinatario'
msg ['Subject'] = 'Titulo do e-mail'

corpo = 'mensagem do email'
msg.attach(MIMEText(corpo, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email, password)
    texto = msg.as_string()
    server.sendmail(email, 'escreva o destinatario', texto)
    server.quit()
    print('Sucesso!')
except Exception as e:
    print(f'Erro no envio: {e}')
