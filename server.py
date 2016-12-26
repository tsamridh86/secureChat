import socket,sys
import keyConfigs

def intialise( port ):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print ('Failed to create socket')
        sys.exit()
    print ('Listening for connections on port '+str(port)+'.')
    s.bind(('127.0.0.1',port))
    print ("Waiting for connection")
    return s

def run( port ):
    socket = intialise(port)
    socket.listen(1)
    c,addr = socket.accept()
    print ('Connected to ',addr)
    # begin key exchange
    privateKey, computedKey = keyConfigs.generateKey()
    c.send(computedKey)
    data = c.recv(512)
    recievedKey = int.from_bytes(data,byteorder="big")
    finalKey = keyConfigs.computeKey(privateKey, recievedKey)
    c.send(b"Ack")
    print ("The generated key : " , finalKey)
    while True:
        data = c.recv(512)
        print (addr[0], data)
        if data == b'bye':
            print ("Disconnected from the client, Shutting down server.")
            exit()
            c.close()
            return False
        message = input ( ">>" )
        message = str.encode(message)
        c.send(message)
    
 
port = int(input("Enter a port no to run on : "))
run(port) 

