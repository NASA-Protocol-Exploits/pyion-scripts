#Default Bundle Protocol Pyion Script (Transmitter)

# Import module
import pyion

# Create a proxy to node 1 and attach to ION
proxy = pyion.get_bp_proxy(1)
proxy.bp_attach()

# Open endpoint 'ipn:1.1' and send data to 'ipn:2.1'
with proxy.bp_open('ipn:1.1') as eid:
    eid.bp_send('ipn:2.1', b'hello')
