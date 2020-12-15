Connections:
Pin 2- 5v - Relay
Pin 4 -5v - Soil Moisture Sensor Amplifier
Pin 6- GND - Relay D0
Pin 9- GND - Soil Moisture Sensor Amplifier
Pin 38 - GPIO 20- IN -Relay A0
Pin 40 - GPIO 21-OUT - Soil Moisture Sensor Amplifier

Source Code:
import urllib2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.IN)
dryFlag==0
wetFlag==0
while True:
  if(GPIO.input(20)==1 and noWaterFlag==0)
    print 'Dry soil' wetFlag==0
    dryFlag==1
    urlopen('https://maker.ifttt.com/trigger/moisture/key/e299M3hPVEBQYpHITTlh7iDDR-_c_ngIO298-mMpCE')
    print 'Notification sent' elif(GPIO.input(20)==0 and waterFlag==0)
    wetFlag==1
    dryFlag==0
    print 'Wet Soil'
    urlopen('https://maker.ifttt.com/trigger/moisture/key/e299M3hPVEBQYpHITTl8h7iDDR-_c_ngIO298-mMpCE')
    print 'Notification sent' //for turning the motor ON and OFF,connect to IFTTT webhooks and ORL Launchpadkeys
    if(urlopen('http://orlindustries.com/olp/device_pull?device_api_key=fa4cf85da7897643dd54704884687bf0').read().split(': ')[3].split('<')[0])=='Motor on':
      GPIO.output(21,GPIO.HIGH)
      print 'Motor on'

      //setting up the connections

      //initializing the values

      //if there is no water then dry soil detected

      //if there is water then wet soil detected

      elif(urlopen('http://orlindustries.com/olp/device_pull?device_api_key=fa4cf85da7897643dd54704884687bf0').read().split(': ')[3].split('<')[0])=='Motor on':
      GPIO.output(21,GPIO.LOW)
      print 'Motor off ' 
      sleep(1)
