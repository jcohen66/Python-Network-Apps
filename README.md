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
```
ping 10.10.10.3 size 18000 repeat 250000
```


### ssh_sftp_app.py
For a given set of ips, download a given set
of remote files to local files.

Output files are written to ../output directory 
and files are post-pended with with the ip. 

#### user.txt
````
user,pw
````

#### files.txt
````
/opt/mule/logs/error.log,../output/error.log
/opt/mule/logs/usta_maven.log,../output/usta_maven.log
````

#### ip.txt
````
10.31.92.31
10.31.92.32
````
