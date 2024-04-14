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


    ports = [2379, 2378, 2377]
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
                print("Key not found in port " + str(port) + "\n")
                printed = True
            else:
                print("Port " + str(port) + " is not reachable. Error: " + str(e))
            
    if not printed:
        print("None of the ports are reachable")
    elif not exists:
        print("Key not found in any of the ports")