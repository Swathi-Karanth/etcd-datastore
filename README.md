# etcd Cluster Operations App

etcd is a distributed key-value store that provides a reliable way to store data across a cluster of machines. It implements the **Raft consensus algorithm** to ensure that data is consistent and available even in the event of node failures. Raft is a consensus algorithm that allows a cluster of nodes to elect a leader and replicate data across the cluster in a consistent manner. etcd uses Raft to maintain a consistent view of the data across all nodes in the cluster. This ensures that data is always available and up-to-date, even if some nodes are down or unreachable. 

Data is no longer maintained in one single centralized server, but rather distributed across multiple nodes in the cluster. This provides fault tolerance and high availability, as the data can be replicated across multiple nodes to ensure that it is always available, even in the event of node failures. etcd is commonly used in distributed systems to store configuration data, service discovery information, and other key-value pairs that need to be shared across multiple nodes. It provides a simple HTTP API for interacting with the cluster and supports operations like get, put, and delete for managing key-value pairs.

etcd is commonly used in distributed systems to store configuration data, service discovery information, and other key-value pairs that need to be shared across multiple nodes. It provides a simple HTTP API for interacting with the cluster and supports operations like get, put, and delete for managing key-value pairs.

In this project to understand the behaviour of etcd cluster, we have created a Streamlit app that allows you to perform various operations on an etcd cluster running on localhost with multiple nodes. The app provides a simple interface for listing all the keys stored in the cluster, getting the value for a specific key, putting a new key-value pair, and deleting an existing key-value pair. The app uses the **etcd3 Python client library** to interact with the etcd cluster and perform these operations. 

The app is designed to be user-friendly and intuitive, with clear instructions and error messages to guide the user through the process. We can see how raft consensus algorithm works in etcd cluster and how data is replicated across multiple nodes in the cluster. This app can be used to explore the capabilities of etcd and understand how it can be used to store and manage data in a distributed system.

We have 2 implementations of this app. One is using command-line (terminal) and the other is using GUI (Streamlit). The command-line implementation is more suitable for users who prefer a text-based interface and want to interact with the etcd cluster using commands. The GUI implementation is more suitable for users who prefer a graphical interface and want to interact with the etcd cluster using a web browser. Both implementations provide the same functionality and allow users to perform the same operations on the etcd cluster.

