Instructions; put websiteBlocker.py and badSites.txt into the same folder. Update websiteBlocker.py and enter your start and end times for your 'working hours,' then update badSites.txt to put in the websites you want blocked. If you want to use the blocker for x amount of hours, go into websiteBlocker.py and update the start and end hours to reflect how long you want the blocker to work for. 

To run, make sure you 'run as administrator' in Windows, or do 'sudo python websiteBlocker.py' in the folder. 

If you don't want to keep the process running in a window, then you can either make it a background process by going to task manager, or you can run the program twice: once when you want to blocking to start and once when you want it to end. In a dire situation where you need to use one of the websites, you can go into websiteBlocker.py and update the end time. 

If a website isn't being blocked, try including the website name with and without the 'www.' 

Ubuntu issue: a recent version of Ubuntu includes dnsmasq, which caches data on the chrome browser, allowing the blocker to run only once before it must be manually reset. If a workaround is found, please let me know. 


