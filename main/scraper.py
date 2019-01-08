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

    for item in tagContent:

        city = item.text.strip()

        if city == 'London':
            return True
        else:
            print(False)

        # print item.text

def sendNotification():
    url = os.environ['WEBHOOK_URL']
    message = {'text' : 'There is a London event, sign up at https://codebar.io/events'}
    requests.post(url, json=message)


if getEvents() == True:
    sendNotification()
