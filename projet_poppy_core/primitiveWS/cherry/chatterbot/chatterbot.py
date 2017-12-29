#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import httplib,urllib
import urllib2

def getResponseFromChatterbot(response):
	start = response.index("Bot :")
	end = 0
	start=start+5
	if "<NOREUT>" not in response:
		end = response.index("<form method")
	try:
		result = response[start:end]
	except Exception :
		result = 'Je ne comprends pas désolé'
	return result

def sendToChatterbot(msg):
	sauveInput=""
	var=""
	varTemp=""
	cerveau="AR.txt"
	vraiesvars=""
	nom=""
	noReut=""
	rappel=""

	
	print "chaine :"+msg
	with open("/home/poppy/resources/ip.txt", "U") as ip_file:
		ip = ip_file.readline().replace('\n', '')
	url="http://"+ip.split(':')[0]+":81/Genesis/chatterbot23.php"
	params={'vartemp':varTemp,'cerveau':cerveau,"vraiesvars":vraiesvars,"nom":nom,"noreut":noReut,"var":var,"usersay":msg,"sauveinput":sauveInput,"rappel":rappel}
	data = urllib.urlencode(params)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	html = response.read()
	test = getResponseFromChatterbot(html)
	return test



	
		









