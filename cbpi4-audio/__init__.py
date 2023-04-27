import asyncio
import re
import logging

from playsound import playsound

from cbpi.api import *
from cbpi.api.config import ConfigType
from cbpi.api.base import CBPiBase

logger = logging.getLogger(__name__)

settings = [
    {
        "id": "hop",
        "default_file": "/home/dietpi/audio/hop.wav",
        "default_regex": "/Hop Alert/",
        "label": "Hop should be added.",
    },
    {
        "id": "target",
        "default_file": "/home/dietpi/audio/target.wav",
        "default_regex": "/Target Temp reached/",
        "label": "Target temp. is reached."
    },
    {
        "id": "nextstep",
        "default_file": "/home/dietpi/audio/nextstep.wav",
        "default_regex": "/Step finished/",
        "label": "Going to next step."
    },
    {
        "id": "cool",
        "default_file": "/home/dietpi/audio/cool.wav",
        "default_regex": "/Boiling completed/",
        "label": "Boil is over."
    },
]

class Audio():
    def __init__(self,cbpi):
        self.task = asyncio.create_task(self.run())
        self.cbpi = cbpi

    def config(self, key, fallback):
        return self.cbpi.config.get(key, fallback)

    async def run(self):
        for s in settings:
            await self.cbpi.config.add(f"audio_file_{s['id']}", s['default_file'], ConfigType.STRING, f"Audio File: {s['label']}")
            await self.cbpi.config.add(f"audio_regex_{s['id']}", s['default_regex'], ConfigType.STRING, f"Audio Regex: {s['label']}")
        self.cbpi.notification.add_listener(self.cbpiNotificationEvent)

    async def cbpiNotificationEvent(self, cbpi, title, message, type, action):
        for s in settings:
            regex = self.config(f"audio_regex_{s['id']}", "//")
            m1 = re.match(regex, title)
            m2 = re.match(regex, message)

            if m1 or m2:
                file = self.config(f"audio_file_{s['id']}", False)
                if file:
                    await playsound(file)

def setup(cbpi):
    cbpi.plugin.register("Audio", Audio)