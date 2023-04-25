
from ast import Num
from calendar import c
from cgitb import text
from unittest import result
from urllib import request
import speech_recognition as sr
from selenium import webdriver
import pyttsx3 as p
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from django.shortcuts import render, redirect
from gtts import gTTS
import os
from playsound import playsound
from django.http import HttpResponse
import speech_recognition as sr
from django.http import JsonResponse
import re
from pynput.keyboard import Key, Controller

file = "good"
i="0"




def texttospeech(text, filename):
    filename = filename + '.mp3'
    flag = True
    while flag:
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(filename)
            flag = False
        except:
            print('Trying again')
    playsound(filename)
    os.remove(filename)
    return

def speechtotext(duration):
    global i, addr, passwrd
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        # texttospeech("speak", file + i)
        # i = i + str(1)
        playsound('speak.mp3')
        audio = r.listen(source, phrase_time_limit=duration)
    try:
        response = r.recognize_google(audio)
    except:
        response = 'N'
    return response

def convert_special_char(text):
    temp=text
    special_chars = ['dot','underscore','dollar','hash','star','plus','minus','space','dash']
    for character in special_chars:
        while(True):
            pos=temp.find(character)
            if pos == -1:
                break
            else :
                if character == 'dot':
                    temp=temp.replace('dot','.')
                elif character == 'underscore':
                    temp=temp.replace('underscore','_')
                elif character == 'dollar':
                    temp=temp.replace('dollar','$')
                elif character == 'hash':
                    temp=temp.replace('hash','#')
                elif character == 'star':
                    temp=temp.replace('star','*')
                elif character == 'plus':
                    temp=temp.replace('plus','+')
                elif character == 'minus':
                    temp=temp.replace('minus','-')
                elif character == 'space':
                    temp = temp.replace('space', '')
                elif character == 'dash':
                    temp=temp.replace('dash','-')
    return temp




def menu_view(request):
    global i, addr, passwrd , anss
    if request.method == 'POST':
        flag = True
        texttospeech("You are in the menu page. What would you like to do ?", file + i)
        i = i + str(1)
        while(flag):
            texttospeech(" To check maps say maps. To book taxi say taxi .Do you want me to repeat?", file + i)
            i = i + str(1)
            say = speechtotext(3)
            if say == 'No' or say == 'no':
                flag = False
        texttospeech("Enter your desired action", file + i)
        i = i + str(1)
        act = speechtotext(10)
        act = act.lower()
        if act == 'direction':
            return JsonResponse({'result' : 'map'})
        elif act == 'taxi' :
            return JsonResponse({'result' : 'taxi'})
        else:
            texttospeech("Invalid action. Please try again.", file + i)
            i = i + str(1)
            return JsonResponse({'result': 'failure'})
    elif request.method == 'GET':
        return render(request, 'homepage/menu.html')



def search_view(request):
    global i,  ans ,spot, info, info1,info2,info3,info4
    if request.method == 'POST':
        flag = True
        text1 = "Welcome to our search section."
        texttospeech(text1, file + i)
        i = i + str(1)    
        
        while (flag):
            texttospeech("name the place you wanna search.", file + i)
            i = i + str(1)
            spot = speechtotext(10)
            if spot != 'N':
                texttospeech("You meant " + spot + " say yes to confirm or no to enter again", file + i)
                i = i + str(1)
                say = speechtotext(3)
                if say == 'yes' or say == 'Yes':
                    flag = False
            else:
                texttospeech("could not understand what you meant:", file + i)
                i = i + str(1) 
        spot = spot.lower()
        spot = convert_special_char(spot)   

        flag = True
        while (flag): 
            driver = webdriver.Chrome(executable_path=r"C:\\Users\\Manikandan\\Downloads\\chromedriver_win32\\chromedriver.exe")
            driver.get(url="https://www.google.com/maps")
            search = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
            search.click()
            search.send_keys(spot)
            search = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
            search.click()
            info = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[5]')
            #info.click()
            texttospeech(info)
            info1 = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[7]')
            texttospeech(info1)
            info2 = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[9]')
            texttospeech(info2)
            info3 = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[11]')
            texttospeech(info3)
            info4 = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[13]')
            texttospeech(info4)
    elif request.method == 'GET':
        return render(request, 'homepage/search.html') 

def direction_view(request):
    global i,  ans ,spot, info, info1,info2,info3,info4
    if request.method == 'POST':
        text1 = "Welcome to our direction section. "
        texttospeech(text1, file + i)
        i = i + str(1)    
        flag = True
        while (flag):
            texttospeech("Enter the place.", file + i)
            i = i + str(1)
            spot = speechtotext(10)
            if spot != 'N':
                texttospeech("You meant " + spot + " say yes to confirm or no to enter again", file + i)
                i = i + str(1)
                say = speechtotext(3)
                if say == 'yes' or say == 'Yes':
                    flag = False
            else:
                texttospeech("could not understand what you meant:", file + i)
                i = i + str(1) 
        spot = spot.lower()
        spot = convert_special_char(spot)   



