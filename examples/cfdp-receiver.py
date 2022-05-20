# Default CFDP Pyion Script (Receiver)

# Import module
import pyion
import pyion.constants as cst

# Create a proxy to node 2 and attach to ION
bpxy = pyion.get_bp_proxy(2)
cpxy = pyion.get_cfdp_proxy(2)

# Attach to ION
bpxy.bp_attach()
cpxy.cfdp_attach()

# Create endpoint and entity
ept = bpxy.bp_open('ipn:2.1')
ett = cpxy.cfdp_open(1, ept)

# Define handler and register it
def ev_handler(ev_type, ev_params):
  print(ev_type, ev_params)
ett.register_event_handler(cst.CFDP_ALL_EVENTS, cfdp_event_handler)

# Wait for end of transaction
ett.wait_for_transaction_end()
