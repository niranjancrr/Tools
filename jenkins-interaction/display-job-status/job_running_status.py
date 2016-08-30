import jenkinsapi 
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.utils.requester import Requester
import requests
import pdb
import time
import sys,os

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
   
def populateBasicParameters(jenk_obj,all_jobs):

    items = populateJenkinsStatus(jenk_obj)
    counter = 0
    for item in items:
        counter = counter + 1
        if item[1].is_running():
            all_jobs[counter] = [item,'Running']
        else:
            all_jobs[counter] = [item,'Idle']

def main():

    url = 'https://xxxxxxxx:8080'
    username = '*************'
    password = '*******************'

    jenk_obj = Jenkins(url,requester=Requester(username, password, baseurl=url, ssl_verify=False))

    os.system('clear')
    print "\n\njenkins version is : {}" .format(jenk_obj.version)
    print "\njenkins url is : {}" .format(url)
    print "\nviews on this page are: {}" .format(jenk_obj.views.keys())
    #print "\nFollowing are the jobs on this jenkins page : \n{}" .format(jenk_obj.get_jobs_list())

    while(1):
        try:
            populateBasicParameters(jenk_obj,all_jobs)
            break
        except:
            continue

    #while(1):
    os.system('clear')
    displayJobStatus(all_jobs) 

if __name__=='__main__':
    main()


