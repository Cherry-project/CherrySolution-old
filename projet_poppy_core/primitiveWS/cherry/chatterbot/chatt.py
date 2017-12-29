#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import collections
import contextlib
import functools
import logging
import re
import signal
import sys
import time
import json
import base64
import os
import urllib2
import urllib
import string
import requests
import speech_recognition as sr
from chatterbot import sendToChatterbot
import copy
import pyaudio
import pypot
import threading

class Chatt(pypot.primitive.Primitive):

    def __init__(self, robot, state = 'normal' ):
        pypot.primitive.Primitive.__init__(self, robot)
        self._state = state
        self._robot = robot
          
    def start(self):
        print "Debut de la primitive chatterbot"
        pypot.primitive.Primitive.start(self)

    def run(self):
        with open("/home/poppy/resources/ip.txt", "U") as ip_file:
            ip = ip_file.readline().replace('\n', '')
    
        syn_parameters = {
            'text': '',
            'voice': 'fr-FR_ReneeVoice',
            'download': True,
            'accept': 'audio/wav'
        }    
    
        def synthesize(text):
            parameters = copy.copy(syn_parameters)
            cleanParameters = {}
            cleanParameters['text'] = text
            cleanParameters['accept'] = parameters['accept']
            cleanParameters['voice'] = parameters['voice']
            url= "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
            username = "22c36812-3396-41a1-afc7-b88209d04f36"
            password = "Z7TtzcqqbPWz"
            r = requests.get(url + '?' + urllib.urlencode(cleanParameters), auth=(username, password))
            return r.content
        def speak(text, ip):
            print "Text to Speak : " + text
            data = {'list': [text],
                    'id': 'sogeti'}
            url = "http://" + ip + "/app/speech"
            req = urllib2.Request(url, json.dumps(data))
            req.add_header('Content-Type', 'application/json')
            spoke = urllib2.urlopen(req)
            print "response :"
            print spoke.read()
        def threadMv(action):
            #print "Playing primitive with parameter : "+action
            if action == "chatterbot":
                time.sleep(16)
                urllib2.urlopen("http://"+ip+"/"+action)
    
        #p = pyaudio.PyAudio()
        #stream = p.open(format=p.get_format_from_width(2),channels=1,rate=22050,output=True)
        response = sendToChatterbot('lance la demo');
        if "&quot;" in response :
            response = response.replace("&quot;"," ")
        if "&apos;" in response :
            response = response.replace("&apos;"," ")
        #s = synthesize(response)
        
        print "got a response !"
        urllib2.urlopen("http://"+ip+"/behaveHello")
        print "Le robot parle : " + response
        #stream.write(s)
        speak(response, ip)
        print "got a response !"
        urllib2.urlopen("http://"+ip+"/chatterbotIdle")
        msg = ""
        continueChatt = True
        while(continueChatt):
            try:
                while(self._state == 'normal'):
                    r = sr.Recognizer()
                    r.dynamic_energy_threshold = True
                    r.pause_threshold = 0.5
                    with sr.Microphone() as source:
                        print("\nSay something ! If the robot does not understand, press control + c to type your keyword !")
                        audio = r.listen(source, phrase_time_limit=5)
                    try:
                        msg = r.recognize_google(audio,language='FR').encode("utf-8")  
                        
                    except sr.UnknownValueError:
                        print("Google n a pas compris l audio")
                    except sr.RequestError as e:
                        print("Pas de message reconnu par google")
        
                    if msg != "":
                        if "stop" in msg:
                            raise KeyboardInterrupt
                        response = sendToChatterbot(msg);
                        if "&quot;" in response :
                            response = response.replace("&quot;"," ")
                        if "&apos;" in response :
                            response = response.replace("&apos;"," ")
        
                        if len(response) > 1 :
                            print "The robot will say : \n"+response
                            # if len(response) > 250:
                            #     threadMvCW = threading.Thread(target=threadMv,args=("chatterbot",))
                            #     threadMvCW.start()
                            #p = synthesize(response)
                            urllib2.urlopen("http://"+ip+"/chatterbot")
                            #stream.write(p)
                            speak(response, ip)
                            urllib2.urlopen("http://"+ip+"/chatterbotRest")
                        print "message reçu : " + msg
                        if "chorégraphie" in msg:
                            print "Stop chatterbot"
                            continueChatt = False  
                            raise KeyboardInterrupt  
                        msg=""
                        response=""    
            except KeyboardInterrupt:
                break