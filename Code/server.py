import microgear.client as microgear
import logging
import base64, zlib, time
import random

appid = 'busServer'
gearkey = 'DsMOLmhGJapI424'
gearsecret =  'ztqEYJLGTExoPwsLtkeQf3O93'
name = 'server' #ชื่อตรงนี้เอาไปใส่ ใน sendto ของแต่ละ client แล้วแต่ละ client จะส่งข้อความมาที่ตัวนี้
topic = '/infobus' #ชื่อ topic

microgear.create(gearkey,gearsecret,appid,{'debugmode': False})

tempA1 = 0
tempA2 = 0
tempA3 = 0
tempB1 = 0
tempB2 = 0
tempB3 = 0

def connection():
     logging.info("----CONNECTED----")

def subscription(topic,message):
    logging.info('GET: '+ message) #โชว์ว่าได้รับข้อความอะไรมา
    global tempA1
    global tempA2
    global tempA3
    global tempB1
    global tempB2
    global tempB3

    temp = message.split(',')

    if temp[0] == "b'info":
        textSentA = "BusA distance = "+str(BusA)+","+"count = "+str(BusAS)
        textSentB = "BusB distance = "+str(BusB)+","+"count = "+str(BusBS)
        #microgear.chat(temp[2],textSentA)
        #microgear.chat(temp[2][:-1],textSentA)
        #microgear.chat(temp[2],textSentB)
        microgear.chat(temp[2][:-1],textSentA+","+textSentB)

    if temp[0] == "b'A":
        microgear.chat(temp[2][:-1],'BUS '+temp[0][2:]+' WITH '+temp[1]+' PEOPLES.')
        if temp[2][:-1] == "client01":
            if BusA > 20:
                eta = (120 - BusA) / 2
            else:
                eta = (20 - BusA) / 2
            microgear.chat(temp[2][:-1],'Arrive in : ' + str(eta) + ' sec')
        elif temp[2][:-1] == "client02":
            if BusA > 50:
                eta = (150 - BusA) / 2
            else:
                eta = (50 - BusA) / 2
            microgear.chat(temp[2][:-1],'Arrive in : ' + str(eta) + ' sec')
        elif temp[2][:-1] == "client03":
            if BusA > 70:
                eta = (170 - BusA) / 2
            else:
                eta = (70 - BusA) / 2
            microgear.chat(temp[2][:-1],'Arrive in : ' + str(eta) + ' sec')
    if temp[0] == "b'B":
        microgear.chat(temp[2][:-1],'BUS '+temp[0][2:]+' WITH '+temp[1]+' PEOPLES.')
        if temp[2][:-1] == "client01":
            if BusB > 20:
                eta = (120 - BusB) / 5
            else:
                eta = (20 - BusB) / 5
            microgear.chat(temp[2][:-1],'Arrive in : ' + str(eta) + ' sec')
        elif temp[2][:-1] == "client02":
            if BusB > 50:
                eta = (150 - BusB) / 5
            else:
                eta = (50 - BusB) / 5
            microgear.chat(temp[2][:-1],'Arrive in : ' + str(eta) + ' sec')
        elif temp[2][:-1] == "client03":
            if BusB > 70:
                eta = (170 - BusB) / 5
            else:
                eta = (70 - BusB) / 5
            microgear.chat(temp[2][:-1],'Arrive in : ' + str(eta) + ' sec')
        

    if temp[2][:-1] == "client01":
        if temp[0][2:] == 'A':
            tempA1 += int(temp[1])
        elif temp[0][2:] == 'B':
            tempB1 += int(temp[1])
    elif temp[2][:-1] == "client02":
        if temp[0][2:] == 'A':
            tempA2 += int(temp[1])
        elif temp[0][2:] == 'B':
            tempB2 += int(temp[1])
    elif temp[2][:-1] == "client03":
        if temp[0][2:] == 'A':
            tempA3 += int(temp[1])
        elif temp[0][2:] == 'B':
            tempB3 += int(temp[1])

def disconnect():
    print("----DISCONNECTED----")

microgear.setalias(name)
microgear.on_connect = connection
microgear.on_message = subscription
microgear.on_disconnect = disconnect
microgear.subscribe(topic)
microgear.connect()

BusA = 0
BusB = 0
BusAS = 0
BusBS = 0

x = 0

while True:
    #random number + send to "bus server" topic
	#T1 = random.randint(0,100)		
	#H1 = random.randint(0,100)
	time.sleep(1)
  
	BusA += 2
	if BusA >= 100:
		BusA -= 100
  
	BusB += 5
	if BusB >= 100:
		BusB -= 100
  

	if BusA == 20:
		
		BusAS += tempA1
		if BusAS >= 20:
			tempA1 = BusAS - 20
			BusAS = 20
			microgear.chat("client01","Seat capacity exceed the limit on BusA by " + str(tempA1))
			
		else:
			tempA1 = 0
	if BusA == 50:
		
		BusAS += tempA2
		if BusAS >= 20:
			tempA2 = BusAS - 20
			BusAS = 20
			microgear.chat("client02","Seat capacity exceed the limit on BusA by " + str(tempA2))
		else:
			tempA2 = 0
	if BusA == 70:
		
		BusAS += tempA3
		if BusAS >= 20:
			tempA3 = BusAS - 20
			BusAS = 20
			microgear.chat("client03","Seat capacity exceed the limit on BusA by " + str(tempA3))
		else:
			tempA3 = 0
		
	if BusB == 20:
		
		BusBS += tempB1
		if BusBS >= 40:
			tempB1 = BusBS - 40
			BusBS = 40
			microgear.chat("client01","Seat capacity exceed the limit on BusB by " + str(tempB1))
			
		else:
			tempB1 = 0
	if BusB == 50:
		
		BusBS += tempB2
		if BusBS >= 40:
			tempB2 = BusBS - 40
			BusBS = 40
			microgear.chat("client02","Seat capacity exceed the limit on BusB by " + str(tempB2))
		else:
			tempB2 = 0
	if BusA == 70:
		
		BusBS += tempB3
		if BusBS >= 40:
			tempB3 = BusBS - 40
			BusBS = 40
			microgear.chat("client03","Seat capacity exceed the limit on BusB by " + str(tempB3))
		else:
			tempB3 = 0
	if x % 10 == 0 and x != 0:
		n = random.randint(1,3)
		BusAS -= n
		if BusAS <= 0:
			BusAS = 0

		n = random.randint(1,3)
		BusBS -= n
		if BusBS <=0:
			BusBS = 0
	x += 1
	if x == 100:
		x = 0
	server_message = str(BusA) + "," + str(BusAS) + "," + str(BusB) + "," + str(BusBS)
	print(server_message)

    				
	microgear.chat("bus server",server_message)
	