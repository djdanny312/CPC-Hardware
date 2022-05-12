from bluetooth import *
from variables import esp32BT_address
#most of these functions can be found on pybluez documentation, in PyBluez API

def executeBT():           
    #MAC address of ESP32
    addr = esp32BT_address
    #takes bluetooth device friendly name and returns a list of dictionary with host,name,description,protocol,port and more.
    service_matches = find_service( address = addr )

    buf_size = 1024;
    #if the device has not been found
    if len(service_matches) == 0:
        print("couldn't find the SampleServer service =(")
        sys.exit(0)
    #prints device description mentioned before
    for s in range(len(service_matches)):
        print("\nservice_matches: [" + str(s) + "]:")
        print(service_matches[s])
    #matches the name and host from the dictionaries and assigns them to variables    
    first_match = service_matches[0]
    
    name = first_match["name"]
    host = first_match["host"]
    #always defaulting the port to 1
    port=1
    print("connecting to \"%s\" on %s, port %s" % (name, host, port))

    # Create the client socket
    sock=BluetoothSocket(RFCOMM)
    sock.connect((host, port))

    print("\nconnected")

    #send message through Bluetooth on Serial Protocol and closes the socket
    sock.send("access granted")
    sock.close()

    print("\n--- bye ---\n")
