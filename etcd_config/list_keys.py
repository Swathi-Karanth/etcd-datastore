    # list all the keys in the etcd cluster
    # 3 node cluster localhost:2379, localhost:2378, localhost:2377

def list_keys():
    def print_keys(port):
        etcd = etcd3.client(host='localhost', port=port)
        i = 1
        print("Retrieving all keys from port " + str(port) + ":")
        for  _, metadata in etcd.get_all():
            print( i, "-", metadata.key.decode('utf-8'))
            # print("Value: " + value.decode('utf-8'))
            i += 1

    import etcd3
    ports = [2379, 2378, 2377]
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