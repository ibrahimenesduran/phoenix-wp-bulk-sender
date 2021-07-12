"""
Coded by Ibrahim Enes Duran
Started 12 July 2021 | Last Updated 12 July 2021

NOTICE! This program is coded for educational purposes.
If there is a data source violation, please contact the following communication channels.

ibrahimenesduran@hotmail.com
"""

import time
from termcolor import colored
import os
import re
import requests
import json

def logger(err, message):
    print('{} | {} | {}'.format(time.strftime('%d/%m/%Y %H:%M:%S', time.localtime()), colored('ERROR', 'red') if err else colored('INFO ', 'green') , message))



def senderEngine(Numbers, message, host, delay):
    statusJSON = {
        'Numbers': {
            'not send': Numbers,
            'sent': [],
            'not user in WP': []
        }
    }
    logger(0, 'Settings')
    logger(0, 'IP:PORT:     {}'.format(host))
    logger(0, 'Delay (sec): {}'.format(delay))
    logger(0, 'Numbers:     {}'.format(len(Numbers)))


    while(1):
        print('{} | {} | {}'.format(time.strftime('%d/%m/%Y %H:%M:%S', time.localtime()), colored('INPUT', 'yellow') , 'Do you want to start sending to message? [Y] Yes [N] No'))
        i = input()
        if (i == 'Y' or i == 'y'):
            break
        elif (i == 'N' or i == 'n'):
            return logger(0, 'Client is closing')

    if not (os.path.exists('./saves')):
        logger(1, './saves was not found by client.')
        logger(0, 'Client is creating ./saves folder...')
        os.mkdir('./saves')

    
    for number in Numbers:
        payload = {'Number': str(number) + '@c.us', 'Message': message }  
        response = requests.post('http://' + host + '/send', json=payload)
        
        if response.status_code == 404:
            return logger(1, 'IP:PORT connection error. Please check ip:port and try again')
        if response.status_code == 400:
            logger(1, 'Please check your server or IP:PORT!')
        elif (response.status_code == 200 and response.json() == False):
            statusJSON['Numbers']['not user in WP'].append(number)
            statusJSON['Numbers']['not send'].remove(number)
        else:
            statusJSON['Numbers']['sent'].append(number)
            statusJSON['Numbers']['not send'].remove(number)
            
        time.sleep(delay)

    print(statusJSON)



def main():
    logger(0, 'Client is starting...')
    logger(0, 'Client is checking variables folder...')

    if not (os.path.exists('./variables')):
        logger(1, './variables was not found by client.')
        logger(0, 'Client is creating ./variables folder...')
        os.mkdir('./variables')

    logger(0, 'Client is checking numbers.txt...')

    files = [f for f in os.listdir('./variables')]
    if not 'numbers.txt' in files:
        return logger(1, './variables/numbers.txt was not found. Please check the file.')

    temp = open('./variables/numbers.txt', 'r').read().split('\n')
    temp_size = len(temp)
    logger(0, 'Client loaded {} numbers.'.format(temp_size))
    Numbers = []
    logger(0, 'Client is checking numbers which is valid...')

    for i in temp:
        if (re.match('905[0,3,4,5,6][0-9]{8}', i) and len(i) == 12):
            Numbers.append(i)
        elif (re.match('05[0,3,4,5,6][0-9]{8}', i) and len(i) == 11):
            Numbers.append('9' + i)
        elif (re.match('5[0,3,4,5,6][0-9]{8}', i) and len(i) == 10):
            Numbers.append('90' + i)     

    logger(0, '{} numbers is valid. {} numbers is not valid.'.format(len(Numbers), temp_size - len(Numbers)))
    temp_size = len(Numbers)

    logger(0, 'Client is checking duplicate numbers...')
    Numbers = list(set(Numbers))
    logger(0, 'Remove {} numbers is duplicate. Last size: {}'.format(temp_size- len(Numbers), len(Numbers)))

    logger(0, 'Client is ready for send message.')
    print('{} | {} | {}'.format(time.strftime('%d/%m/%Y %H:%M:%S', time.localtime()), colored('INPUT', 'yellow') , 'Please enter the message:'))
    
    message = input()

    if len(message) > 15000:
        return logger(1, 'Please check your message! Too long.')

    if len(message) < 10:
        return logger(1, 'Please check your message! Too short.')

    logger(0, 'Message is ready:\n{}'.format(message))

    while 1:
        print('{} | {} | {}'.format(time.strftime('%d/%m/%Y %H:%M:%S', time.localtime()), colored('INPUT', 'yellow') , 'Message will send to {} numbers. Do you want to send message to numbers? [Y] Yes [N] No'.format(len(Numbers))))
        i = input()
        if (i == 'Y' or i == 'y'):
            break
        elif (i == 'N' or i == 'n'):
            return logger(0, 'Client is closing')

    print('{} | {} | {}'.format(time.strftime('%d/%m/%Y %H:%M:%S', time.localtime()), colored('INPUT', 'yellow') , 'Please enter the IP:PORT: '))
    host = input()

    while 1:
        print('{} | {} | {}'.format(time.strftime('%d/%m/%Y %H:%M:%S', time.localtime()), colored('INPUT', 'yellow') , 'Please enter the message delay (seconds): '))
        try:
            delay = int(input())
            break
        except:
            continue

    senderEngine(Numbers, message, host, delay)



main()

