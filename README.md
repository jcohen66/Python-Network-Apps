# Python Network Applications

### ssh_configuration_app.py
Read and write network switch configuration in
virtual 3 node network of Arista switches.

Requires input of three config files:
* user.txt containing credentials
* commands.txt containing Arista switch commands
* ip.txt containing list of ips for Arista switches in network

### ssh_configuration_top_app.py
Every 10 seconds, poll the switch for top 
cpu data and append to cpu.txt file.

#### Generate traffic on the switch 1
```ping 10.10.10.3 size 18000 repeat 250000```