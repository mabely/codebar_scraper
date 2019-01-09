import requests
import lxml
from bs4 import BeautifulSoup
import os

def getEvents():
    url = os.environ['SCRIPT_URL']
    events = requests.get(url)
    html_content = events.content

#    data = events.text
    soup = BeautifulSoup(html_content, 'lxml')

    sectionContent = soup.find('section', {'id': 'banner'})

    tagContent = sectionContent.find_all('span', {'class': 'label status'})
    
    count = 0
    
    for item in tagContent:
        city = item.text.strip()
        if city == 'London':
            count += 1
            print(True)
        else:
            print(False)
            
    if count > 0:
        return True, count
    else:
        return False, 0
        # print item.text

def sendNotification():
    city_output,city_count = getEvents()
    url = os.environ['WEBHOOK_URL']
    if city_output == True:
        if city_count == 1:
            message = {'text' : str.format('There is {} London event, sign up at https://codebar.io/events', city_count)}
        elif city_count > 1:
            message = {'text' : str.format('There are {} London events, sign up at https://codebar.io/events', city_count)}      
        requests.post(url, json=message)
    else:
        print('None')
    return city_output

sendNotification()
