import streamlit as st
import etcd3

ports = [2379, 2378, 2377]

def list_keys():
    def print_keys(port):
        etcd = etcd3.client(host='localhost', port=port)
        i = 1
        st.write(f"Retrieving all keys from port {port}:")
        for _, metadata in etcd.get_all():
            st.write(f"{i} - {metadata.key.decode('utf-8')}")
            i += 1
        
    printed = False
    for port in ports:
        try:
            print_keys(port)
            printed = True
            break
        except Exception as e:
            st.error(f"Port {port} is not reachable. Error: {e}")
    
    if not printed:
        st.error("None of the ports are reachable")

def get_value(key):
    printed = False
    exists = False
    def extract_val(key, port):
        etcd = etcd3.client(host='localhost', port=port)
        value,_ = etcd.get(key)
        st.write(f"Value for key {key} in port {port}:")
        st.write(value.decode('utf-8'))
    
    for port in ports:
        try:
            extract_val(key, port)
            printed = True
            exists = True
            break
        except Exception as e:
            if str(e) == "'NoneType' object has no attribute 'decode'":
                st.error(f"Key not found by accessing node {port}. Checking for other nodes")
                printed = True
            else:
                st.error(f"Port {port} is not reachable. Error: {e}")
    
    if not printed:
        st.error("None of the ports are reachable")
    elif not exists:
        st.error("Key not found in the cluster.")

def put_pair(key, value):
    def insert_pair(key, value, port):
        etcd = etcd3.client(host='localhost', port=port)
        etcd.put(key, value)
        st.write(f"Key-Value pair inserted in the cluster through port {port}")
    
    added = False
    for port in ports:
        try:
            insert_pair(key, value, port)
            added = True
            break
        except Exception as e:
            st.error(f"Port {port} is not reachable. Error: {e}")
    
    if not added:
        st.error("None of the ports are reachable. Failed to add key-value pair. Check the cluster health.")
    
def delete_pair(key):
    def remove_pair(key, port):
        etcd = etcd3.client(host='localhost', port=port)
        
        key_exists = False
        for _, kv in etcd.get_all():
            if kv.key.decode('utf-8') == key:
                key_exists = True
                break
        
        if not key_exists:
            st.error(f"Key not found in the cluster. Check the key and try again.")
            return
        etcd.delete(key)
        st.write(f"Key-Value pair deleted in the cluster through port {port}")
    
    deleted = False
    for port in ports:
        try:
            remove_pair(key, port)
            deleted = True
            break
        except Exception as e:
            st.error(f"Port {port} is not reachable. Error: {e}")
    
    if not deleted:
        st.error("None of the ports are reachable. Failed to delete key-value pair. Check the cluster health.")

    
def main():
    st.title("etcd Cluster Operations")
    # Display cluster status
    for port in ports:
        try:
            etcd = etcd3.client(host='localhost', port=port)
            stat = etcd.status()
            st.write("**Cluster status:**")
            st.text(f"Leader Details:")
            st.text(f"{stat.leader}")
            st.text(f"etcd version: {stat.version}")
            break
        
        except Exception as e:
            st.error(f"Node with port {port} is not reachable. Error: {e}")        
    choice = st.selectbox(
        "Choose the operation to perform:",
        ["List all the keys", "Get value for a key", "Put a key-value pair", "Delete a key-value pair"]
    )

    if choice == "List all the keys":
        list_keys()
    elif choice == "Get value for a key":
        key = st.text_input("Enter the key to get the value:")
        if st.button("Get Value"):
            get_value(key)
    elif choice == "Put a key-value pair":
        key = st.text_input("Enter the key:")
        value = st.text_input("Enter the value:")
        if st.button("Put Pair"):
            put_pair(key, value)
    elif choice == "Delete a key-value pair":
        key = st.text_input("Enter the key to delete:")
        if st.button("Delete Pair"):
            delete_pair(key)

    st.write("\n\nThank you for using the etcd client")

if __name__ == "__main__":
    main()
