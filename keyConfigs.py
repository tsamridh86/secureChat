from random import randrange
generator = 2
divisor = 67

def generateKey():
	privateKey = []
	transferKey = [] 
	for i in range(0,10):
		num = randrange(10,100)
		privateKey.append(num)
		transferKey.append(pow(generator,num,divisor))
	return privateKey, transferKey

def computeKey(privateKey, recievedKey):
	finalKey = []
	for i in range(len(privateKey)):
		finalKey.append(pow(recievedKey[i],privateKey[i],divisor))
	return finalKey