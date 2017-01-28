import socket , pickle
import keyConfigs
 
port = int(input("Enter port number: "))
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()
ip=input("Enter IP address: ")
client_socket.connect((ip,port))

# begin key exchange
data = client_socket.recv(512)
recievedKey = pickle.loads(data)
privateKey, computedKey = keyConfigs.generateKey()
client_socket.send(pickle.dumps(computedKey))
finalKey = keyConfigs.computeKey(privateKey, recievedKey)
print ("The generated key : " , finalKey)
while 1:
    data = client_socket.recv(512)
    if ( data == 'bye' ):
        print (client_socket.getsockname()[0] , data)
        client_socket.close()
        break
    else:
        print (client_socket.getsockname()[0] , data)
        message = input ( "SEND( TYPE bye to Quit):" )
        if message == 'bye':
            message = str.encode(message)
            client_socket.send(message)
            client_socket.close()
            break
        else:
            message = str.encode(message)
            client_socket.send(message)