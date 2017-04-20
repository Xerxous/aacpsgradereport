import time, traceback
from smtp import mail, reader
from parconn.pcxp import auth, parse

MAIN = 'woosuk2009@gmail.com'
path = reader.get_dir()
API_KEY = mail.get_key()
client = mail.create_client(API_KEY)
count = 0

while True:
    try:
        header = reader.get_header()
        secret = reader.get_cred(path)
        EMAILS = secret['emails']
        USERNAMES = secret['user']
        PASSWORDS = secret['pass']
        count += 1
        for i in range(len(EMAILS)):
            content = reader.get_body()
            session = auth.login(USERNAMES[i], PASSWORDS[i])
            assignments = '<b>New Assignments</b><br/>' + '<br/>'.join(parse.glued(session, 'ASSIGN_GEN', [1, 3, 5, 6, 7]))
            grades = '<b>Grades</b><br/>'+'<br/>'.join(parse.glued(session, 'ASSIGN_SCH', [0, 2, 4]))
            if not len(assignments):
                assignments = 'No Assignments yet.'
            if not len(grades):
                grades = 'No grades for this quarter. Not yet.'
            content += '<br/><br/>' + grades + '<br/><br/>' + assignments
            message = mail.create_message(EMAILS[i], header + str(count), content)
            sent = client.client.mail.send.post(request_body=message.get())
            print(sent.status_code)
            session.cookies.clear()
            print('sent to ' + EMAILS[i])
        time.sleep(43200)
    except KeyboardInterrupt:
        raise
    except:
    	message = mail.create_message(MAIN, 'GRADE REPORT ERROR', 'fix')
    	client.client.mail.send.post(request_body=message.get())
        traceback.print_exc()
    	time.sleep(43200)
