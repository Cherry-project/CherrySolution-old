# coding: utf-8
import pyaudio
from twisted.internet import interfaces, reactor
from zope.interface import implementer

# 2^63 - Maximum imposé par le protocole WebSocket
MAX_FRAME_SIZE = 0x7FFFFFFFFFFFFFFF
CHUNK_SIZE = 1024 * 20
SHORT_BINARY_SILENCE = chr(0) * 100


@implementer(interfaces.IPushProducer)
class MicrophoneProducer:
    """
    Implémentation du pattern Producer-Consumer de Twisted, permettant d'envoyer en streaming le son du microphone.
    Les morceaux sont envoyés au WebSocket via des MessageFrames.
    """

    def __init__(self, proto):
        self.proto = proto
        self.started = False
        self.paused = False
        self._pyaudio = pyaudio.PyAudio()
        self._microphone_stream = self._pyaudio.open(format=pyaudio.paInt16,
                                                     channels=1,
                                                     rate=16000,
                                                     frames_per_buffer=CHUNK_SIZE,
                                                     input=True,
                                                     start=False,
                                                     stream_callback=self.stream_callback_send_chunk)

    def stream_callback_send_chunk(self, in_data, frame_count, time_info, status):
        '''
        Callback appelé par PyAudio dès qu'un nouveau morceau a été enregistré.
        Cette fonction récupère le morceau et l'envoie au serveur.
        '''
        if not self.proto._output_stream.is_active():
            print("envoi audio")
            self.proto.sendMessageFrame(in_data)
        else:
            print("pas envoyé car lecture")
        return (in_data, pyaudio.paContinue)

    def pauseProducing(self):
        self.paused = True
        self._microphone_stream.stop_stream()
        # Envoi d'un silence avant le message de fin, sinon il peut y avoir une erreur lorsqu'aucune donnée n'est envoyée entre le message de début et de fin
        self.proto.sendMessageFrame(SHORT_BINARY_SILENCE)
        self.proto.endMessage()

    def resumeProducing(self):
        print("resumeProducing : output active ? "+str(self.proto._output_stream.is_active()))
        while self.proto._output_stream.is_active():
            print("is active")
        else:
            print("inactive")
            self.proto.beginMessage(isBinary=True)
            self.paused = False
            self._microphone_stream.start_stream()

    def stopProducing(self):
        self._microphone_stream.stop_stream()
        self.started = False
