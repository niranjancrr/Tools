'''
Please replace admin@company.com with administrator email address
Please replace email.company.com with your email server
'''

import smtplib
import argparse
import time
from email.mime.text import MIMEText


def send_email(to,sub,body):

    msg = MIMEText(body)

    me = 'admin@company.com'
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ','.join(entry for entry in to)

    server = smtplib.SMTP('email.company.com')
    server.sendmail(me, to, msg.as_string())
    server.quit()

def main():

    try:

        parser = argparse.ArgumentParser()
        parser.add_argument('-to', action="append", dest='email_list', required=True)
        parser.add_argument('-sub', action="store", dest='email_sub', required=True)
        parser.add_argument('-body', action="store", dest='email_body', required=True)
        args = parser.parse_args()
 
        email_list = args.email_list
        email_sub = args.email_sub
        email_body = args.email_body

        flag = 0

        counter = 10

        while counter>0:
            try: 
                send_email(email_list,email_sub,email_body)

                print '\n********************************************************'
                print 'Email will be sent to: ' + str(args.email_list) + '\n'
                print 'Email subject: ' + str(args.email_sub) + '\n'
                print 'Email body: \n\n' + str(args.email_body) + '\n\n\n' + 'Please contact admin@company.com if you have any questions'
                print '********************************************************\n'

                flag = 1
                counter = 0

            except:
                time.sleep(1)
                counter -= 1
                continue 

        if flag == 1:
            print "\nEmail was sent successfully!\n"
        else:
            print "\nEmail sending Failed. Please check!\n"

    except:

        print "Usage is python email_notification.py -to 'email1,email2,...' -sub 'Email Subject' -body 'email body'"


if __name__ == '__main__':
    main()

