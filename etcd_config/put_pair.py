    # accept a key and a vakue from the user and store it in the etcd cluster. 
    # if a key already exists, the value gets updated. 

def put_pair():
    import etcd3

    print("Enter the key")
    key = input()

    print("Enter the value")
    value = input()

    def put_pair(key, value, port):
        etcd = etcd3.client(host='localhost', port=port)
        etcd.put(key, value)
        print("Key-Value pair inserted in the cluster through port " + str(port))

    ports = [2379, 2378, 2377]
    added = False

    for port in ports:
        try:
            put_pair(key, value, port)
            added = True
            break
        except Exception as e:
            print("Port " + str(port) + " is not reachable. Error: " + str(e))
            
    if not added:
        print("None of the ports are reachable. Failed to add key-value pair. Check the cluster health.")