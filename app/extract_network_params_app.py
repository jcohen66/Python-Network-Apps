from network.ip_file_valid import ip_file_valid
from network.ip_address_valid import ip_addr_valid
from network.ip_reach import ip_reach
from network.ssh_connection_top import ssh_connection
from network.create_threads import create_threads
import sys
import time

# Save the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

# Verify the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user.  Exiting ...")
    sys.exit()

# Verify the reachability of each IP address in the list
try:
    ip_reach(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user.  Exiting ...")
    sys.exit()

# Call threads creation function for one or multiple SSH connections
# every 10 seconds
while True:
    create_threads(ip_list, ssh_connection)
    time.sleep(10)

# End of program

