#!/usr/bin/python3
 
from i2clibraries import i2c_lcd
from time import * 
import urllib.request
import json

def printPageLiked():
 url = 'https://graph.facebook.com/raspberrypi66?fields=likes'
 try:
  fbResult= json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
  writeBigNumber(fbResult['likes'])
 except:
  print("can't connect to server")

def writeBigNumber(number):
 number=str(number).zfill(5)
 digitCount=len(number)
 for i in range(0,digitCount):
  x=int(number[i:i+1])
  writeBigDigit(x,i)

def writeBigDigit(number=0,digit=0):
 bn14=[1,2,3,0,       2,3,254,0,     1,2,3,0,       1,2,3,0,       2,254,254,0,   2,2,2,0,       1,2,3,0,       2,2,2,0,       1,2,3,0,       1,2,3,0]
 bn24=[255,254,255,0, 254,255,254,0, 1,2,255,0,     254,2,255,0,   255,2,2,0,     255,2,2,0,     255,2,3,0,     254,2,255,0,   255,2,255,0,   255,254,255,0]
 bn34=[255,254,255,0, 254,255,254,0, 255,254,254,0, 254,254,255,0, 254,255,254,0, 254,254,255,0, 255,254,255,0, 254,255,254,0, 255,254,255,0, 4,6,255,0]
 bn44=[4,6,5,0,       6,6,6,0,       4,6,6,0,       4,6,5,0,       254,6,254,0,   6,6,5,0,       4,6,5,0,       254,6,254,0,   4,6,5,0,       254,254,6,0]

 lcd._write(0x80+digit*4)
 lcd.writeCustom(bn14[number*4])
 lcd.writeCustom(bn14[number*4+1])
 lcd.writeCustom(bn14[number*4+2])

 lcd._write(0xC0+digit*4)
 lcd.writeCustom(bn24[number*4])
 lcd.writeCustom(bn24[number*4+1])
 lcd.writeCustom(bn24[number*4+2])

 lcd._write(0x94+digit*4)
 lcd.writeCustom(bn34[number*4])
 lcd.writeCustom(bn34[number*4+1])
 lcd.writeCustom(bn34[number*4+2])

 lcd._write(0xD4+digit*4)
 lcd.writeCustom(bn44[number*4])
 lcd.writeCustom(bn44[number*4+1])
 lcd.writeCustom(bn44[number*4+2])


lcd = i2c_lcd.i2c_lcd(0x20,1, 2, 1, 0, 4, 5, 6, 7, 3)

lcd.customChar(1,[0,0,0,0,3,15,15,31])
lcd.customChar(2,[0,0,0,0,31,31,31,31])
lcd.customChar(3,[0,0,0,0,24,30,30,31])
lcd.customChar(4,[31,15,15,3,0,0,0,0])
lcd.customChar(5,[31,30,30,24,0,0,0,0])
lcd.customChar(6,[31,31,31,31,0,0,0,0])

lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)
lcd.clear()
lcd.backLightOn()

while(1):
 try:
  printPageLiked()
  sleep(10)
 except:
  lcd.clear()
  lcd.backLightOff()
  exit()