def taxi_view(request):
    global i,daddr,ssearch,esearch,fsearch
    if request.method == 'POST':
        flag = True
        text1 = "Welcome to our taxi section."
        texttospeech(text1, file + i)
        i = i + str(1)    
        
        while (flag):
            texttospeech("name the destination place.", file + i)
            i = i + str(1)
            daddr = speechtotext(10)
            if daddr != 'N':
                texttospeech("You meant " + daddr + " say yes to confirm or no to enter again", file + i)
                i = i + str(1)
                say = speechtotext(3)
                if say == 'yes' or say == 'Yes':
                    flag = False
            else:
                texttospeech("could not understand what you meant:", file + i)
                i = i + str(1) 
        daddr = daddr.lower()
        daddr = convert_special_char(daddr)   

        flag = True
        while (flag): 
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 1}
            chrome_options.add_experimental_option("prefs",prefs)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(executable_path=r"C:\\Users\\Manikandan\\Downloads\\chromedriver_win32\\chromedriver.exe", options=chrome_options)
            driver.get(url="https://book.olacabs.com/?pickup_name=20%2F20%2C%20Royapettah%2C%20Chennai&lat=13.0547712&lng=80.2717696&pickup=")
            driver.maximize_window()
            #driver.get(url="https://book.olacabs.com/")
            #driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('ola-loc-permission').shadowRoot.querySelector('div').querySelector('.confirm-btn').click()")
            #driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('ola-notification').shadowRoot.querySelector('div').querySelector('.confirm-btn').click()")
            time.sleep(4)
            try:
                driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('header').querySelector('span#login').click()")
            except Exception:
                pass

            while (flag):
                texttospeech("enter your mobile number.", file + i)
                i = i + str(1)
                Num = speechtotext(11)
                if Num != 'N':
                    texttospeech("You meant " + Num + " say yes to confirm or no to enter again", file + i)
                    i = i + str(1)
                    say = speechtotext(3)
                    if say == 'yes' or say == 'Yes':
                        flag = False
                else:
                    texttospeech("could not understand what you meant:", file + i)
                    i = i + str(1) 
            Num = Num.lower()
            Num = convert_special_char(Num)   
            Num=str(Num)
            keyboard = Controller()
            time.sleep(3)
            keyboard.type(Num)
            time.sleep(3)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            
            
            #ssearch = driver.find_element(By.XPATH, '//*[@id="phone-number"]')
            #ssearch.click() 
            ## otp
            otpFLag=True 
            while (otpFLag):
                texttospeech("speak your one time password .", file + i)
                i = i + str(1)
                otp = speechtotext(11) 
                if otp != 'N':
                    texttospeech("You meant " + otp + " say yes to confirm one time password or no to enter again", file + i)
                    i = i + str(1)
                    say = speechtotext(3)
                    if say == 'yes' or say == 'Yes':
                        otpFLag = False
                else:
                    texttospeech("could not understand what you meant:", file + i)
                    i = i + str(1)
            otp = otp.lower()
            otp = convert_special_char(otp)   
            otp=str(otp)
            keyboard = Controller()
            time.sleep(3)
            keyboard.type(otp)
            time.sleep(3)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
             #
            
            time.sleep(3)
            driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('iron-pages').querySelector('ola-home').shadowRoot.querySelector('ola-location-input').shadowRoot.querySelector('div.right.h-full.text.value').click()")
            time.sleep(3)
            driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('ola-modal').shadowRoot.querySelector('ola-location').shadowRoot.querySelector('div.locations-container').querySelector('div.results-row > div > div > div.middle.text.value').click()")
            time.sleep(3)
            driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('ola-home').shadowRoot.querySelector('div.page-container.bg-light').querySelector('ola-home-local').shadowRoot.querySelector('ola-location-input').shadowRoot.querySelector('div.card.bg-dark.no-border').querySelector('div.right.h-full.text.placeholder').click()")
            time.sleep(2)
            #inputadress="document.querySelector('ola-app').shadowRoot.querySelector('ola-modal').shadowRoot.querySelector('ola-location').shadowRoot.querySelector('div.locations-container').querySelector('#addressInput').value="+myadress
            #daddr =  'Marina beach'
            keyboard.type(daddr)
            time.sleep(3)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(3)
            driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('ola-modal').shadowRoot.querySelector('ola-location').shadowRoot.querySelector('div.locations-container').querySelector('div.results-row > div > div:nth-child(1)>div.middle.text').click()")

            autoprice = driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('ola-home').shadowRoot.querySelector('div.page-container.bg-light').querySelector('ola-home-local').shadowRoot.querySelector('div.cabs-list-section>ola-cabs').shadowRoot.querySelector('div.card.car-cont.bg-white.when-NOW').querySelector('div:nth-child(1) > div.middle > div.text.value.cab-name > span > span:nth-child(1)').innerText")

            print(autoprice)

            

            texttospeech("auto price", file + i)
            i = i + str(1)
            texttospeech(autoprice, file + i)
            i = i + str(1)
            if spot != 'N':
                texttospeech(" say yes to confirm or no to cancel", file + i)
                i = i + str(1)
                gsearch = speechtotext(3)
                if gsearch == 'yes' or gsearch == 'Yes':
                    flag = False
            driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('ola-home').shadowRoot.querySelector('div.page-container.bg-light').querySelector('ola-home-local').shadowRoot.querySelector('div.cabs-list-section>ola-cabs').shadowRoot.querySelector('div.card.car-cont.bg-white.when-NOW').querySelector('div:nth-child(1) > div.middle > div.text.value.cab-name').click()")
            time.sleep(3)
            driver.execute_script("document.querySelector('ola-app').shadowRoot.querySelector('ola-modal').shadowRoot.querySelector('ola-confirm-ride-p2p').shadowRoot.querySelector('div.footer > button').click()")
            #hsearch = driver.find_element(By.XPATH, '/html/body/ola-app//iron-pages/ola-home//div[2]/ola-home-local//div/ola-cabs//div[2]/div[1]/div[2]')
            #hsearch.click()                                         

    elif request.method == 'GET':
        return render(request, 'homepage/taxi.html') 