We use the [etcd3 Python client library](https://python-etcd3.readthedocs.io/en/latest/installation.html) to interact with the etcd cluster and perform operations like get, put, and delete on the key-value pairs stored in the cluster. The etcd3 library provides a simple and easy-to-use interface for interacting with the etcd cluster and allows us to perform these operations with just a few lines of code. We can see how the data is replicated across the nodes in the cluster and how the Raft consensus algorithm ensures that the data is consistent and available even in the event of node failures.

## etcd cluster and system information
- This project uses a 3-node etcd cluster running on localhost with the following configuration:
  - Node 1: http://localhost:2379
  - Node 2: http://localhost:2378
  - Node 3: http://localhost:2377

- etcd version used: v3.5.12
- Operating system: Windows 11

## Files
- **snapshot.db** : This file is created by etcd to store the snapshot of the data in the cluster. It is used to restore the data in case of node failures or restarts. The snapshot.db file is stored in the data directory specified in the etcd configuration file. It contains a copy of the data stored in the etcd cluster at the time the snapshot was taken. The snapshot.db file is used to restore the data when a node restarts or when a new node joins the cluster. It ensures that the data is consistent across all nodes in the cluster and that no data is lost in the event of node failures.
- **etcd_config/config_files folder**: This folder contains the configuration files (```.yaml```) for the etcd cluster nodes. Each configuration file specifies the node's name, data directory, listen client URLs, listen peer URLs, and initial cluster configuration. The configuration files are used to start the etcd nodes with the specified settings. The configuration files ensure that all nodes in the cluster have the same configuration and can communicate with each other to maintain consistency and availability of the data.
- delete_key.py: This file contains the code to delete a key-value pair from the etcd cluster. It takes a key as input and deletes the corresponding key-value pair from the cluster. If the key does not exist, an error message is displayed stating that the key was not found in the cluster. The delete_key function uses the etcd3 Python client library to interact with the etcd cluster and perform the delete operation.
- **get_key.py**: This file contains the code to get the value for a key from the etcd cluster. It takes a key as input and retrieves the corresponding value from the cluster. If the key does not exist, an error message is displayed stating that the key was not found in the cluster. The get_key function uses the etcd3 Python client library to interact with the etcd cluster and perform the get operation.
- **list_keys.py**: This file contains the code to list all the keys stored in the etcd cluster. It retrieves and displays all the keys in the cluster in alphabetical order. The list_keys function uses the etcd3 Python client library to interact with the etcd cluster and perform the list operation.
- **put_pair.py**: This file contains the code to put a new key-value pair in the etcd cluster. It takes a key and value as input and adds the key-value pair to the cluster. If the key already exists, its value is updated. The put_key function uses the etcd3 Python client library to interact with the etcd cluster and perform the put operation.
- app.py: This file contains the code for the Streamlit app that allows users to interact with the etcd cluster using a graphical interface. The app provides options to list all keys, get the value for a key, put a new key-value pair, and delete a key-value pair. The app uses the etcd3 Python client library to interact with the etcd cluster and perform the specified operations. The app displays clear instructions and error messages to guide the user through the process.
- **app_command_line.py**: This file contains the code for the command-line interface that allows users to interact with the etcd cluster using text-based commands. The command-line interface provides options to list all keys, get the value for a key, put a new key-value pair, and delete a key-value pair. The command-line interface uses the etcd3 Python client library to interact with the etcd cluster and perform the specified operations. The command-line interface displays clear instructions and error messages to guide the user through the process.


Note: 
- If you wish to change the localhost and port number, you can do so by changing the values in the configuration files and the Streamlit app accordingly. Make sure to update the Streamlit app with the correct configuration settings to interact with the etcd cluster running on the specified host and port.
- The 4 individual files (delete_key.py, get_key.py, list_keys.py, put_pair.py) are used to perform the respective operations individually on the etcd cluster. They contain only command-line implementation and are not part of the Streamlit app. 

## Features

- **List all the keys:** Retrieve and display all the keys stored in the etcd cluster. This provides an overview of the data stored in the cluster. It lists the keys in alphabetical order.
- **Get value for a key:** Enter a key and get its corresponding value from the etcd cluster. If the key does not exist, an error message will be displayed stating key was not found in the cluster. It is case-sensitive and must be entered exactly as it is stored in the cluster.
- **Put a key-value pair:** Add a new key-value pair to the etcd cluster. If the key already exists, its value will be updated.
- **Delete a key-value pair:** Enter a key to delete its corresponding key-value pair from the etcd cluster. If the key does not exist, an error message will be displayed stating key was not found in the cluster.

## Usage

1. Install etcd on your machine. You can download the latest release from the [github repository](https://github.com/etcd-io/etcd/releases). Use version 3.5.12 for this project to avoid conflicts. Extract the downloaded file and add the etcd binary to your PATH.
   
    To check if etcd is installed correctly, run the following command in your terminal:

    ```bash
    etcd --version
    ```

    You should see the version number of etcd installed on your machine.

    In case, the link doesn't work, we have added the etcd binary in the project folder. You can add the etcd binary to your PATH and use that to run the etcd cluster.
2. Clone the repository:

    ```bash
    git clone https://github.com/your_username/etcd-cluster-operations-app.git
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Go to Project Directory:

    ```bash
    cd Product
    ```
5. Start the etcd cluster:

    ```bash
    etcd --config-file=etcd_config/config_files/etcd1.yaml
    etcd --config-file=etcd_config/config_files/etcd2.yaml
    etcd --config-file=etcd_config/config_files/etcd3.yaml
    ```

6. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

    To Run the command-line app:
    ```bash
    python app_command_line.py
    ```

7. Choose the operation you want to perform from the dropdown menu and follow the instructions.

## Requirements/Installation for this project

- Python 3.11.5
- pip 23.3.2
- Streamlit 1.28.1
- etcd 3.5.12
- Code Editor: Visual Studio Code

## Note

- Make sure your etcd cluster is running on localhost with the specified ports (2379, 2378, 2377) for this app to interact with it. If ports are different, update the Streamlit app and configuration file (.yaml files) accordingly.
- If any port is unreachable or if there are errors during operations, appropriate error messages will be displayed to guide you.
- Make sure to run the commands in step 5 in separate terminal windows to start each node of the etcd cluster. If you are using a different configuration file or port numbers, update the Streamlit app accordingly. Also, if the command fails, it is probably because the etcd binary is not in your PATH. You can specify the full path to the etcd binary in the command. In some cases, the ports might be in use, so you can change the port numbers in the configuration files.
- Before you stop the server, make sure to take a snapshot of the data in the etcd cluster. This can be done using the etcdctl snapshot save command. The snapshot.db file will be created in the data directory specified in the etcd configuration file. This file can be used to restore the data when the server is restarted or when a new node joins the cluster. 

    To take a snapshot of the data in the etcd cluster, run the following command:
    ```bash
    etcdctl --endpoints=http://localhost:2377 snapshot save snapshot.db 
    ```
    You can also take snapshots of the other nodes in the cluster:
    ```bash
    etcdctl --endpoints=http://localhost:2378 snapshot save snapshot.db
    ```
    or
    ```bash 
    etcdctl --endpoints=http://localhost:2379 snapshot save snapshot.db 
    ```
