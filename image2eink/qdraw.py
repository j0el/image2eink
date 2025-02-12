#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'image2eink/pic')
#libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'image2ink/lib')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '/home/jberman/e-Paper/RaspberryPi_JetsonNano/python/lib/')
sys.path.append(libdir)

from waveshare_epd import epd7in5bc
import time
from PIL import Image,ImageDraw,ImageFont
epd = epd7in5bc.EPD()
HBlackimage = Image.open(os.path.join(picdir, '7in5b-b.bmp'))
HRYimage = Image.open(os.path.join(picdir, '7in5b-r.bmp'))    
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
epd.init()
epd.Clear()
time.sleep(1)
epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
epd7in5bc.epdconfig.module_exit()
exit()
