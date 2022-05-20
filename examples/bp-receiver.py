python
import pyion

# Create a proxy to node 2 and attach to it
proxy = pyion.get_bp_proxy(2)
proxy.bp_attach()

# Listen to 'ipn:2.1' for incoming data
with proxy.bp_open('ipn:2.1') as eid:
    while eid.is_open:
        try:
            # This is a blocking call.
            print('Received:', eid.bp_receive())
        except InterruptedError:
            # User has triggered interruption with Ctrl+C
            break
