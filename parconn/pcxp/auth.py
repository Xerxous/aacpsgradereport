import requests

session = requests.Session()

def login(USERNAME, PASSWORD):
	url = 'https://parentconnect.aacps.org/Login.asp?LoginState=2'
	session.get(url,verify=False)
	login_data = dict(RegisterMe=1,UserID=USERNAME, UserPwd=PASSWORD)
	session.post(url, data=login_data, headers={'Referer':'https://parentconnect.aacps.org/'})
	return session
