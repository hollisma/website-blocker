# Can leave as a background task. Will check if the current time is in your working time every hour
# and add/remove the list of blocked sites.

import time
from datetime import datetime as dt
# importing datetime twice like this so we can do dt.now()
# otherwise it have to be datetime.datetime.now()

# must put one site on each line, no quotes
# should put both 'www.facebook.com' and 'facebook.com'
nameOfFilesWithSites = 'badSites.txt'


# this will depend on OS used
# r allows us to use the \ char
# WINDOWS
# hosts_path=r'C:\Windows\System32\drivers\etc\hosts'
# UBUNTU and MAC
hosts_path = '/etc/hosts'

redirect = '127.0.0.1'

# get the list of sites to be blocked
f = open(nameOfFilesWithSites, 'r')
sites = f.readlines()
rip_productivity = []  # this is the array of sites to be blocked
for s in sites:
    rip_productivity.append(s.strip())
f.close()

while True:
    rn = dt.now()
    # if in working hours
    if dt(rn.year, rn.month, rn.day, 9) < rn < dt(rn.year, rn.month, rn.day, 17):
        print('Do some work :)')

        # write to the hosts_path file
        # with keyword basically is a safe way to make a context
        # 'r+' means read and write
        with open(hosts_path, 'r+') as file:
            content = file.read()  # reads entire file

            # write each site in sites_that_kill_me to hosts_path
            for site in rip_productivity:
                if site in content:
                    pass
                else:
                    file.write(redirect+' '+site+'\n')
    # not in working hours
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()  # array of lines in hosts_path
            file.seek(0)  # move pointer to beginning of file
            for line in content:
                # if a line doesn't contain a bad site
                if not any(site in line for site in rip_productivity):
                    file.write(line)
            file.truncate()  # deletes everything after the file pointer
        print('have funnn!!!')
    # will update every hour
    time.sleep(3600)

