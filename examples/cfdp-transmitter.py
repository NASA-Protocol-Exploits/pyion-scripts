# Default CFDP Pyion Script (Transmitter)

# Import module
import pyion
import pyion.constants as cst

# Create a proxy to node 1 and attach to ION
bpxy = pyion.get_bp_proxy(1)
cpxy = pyion.get_cfdp_proxy(1)

# Attach to ION
bpxy.bp_attach()
cpxy.cfdp_attach()

# Create endpoint and entity
ept = bpxy.bp_open('ipn:1.1')
ett = cpxy.cfdp_open(2, ept)

# Define handler and register it
def ev_handler(ev_type, ev_params):
  print(ev_type, ev_params)
ett.register_event_handler(cst.CFDP_ALL_EVENTS, ev_handler)

# Send a file
ett.cfdp_send('source_file')

# Wait for CFDP transaction to end
ok = ett.wait_for_transaction_end()
if ok:
  print('Successful file transfer')
else:
  print('Failed transaction')
