# General imports
import pickle

# Import module
import pyion

# =================================================================
# === Define global variables
# =================================================================

# ION node numbers
node_nbr, peer_nbr = 2, 1

# Client identifier
client_id = 4

# =================================================================
# === MAIN
# =================================================================

# Create a proxies to ION
pxy = pyion.get_ltp_proxy(node_nbr)

# Attach to ION's BP and CFDP
pxy.ltp_attach()

# Open a service access point and receive data
with pxy.ltp_open(client_id) as sap:
    # You are now ready to received
    print('LTP ready to receive data')

    # Receive
    while sap.is_open:
        try:
            # This is a blocking call
            data = sap.ltp_receive()
            print(data)
        except ConnectionAbortedError:
            break
