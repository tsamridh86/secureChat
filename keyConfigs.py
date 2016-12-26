from random import randrange
generator = 2
divisor = 67

def generateKey():
	num = randrange(1,100)
	return num , pow(generator,num,divisor).to_bytes(1,byteorder="big")

def computeKey(privateKey, recievedKey):
	return pow(recievedKey,privateKey,divisor)