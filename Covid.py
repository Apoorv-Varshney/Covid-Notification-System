# Realtime Coronavirus Notification System

from plyer import notification # module for windows notification
import requests
import json
import time

def notifyMe(title, message): # creating windows notification
    notification.notify(
        title=title, 
        message=message,
        app_icon="C:\\Users\\Apoorv Varshney\\Desktop\\CovidNotify\\covid.ico", # icon path
        timeout=3 
    )

def getData(url): # function to get data from url
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:   
        myHtmlData=getData('https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true') # passing the url

        parseData=json.loads(myHtmlData) # parsing json data to dictionary
        region=parseData['regionData'] # getting statewise data
        state=['Uttar Pradesh','Rajasthan','Delhi','Maharashtra']

        for r in region[0:35]:
            st=r.get('region') # getting state name one by one

            if (st in state): # checking state name in state list
                ntitle="Cases of Covid-19" # setting title to notification window
                ntext=f"State : {st} \nActive-Today : {r['newInfected']}  \nRecovered-Today : {r['newRecovered']} \nDeaths-Today : {r['newDeceased']}" # setting cases

                notifyMe(ntitle,ntext) # passing title and message
                time.sleep(4) # pausing notification panel for 4 seconds

        time.sleep(3600) # next notification after 3600 seconds