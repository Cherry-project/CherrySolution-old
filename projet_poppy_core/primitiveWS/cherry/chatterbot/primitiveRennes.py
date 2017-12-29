#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import pyaudio
import time

from twisted.internet import reactor

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS

from threading import Timer

from testRennes import WebSocketClientProtocolSmartPoppy
import json
import pypot.primitive

class testRennes(pypot.primitive.Primitive):
    
    properties = pypot.primitive.Primitive.properties + ['listen_state']

    def __init__(self, robot, state = 'normal'):
        pypot.primitive.Primitive.__init__(self, robot)
        self._state = state
        self._robot = robot

          
    def start(self):
        pypot.primitive.Primitive.start(self)

    def run(self):
        factory = WebSocketClientFactory(u"ws://poppy.cloud-center.tech:80/ws")
        # factory = WebSocketClientFactory(u"ws://127.0.0.1:8080/ws")
        factory.protocol = WebSocketClientProtocolSmartPoppy
        connectWS(factory)
        reactor.run()

    @property
    def listen_state(self):
        return self._state

    @listen_state.setter
    def listen_state(self, state):
        print("Set parameter to: " + state)
        self._state= state
