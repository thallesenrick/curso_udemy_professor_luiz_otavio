from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'testethalles@outlook.com'
minha_senha = 'abobodada0906'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Thalles', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Thalles Enrick André Maciel'
msg['to'] = meu_email
msg['subject'] = 'Atenção: este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'E-mail não enviado... Erro: {e}')