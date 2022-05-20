# General imports
import pickle
import numpy as np
import string

# Import module
import pyion

# =================================================================
# === Define global variables
# =================================================================

# ION node numbers
node_nbr, peer_nbr = 1, 2

# Client identifier
client_id = 4

# Define data size in bytes. Set to 1200 bytes because LTP block and
# LTP segment are set to this value
data_size = 2400

# Define data to send as a stream of random ASCII chars. Each char
# uses 1 byte.
chars = list(string.ascii_lowercase)
data  = np.random.choice(chars, size=(data_size,)).astype('|S1').tostring()

# =================================================================
# === MAIN
# =================================================================

# Create a proxy to LTP
pxy = pyion.get_ltp_proxy(node_nbr)

# Attach to ION's LTP engine
pxy.ltp_attach()

# Open a endpoint access point for this client and send data
with pxy.ltp_open(client_id) as sap:
    print('Sending', data)
    sap.ltp_send(peer_nbr, data)
