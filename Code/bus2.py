import microgear.client as microgear
import logging
import time

appid = 'busServer'
gearkey = 'rR1N71fN0gbNSWK'
gearsecret =  'NrC6z97xpmSIcOBeGMns77CN3'

name = 'client02' #ชื่อของเจ้าตัวนี้
topic = '/infobus' #ชื่อ topic
sendto = 'server' #อันนี้ส่งไปยังตัวทดสอบนะครับ เป็นชื่ออีกไฟล์

microgear.create(gearkey,gearsecret,appid,{'debugmode': False})

def connection():
     logging.info("----CONNECTED----")

def subscription(topic,message):
    logging.info('GET: '+message[2:-1]) #ได้ข้อความจาก Server จากที่ส่งไป
    
def disconnect():
    logging.info("----DISCONNECTED----")

microgear.setalias(name)
microgear.on_connect = connection
microgear.on_message = subscription 
microgear.on_disconnect = disconnect
microgear.subscribe(topic)
microgear.connect(False)
while True:
    send = input(name+': ')
    if send == 'Q':
        logging.info('--ENDING--')
        break
    if send == 'info':
        microgear.chat(sendto,send+','+'0'+','+name) #ส่งเป็น string เช่น 'info,0,client01'
        logging.info("SENT: "+send+','+'0'+','+name+" | TO: " +sendto) #โชว์ข้อความว่าส่งอะไรไปที่ไหน
        continue
    try:
        temp = send.split(',')
        microgear.chat(sendto,temp[0]+','+temp[1]+','+name) #ส่งเป็น string เช่น 'A,8,client01' 
        logging.info("SENT: "+temp[0]+','+temp[1]+','+name+" | TO: " +sendto) #โชว์ข้อความว่าส่งอะไรไปที่ไหน
    except:
        print('INPUT: Q | info | bus,people') #ขึ้นกรณีใส่ไม่ถูก
        continue