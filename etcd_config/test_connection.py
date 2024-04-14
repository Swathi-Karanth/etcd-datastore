# # >>> help(etcd3.client) 
# Help on function client in module etcd3.client:

# client(host='localhost', port=2379, ca_cert=None, cert_key=None, cert_cert=None, timeout=None, user=None, password=None, grpc_options=None)        
#     Return an instance of an Etcd3Client.

import etcd3

client = etcd3.client()
print(client)