    # delete a key value pair in a 3 node etcd cluster.

def delete_pair():
    import etcd3

    print("Enter the key to delete:")
    key = input()

    def delete_pair(key, port):
        etcd = etcd3.client(host='localhost', port=port)
        
        key_exists = False
        for _, kv in etcd.get_all():
            if kv.key.decode('utf-8') == key:
                key_exists = True
                break
        
        if not key_exists:
            print("Key not found in the cluster. Check the key and try again.")
            return
        etcd.delete(key)

        print("Key-Value pair deleted in the cluster through port " + str(port))

    ports = [2379, 2378, 2377]

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