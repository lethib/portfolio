from crypt import methods
from flask import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from password import *

app = Flask(__name__)
app.secret_key = "thibwebdev"

@app.route('/', methods=["POST","GET"])
def home():
    ok = request.args.get('ok') #On récupère l'argument
    if request.method == "POST":
        demande_info = request.form
        msg = MIMEMultipart()
        msg['From'] = 'portfolio.lethib@gmail.com'
        msg['To'] = 'thibault.mroz76@gmail.com'
        msg['Subject'] = demande_info['prenom'] + ' ' +  demande_info['nom'] + ' vous a envoyé une nouvelle demande : ' + demande_info['objet']
        message = 'Mail contact : '+ demande_info['mail'] + '\n' + 'Numéro de téléphone : ' + demande_info['tel'] + '\n\n' + demande_info['message']
        msg.attach(MIMEText(message))

        mailserver = smtplib.SMTP('smtp.gmail.com',587)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login('portfolio.lethib@gmail.com', password)

        mailserver.sendmail('portfolio.lethib@gmail.com','thibault.mroz76@gmail.com',msg.as_string())

        print('Mail sent')
        mailserver.quit()

        return render_template('index.html', ok=True)
    else:
        return render_template('index.html', ok=False)

if __name__ == '__main__':
    app.run(debug=True)