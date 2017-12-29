# coding: utf-8
import json

import pyaudio
import txaio
from autobahn.twisted import WebSocketClientProtocol, WebSocketClientFactory
from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor

from MicrophoneProducer import MicrophoneProducer


class PoppyClientProtocol(WebSocketClientProtocol):
    """
    Implémentation d'un protocole de websocket client, permettant de mener une conversation avec Smart-Poppy. 
    Enregistre le son du microphone et l'envoie en streaming au serveur, puis joue les réponses audio du serveur (en 
    coupant le microphone pour éviter que l'API ne se parle toute seule). 
    """

    def __init__(self):
        super(PoppyClientProtocol, self).__init__()
        self.producer = MicrophoneProducer(self)
        self._pyaudio = pyaudio.PyAudio()
        self._output_stream = self._pyaudio.open(format=self._pyaudio.get_format_from_width(2),
                                                 channels=1,
                                                 rate=22050,
                                                 output=True,
                                                 start=False)

    def send_start(self):
        start_message_content = {
            "action": "start",
            "audio_type_input": "audio/l16;rate=16000",
            "audio_type_output": "audio/wav",
            "inactivity_timeout": -1
        }
        start_message = json.dumps(start_message_content)
        self.sendMessage(start_message.encode("utf-8"), isBinary=False)

    def play_binary_wav(self, binary_wav):
        print("Lecture du message reçu")
        self._output_stream.start_stream()
        self._output_stream.write(binary_wav)
        self._output_stream.stop_stream()
        print("Fin de la lecture")
        # reactor.callLater(0.2, self.producer.resumeProducing)

    def onOpen(self):
        self.send_start()
        print("start sent")
        self.registerProducer(self.producer, True)
        reactor.callFromThread(self.producer.resumeProducing)

    # def onMessageBegin(self, isBinary):
    #     if isBinary is True:
    #         self.producer.pauseProducing()


    def onMessage(self, payload, isBinary):
        print("MESSAGE RECU")
        if isBinary is True:
            self.play_binary_wav(payload)
        else:
            print(payload)
            json_payload = json.loads(payload)
            if "record" in json_payload:
                if json_payload["record"] == "stop":
                    self.producer.pauseProducing()
                elif json_payload["record"] == "start":
                    self.producer.resumeProducing()


    def onClose(self, wasClean, code, reason):
        print("Fermeture : " + str(code))
        print("Raison de la fermeture : " + reason)
        self.producer.stopProducing()


if __name__ == '__main__':
    txaio.start_logging(level='debug')
    factory = WebSocketClientFactory(u"ws://poppy.cloud-center.tech:80/ws")
    # factory = WebSocketClientFactory(u"ws://127.0.0.1:8080/ws")
    factory.protocol = PoppyClientProtocol
    connectWS(factory)
    reactor.run()
