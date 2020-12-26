import paramiko
import os.path
import time
import sys
import re


# Check username/password file
# Prompt user for input - USERNAME/PASSWORD file
user_file = input("\n% Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")

if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")
else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()

# Check commands file
# Prompt user for input - COMMANDS FILE
cmd_file = input("\n% Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

# Verify the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid :)\n")
else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys,exit()


# Open SSHv2 connection to the device
def ssh_connection(ip):
    global user_file
    global cmd_file

    # Create SSH Connection
    try:
        # Define SSH parameters
        selected_user_file = open(user_file, 'r')

        # Starting from the beginning
        selected_user_file.seek(0)

        login = selected_user_file.readlines()[0]
        # Read the username from the file
        username = login.split(',')[0].rstrip("\n")

        # Read the password from the file
        password = login.split(',')[1].rstrip("\n")

        # Log into device
        session = paramiko.SSHClient()

        # For testing purposes, this allows auto-accepting unknown host keys
        # Do not use in production!  The default would be paramiko.RejectPolicy
        session.set_missing_host_key_policy( paramiko.AutoAddPolicy() )

        # Connect to the device using username and password
        session.connect(ip.rstrip("\n"), username = username, password = password)

        # Start an interactive shell session on the router
        connection = session.invoke_shell()

        # Set terminal length for entire output - disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        # Enter global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        # Open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + "\n")
            time.sleep(2)

        # Close the user file
        selected_user_file.close()

        # Close the command file
        selected_cmd_file.close()

        # Check command output for IOS syntax errors
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("There is at least one IOS syntax error on device! {}".format(ip))
        else:
            print("DONE for device: {}".format(ip))

        # Test for reading command output
        print(str(router_output) + "\n")
        # print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", str(router_output))[1])

        # Close the connection
        session.close()

    except paramiko.AuthenticationException:
        print("* invalid username or password :( Please check the username/password file and device configuration.\n")
        print("* Closing program.., Bye!")
