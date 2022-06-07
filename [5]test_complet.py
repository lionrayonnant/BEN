class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import string
import random
import json
import qrcode
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#caractère_chaine_generator
nb_de_chaine = 1
nb_de_caractère = 16
for x in range(nb_de_chaine):
  qrdata = (''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(nb_de_caractère)))

  print(
    '\n'+ "La nouvelle chaine de caratère : " + color.BOLD + color.RED + qrdata + '\033[0m' + 
    " a bien étais crée "
    )


#écrire_dans_json
fileName = "data.json"
jsonObject = {
    "cdc" : (qrdata)
}

file = open(fileName, "w")
json.dump(jsonObject, file)
file.close()

print(
    "La chaine de caratère : " + color.BOLD + color.RED+ qrdata + '\033[0m' + 
    " a bien été enregistré dans le fichier : " + color.BOLD + color.UNDERLINE + color.PURPLE + "data.json" + '\033[0m'
    )


#qr_code_generator
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(qrdata)
qr.make(fit=True)

img = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))
img.save('QR_code_' + qrdata + '.png')

print(
    "QR-code crée : " + color.BOLD + color.UNDERLINE + color.PURPLE + 'QR_code_' + qrdata + '.png' + '\033[0m' + 
    " la chaine de caractère associée : " + color.BOLD + color.RED + qrdata + '\033[0m'
    )


#evoyer_mail
Objet_du_message = "Test1"
contenu_du_message = "Test2"
expéditeur = "robot.livreur.2022@gmail.com"
mot_de_passe = input('\n'+ color.CYAN + color.BOLD +    "mot de passe : "     + '\033[4m' + '\033[95m')
receveur = input('\033[0m'+ color.CYAN + color.BOLD +        "mail du client : "   + '\033[4m' + '\033[95m')
print('\033[0m')
piece_jointe = 'QR_code_' + qrdata + '.png'

message = MIMEMultipart()
message["From"] = expéditeur
message["To"] = receveur
message["Subject"] = Objet_du_message
message["Bcc"] = receveur

message.attach(MIMEText(contenu_du_message, "plain"))

with open(piece_jointe, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
   
encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {piece_jointe}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(expéditeur, mot_de_passe)
    server.sendmail(expéditeur, receveur, text)

print("le QR-code : " + color.BOLD + color.PURPLE + color.UNDERLINE + 'QR_code_' + qrdata + '.png' + '\033[0m' + 
    " a bien était envoyé à : " + color.BOLD + color.RED + receveur + '\033[0m' +'\n'
    )