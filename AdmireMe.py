# Task  :
# 1. URL of user Avatar.
# 2. Congratulation to User GIF Operation.
# 3. Email Operation.
# 4. Image Attachment to the Mail.

import cv2
import json
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase 
from email import encoders
from urllib.request import urlopen
import numpy as np
import os

parsed_json=json.loads(sys.argv[1])

image_url=str(parsed_json['user']['avatarUrl'])
email=str(parsed_json['user']['email'])
username=str(parsed_json['user']['login'])


org=str(sys.argv[2])

# Congratulation Operation
#fnt = ImageFont.truetype("arial.ttf", 36)
def create_imageo_with_text(size, text):
    imgo = Image.new('RGB', (600, 50), "white")
    drawo = ImageDraw.Draw(imgo)
    drawo.text((size[0], size[1]), text, fill="black")
    return imgo
 
frameso = []
 
def rollo(text):
    for i in range(len(text)+1):
        new_frameo = create_imageo_with_text((0,0), text[:i])
        frameso.append(new_frameo)

user=username

all_texto = """ >> Congratulations!""",user
""">>Done""".splitlines()
[rollo(text) for text in all_texto]

name = os.path.splitext(user)[0] + '.gif'
frameso[0].save(name, format='GIF',
        append_images=frameso[1:], save_all=True, duration=180, loop=0)

ProcessedGifURL="https://github.com/Pratham31/AdmireME/blob/master/"+name


# email operation

sender_mailID = "admiremeopensource@gmail.com"
receiver_mailID = email
password = str(os.environ['GKEY'])

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
msg = MIMEMultipart()
msg['Subject'] = '@'+username+', Thank you for your Contribution.'
msg['From'] = "Prathamesh Giri"
msg['To'] = receiver_mailID
msgText = MIMEText(
    '<center><h1>Thank you &#58130; @'+username+'&#58130;; | Congratulations!</h1><img style="width:100%;" src="https://i.ibb.co/vQCzVDK/devv.png"></img><center><p><t>Hello <b>@'+username+'</b>, <br><br>Thank you for your contribution in <b>'+org+'</b>.&#128519;<br><b>Note - Please find the attached files.</b><br><br>~ Organization Maintainer <b>@'+org+'</b></p><center><img style="width:20em; height:auto;" src="https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif"></img><br></br><br></br><br></br></center></center><div style="text-align:center;width:100%;padding:20px;background:black;color:white;">Powered by Github Actions &emsp; &emsp; &emsp; | &emsp; &emsp; &emsp; Made for DEV.to Hackathon.<br><br><br><img style="width:100%; height:auto;" src="https://i.ibb.co/TwNc306/Thanking-Note.gif"></img><div></div>', 'html')
msg.attach(msgText)


# attach image
    
#foreground = Image.open("https://i.ibb.co/tZhss9t/Congratulation.png")
foreground=requests.get("https://i.ibb.co/tZhss9t/Congratulation.png")
response = requests.get(image_url)
fimg = Image.open(BytesIO(foreground.content))
img = Image.open(BytesIO(response.content))
img.paste(fimg, (10, 10), fimg)
#img.save('finals.jpg', quality=95)
#filename="finals.jpg"
#f=file(filename)
#finalimg=MIMEText(f.read())
#finalimg = MIMEImage(img.read())
save_b = BytesIO()
img.save(save_b, format='PNG')
save_b = save_b.getvalue()
img = BytesIO(save_b)
finalimg = MIMEImage(img.read())
finalimg.add_header('Content-Disposition', 'attachment', filename="You.jpg")
msg.attach(finalimg)


server.login(sender_mailID, password)
server.sendmail(sender_mailID, receiver_mailID, msg.as_string())
print("Email has sent Successfully")

