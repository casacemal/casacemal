from __future__ import print_function
import BlynkLib
import time
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
from time import sleep
from json import dumps

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


BLYNK_AUTH = 'jlBPcVnvXNtdq0xiFENIOMYm6jkw8T9w'
GPIO.setup(12, GPIO.OUT)
#GPIO.output(12,GPIO.LOW)
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH,
                      # insecure=True,          # disable SSL/TLS
                       server='blynk.cloud',   # set server address
                       port=80,                # set server port 443 tls güvenli
                       heartbeat=30,           # set heartbeat to 30 secs
                       #log=print               # use print function for debug logging
                       )

@blynk.ON("connected")
def blynk_connected(ping):
    print( ping )
    print('Blynk connected')
@blynk.ON("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')
    connect_blynk()
@blynk.ON("V1")
def v1_write_handler(value):   
    print('        Current slider value: {}'.format(value[0]))
    v1_durum = int(value[0]) # str den int e çevirir
    print('                    vı durum slider value: ',v1_durum)
    if (v1_durum == 80):
      print("       v1 den okunan ",v1_durum)   
      print("     tmr_start_time den okunan ",tmr_start_time)
    elif(v1_durum ==5) :
       print("    /////// ok ",v1_durum)   
       print("      ////// okunan ",tmr_start_time)
    print("    v1 *********************** ",tmr_start_time)   
@blynk.ON("V5")
def v5_write_handler(value):   
    print('        Current slider value: {}'.format(value[0]))
    v5_durum = int(value[0]) # str den int e çevirir
    print('                    vı durum slider value: ',v5_durum)
    if (v5_durum == 1):     
      print("     t5555555555555555 ")
      publish.single("/lamp/salon/pow", dumps(""), hostname="192.168.1.14")
    elif(v5_durum == 0) :
       print("      ////// okunan ")
       print("    v5---*********************** ")
       
@blynk.ON("V8")
def v8_write_handler(value):   
    print('        Current slider value: {}'.format(value[0]))
    v8_durum = int(value[0]) # str den int e çevirir
    print('                    vı durum slider value: ',v8_durum)
    if (v8_durum == 1):     
      print("     t5555555555555555 ")
      publish.single("/lamp/yatak/pow", dumps(""), hostname="192.168.1.14")
@blynk.ON("V9")
def v9_write_handler(value):   
    print('        Current slider value: {}'.format(value[0]))
    v9_durum = int(value[0]) # str den int e çevirir
    print('                    v9 durum slider value: ',v9_durum)
    if (v9_durum == 1):     
      print("     999999 ")
      publish.single("/sistem/yatak/gecelamp", dumps(""), hostname="192.168.1.14")
@blynk.ON("V13")
def v13_write_handler(value):   
   # print('        Current slider value: {}'.format(value[0]))
    v13_durum = int(value[0]) # str den int e çevirir
    print('          v13 durum slider value: ',v13_durum)
    if (v13_durum == 1):     
      print("   kapı açıldı  13 ")
      publish.single("/zil/oto", dumps(""), hostname="192.168.1.14")

def blynk_handle_vpins(pin, value):
    print("      V{} deger: {}".format(pin, value))
    
def connect_blynk():
  try:
      print("blynk server a bağlanacak ")
      blynk = BlynkLib.Blynk(BLYNK_AUTH,
                      # insecure=True,          # disable SSL/TLS
                       server='blynk.cloud',   # set server address
                       port=80,                # set server port 443 tls güvenli
                       heartbeat=30,           # set heartbeat to 30 secs
                       log=print               # use print function for debug logging
                       )
      
  except Exception as e:
      print("bağlantı koptu yeniden bağlanıyor.")
      connect_blynk()
  #print("blynk server a bağlandı ")
  return blynk
tmr_start_time=0
a=0
while True:
  
      blynk.run()
      Input = GPIO.input(12)
    #print("12. pin okunan ",Input)
      t = time.time()
      if t - tmr_start_time > 5:
        #print("5 sec elapsed, sending data to the server...")
       # blynk.virtual_write(0,a )
        tmr_start_time = t
        a += 1        
        publish.single("temperature", dumps(a), hostname="192.168.1.14")
        



 
        
       

