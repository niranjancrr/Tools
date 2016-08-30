import jenkinsapi 
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.utils.requester import Requester
import requests
import time
import sys,os
import pdb

enabled_jobs = {}
disabled_jobs = {}
all_jobs = {}

def populateJenkinsStatus(jenk_obj):
    counter = 1
    while(1):
        try:
            items = jenk_obj.items()
            break
        except:
            counter = counter + 1
            print "Attempt {}" .format(counter)
     
    return items

def displayJobStatus(all_jobs):
    print "\nJob Status is:\n"
    col_width = max([all_jobs[key][0][0].__len__() for key in all_jobs.keys()])
    col_width2 = max(all_jobs.keys())
    for entry in all_jobs.keys():
        print " {}. {} \t\t {}" .format(entry,all_jobs[entry][0][0].ljust(col_width),all_jobs[entry][1])
   
def changeJobState2(choice,user_action,all_jobs):

    for user_choice in choice:
        if user_action == 'enable':
            while(1):
                try:
                    all_jobs[int(user_choice)][0][1].enable()
                    all_jobs[int(user_choice)][1] = 'Enabled'
                    print "Successfully enabled job: {}" .format(all_jobs[int(user_choice)][0][0])
                    break
                except:
                    print "Failed to enable job: {}" .format(all_jobs[int(user_choice)][0][0])
            time.sleep(0.25)
        elif user_action == 'disable':
            while(1):
                try:
                    all_jobs[int(user_choice)][0][1].disable()
                    all_jobs[int(user_choice)][1] = 'Disabled'
                    print "Successfully disabled job: {}" .format(all_jobs[int(user_choice)][0][0])
                    break
                except:
                    print "Failed to disable job: {}" .format(all_jobs[int(user_choice)][0][0])
            time.sleep(0.25)
        elif user_choice == 'exit' or user_action == 'exit':
            sys.exit(0)
        else:
            print "Invalid option(s). Please try again. Type exit to quit program"

def changeJobState(all_jobs):

    while(1):
        try:
            choice = raw_input('\nJob number(s) separated by \',\' to be modified: ')
            if choice == 'exit':
                raise
            user_choice = choice.split(',')
            #user_choice = int(raw_input('\nJob number to be modified: '))
            user_action = raw_input('\ndisable/enable: ')
        except:
            input = raw_input("Do you wish to exit this script (y/n): ")
            if (input == 'y'):
                print "Exiting Script!!"
                sys.exit()
            elif (input == 'n'):
                print "Continuing!!"
                continue
            else:
                print "Please enter a valid option (y/n): " 
                continue

        if int(user_choice[0]) == 0:
            for choice in range(all_jobs.__len__()):
                changeJobState2([int(choice)+1], user_action, all_jobs)
            break
        else:
            changeJobState2(user_choice, user_action, all_jobs)
            break

def populateBasicParameters(jenk_obj,all_jobs):

    items = populateJenkinsStatus(jenk_obj)
    counter = 0
    for item in items:
        counter = counter + 1
        if item[1].is_enabled():
            all_jobs[counter] = [item,'Enabled']
        else:
            all_jobs[counter] = [item,'Disabled']

def main():

    url = 'https://XXXXXXXXXXXXXXXXXXX:8080'
    username = '***********'
    password = '**********************'

    jenk_obj = Jenkins(url,requester=Requester(username, password, baseurl=url, ssl_verify=False))

    os.system('clear')
    print "\n\njenkins version is : {}" .format(jenk_obj.version)
    print "\njenkins url is : {}" .format(url)

    while(1):
        try:
            populateBasicParameters(jenk_obj,all_jobs)
            break
        except:
            continue

    while(1):
        os.system('clear')
        displayJobStatus(all_jobs) 
        changeJobState(all_jobs)

if __name__=='__main__':
    main()


