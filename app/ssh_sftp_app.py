from network.ip_file_valid import ip_file_valid
from network.ip_address_valid import ip_addr_valid
from network.ip_reach import ip_reach
from network.ssh_connection_mule import ssh_connection
from network.create_threads import create_threads
import sys

# Save the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

# Verify the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user.  Exiting ...")
    sys.exit()

create_threads(ip_list, ssh_connection)

# End of program

