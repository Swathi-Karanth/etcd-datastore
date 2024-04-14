    # list all the keys in the etcd cluster
    # 3 node cluster localhost:2379, localhost:2378, localhost:2377

import etcd3

ports = [2379, 2378, 2377]
def list_keys():
    def print_keys(port):
        etcd = etcd3.client(host='localhost', port=port)
        i = 1
        print("Retrieving all keys from port " + str(port) + ":")
        for  _, metadata in etcd.get_all():
            print( i, "-", metadata.key.decode('utf-8'))
            # print("Value: " + value.decode('utf-8'))
            i += 1

    printed = False
    for port in ports:
        try:
            print_keys(port)
            printed = True
            break
        except Exception as e:
            print("Port " + str(port) + " is not reachable. Error: " + str(e))
        
    if not printed:
        print("None of the ports are reachable")


    # get the corresponding value for the key in the 3 node etcd cluster
def get_value():
    import etcd3

    print("Enter the key to get the value:")
    key = input()

    def get_value(key, port):
        etcd = etcd3.client(host='localhost', port=port)
        value,_ = etcd.get(key)
        print("Value for key " + key + " in port " + str(port) + ":")
        print(value.decode('utf-8'))

    printed = False
    exists = False

    for port in ports:
        try:
            get_value(key, port)
            printed = True
            exists = True
            break
        except Exception as e:
            if str(e) == "'NoneType' object has no attribute 'decode'":
                print("Key not found while accessing cluster through node/port " + str(port) + "Checking for other nodes to access." + "\n")
                printed = True
            else:
                print("Port " + str(port) + " is not reachable. Error: " + str(e))
            
    if not printed:
        print("None of the ports are reachable")
    elif not exists:
        print("Key not found in the cluster.")

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
        
        
    # delete a key value pair in a 3 node etcd cluster.

def delete_pair():
    import etcd3

    print("Enter the key to delete:")
    key = input()

    def delete_pair(key, port):
        etcd = etcd3.client(host='localhost', port=port)
        key_exists = False
        for _,kv in etcd.get_all():
            if kv.key.decode('utf-8') == key:
                key_exists = True
                break
        
        if not key_exists:
            print("Key not found in the cluster. Check the key and try again.")
            return
        etcd.delete(key)

        print("Key-Value pair deleted in the cluster through port " + str(port))

    deleted = False

    for port in ports:
        try:
            delete_pair(key, port)
            deleted = True
            break
        except Exception as e:
            print("Port " + str(port) + " is not reachable. Error: " + str(e))

    if not deleted:
        print("None of the ports are reachable. Failed to delete key-value pair. Check the cluster health.")
        

if __name__ == "__main__":
    while True:
        print("Choose the operation to perform:")
        print("1. List all the keys")
        print("2. Get value for a key")
        print("3. Put a key-value pair")
        print("4. Delete a key-value pair")
        print("5. Exit")
        choice = int(input())
        if choice == 1:
            list_keys()
        elif choice == 2:
            get_value()
        elif choice == 3:
            put_pair()
        elif choice == 4:
            delete_pair()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
    
    print("\n\nThank you for using the etcd client")