#coding: utf-8
import os
import pyaudio
import time
from twisted.internet import reactor

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS

from threading import Timer

import json


class WebSocketClientProtocolSmartPoppy(WebSocketClientProtocol):

    def sendStart(self):
        print("Send start")
        start_message_content = {
            "action": "start",
            "type": "audio/l16;rate=16000",
            "result_audio_type": "audio/wav",
            "interim_results": True,
            "continuous": True
        }
        start_message = json.dumps(start_message_content)
        print(json.dumps(start_message_content))
        self.sendMessage(start_message, isBinary=False)
        self.Loop = True

    def sendStop(self):
        print("Send stop")
        start_message_content = {
            "action": "stop"
        }
        start_message = json.dumps(start_message_content)
        print(json.dumps(start_message_content))
        self.sendMessage(start_message, isBinary=False)

    def StopLoop(self):
    	self.Loop = False

    def conversation(self, taille_ko):
        self.sendStart()

        self.p = pyaudio.PyAudio()
        audioFd, writer = os.pipe()
        self.writer = writer
        self.in_stream = self.p.open(format=pyaudio.paInt16,
                             channels=1,
                             rate=16000,
                             input=True,
                             frames_per_buffer=1024*taille_ko)
        self.in_stream.start_stream()
        self.out_stream = self.p.open(format=self.p.get_format_from_width(2),
                        channels=1,
                        rate=22050,
                        output=True)
        self.out_stream.start_stream()

        print("Début de l'enregistrement")
        nb_morceaux = 0
        # while nb_morceaux < 10:
        while self.Loop is True:
            nb_morceaux=nb_morceaux+1
            print("Envoi morceau audio n° :"+str(nb_morceaux))
            self.sendMessage(self.in_stream.read(1024*taille_ko, False), isBinary=True)

        self.sendStop()
        self.in_stream.stop_stream()
        self.in_stream.close()
        self.out_stream.stop_stream()
        self.out_stream.close()
        self.p.terminate()
        print("Fin de l'enregistrement")

    """
    Émet le son d'un stream enregistré au format wav 
    """
    def play_binary_wav(self, binary_wav):
        self.out_stream.write(binary_wav, False)
        
    def onOpen(self):
        #Attend 3 secondes pour être sûr que le websocket client est bien initié
        t = Timer(3.0, self.conversation, args=(20,))
        t.start()

    def onMessage(self, payload, isBinary):
        if isBinary is True:
            print("Lecture du message reçu")
            self.play_binary_wav(payload)
        else:
            print(payload)

if __name__ == '__main__':
    factory = WebSocketClientFactory(u"ws://poppy.cloud-center.tech:80/ws")
     # factory = WebSocketClientFactory(u"ws://127.0.0.1:8080/ws")
    factory.protocol = WebSocketClientProtocolSmartPoppy
    connectWS(factory)
    reactor.run()
