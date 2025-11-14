import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

# Función para extraer resumen de una web (ejemplo para Navarra)
def extraer_navarra():
    url = "https://parlamentodenavarra.es/es/actividad-parlamentaria/calendario-de-sesiones"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    titulos = soup.find_all('h3')  # Ejemplo: títulos de sesiones
    resumen = "Agenda Navarra:\n"
    for t in titulos[:5]:
        resumen += "- " + t.get_text(strip=True) + "\n"
    return resumen

# Puedes crear funciones similares para otros parlamentos

# Función para enviar email con resumen
def enviar_email(cuerpo):
    remitente = "tu_email@gmail.com"
    destinatario = "carloscm@gfi.org"
    asunto = "Resumen semanal de agendas parlamentarias"

    msg = MIMEText(cuerpo)
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remitente, 'tu_contraseña')  # Usa contraseña de app si tienes 2FA
    servidor.sendmail(remitente, destinatario, msg.as_string())
    servidor.quit()

if __name__ == "__main__":
    resumen = extraer_navarra()
    # Añade otras agendas sin modificar el envío
    enviar_email(resumen)
