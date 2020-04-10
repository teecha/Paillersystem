import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
# Clear display.
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = 0
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
# Load default font.
#font = ImageFont.load_default()
# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('nasalization-rg.ttf', 16)
#while True:
draw.rectangle((0,0,width,height), outline=0, fill=0)
draw.text((x, top + 8),      "Enter the Text",  font=font, fill=255)
disp.image(image)
disp.display()
time.sleep(.1)
subprocess.call("python3 input.py",shell = True)
draw.rectangle((0,0,width,height), outline=0, fill=0)
draw.text((x, top + 8),       "Text entered",  font=font, fill=255)
disp.image(image)
disp.display()
time.sleep(.1)
subprocess.call("python3 lol.py",shell = True)
draw.rectangle((0,0,width,height), outline=0, fill=0)
draw.text((x, top + 8),       "Encrypted",  font=font, fill=255)
disp.image(image)
disp.display()
time.sleep(.1)
