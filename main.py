#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import adbutils
import os
from utils.utils import *
from modules.media import *
from modules.system import *

DUMP_PATH = "dump"
DUMP_PATH = os.path.join(os.getcwd(), DUMP_PATH)

DUMP_SCREENSHOT = "screenshot"
DUMP_SCREENSHOT = os.path.join(DUMP_PATH, DUMP_SCREENSHOT)

DUMP_SCREENRECORD = "screenrecord"
DUMP_SCREENRECORD = os.path.join(DUMP_PATH, DUMP_SCREENRECORD)


def setup():
    if not os.path.exists(DUMP_PATH):
        os.mkdir(DUMP_PATH)
    if not os.path.exists(DUMP_SCREENSHOT):
        os.mkdir(DUMP_SCREENSHOT)
    if not os.path.exists(DUMP_SCREENRECORD):
        os.mkdir(DUMP_SCREENRECORD)

def main():
    try:        
        devices = get_devices()
        if devices == []:
            raise Exception("No devices connected")
        media = Media(devices[0].serial)
        # printInfo(media.screenshot(DUMP_SCREENSHOT))
        # printInfo(media.screenrecord(DUMP_SCREENRECORD))
        system(devices[0].serial)
        
    except Exception as e:
        printError(e)

if __name__ == "__main__":
    setup()
    main()
