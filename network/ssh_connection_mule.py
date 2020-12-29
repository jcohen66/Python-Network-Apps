import paramiko
import os.path
import time
import sys
import re
import shutil
from network.create_threads import create_threads




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
    sys.exit()

def download_file(ip, session, files_to_download):

    # Download each file using sftp
    files = files_to_download.split(',')
    remote_file = files[0].replace('\n', '')
    local_file = files[1].replace('\n', '') + '-' + ip.replace('.', '_')

    # Open af file for capturing output
    with open(local_file, 'w+') as out_file:

        sftp_client = session.open_sftp()
        remote_file = sftp_client.open(remote_file)
        try:
            for line in remote_file:
                # process line
                out_file.write(str(line))
                print(str(line))
        finally:
            remote_file.close()

    print("DONE for remote: {}  local: {}".format(remote_file, local_file))

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

        # Open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Download each file using sftp
        files_to_cat = []
        for file_pair in selected_cmd_file.readlines():
            download_file(ip, session, file_pair)

            print("DONE for device: {}".format(ip))
            time.sleep(2)

        # Close the user file
        selected_user_file.close()

        # Close the command file
        selected_cmd_file.close()




        # Test for reading command output
        # print(str(router_output) + "\n")
        # print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", str(router_output))[1])

        # Close the connection
        session.close()

    except paramiko.AuthenticationException:
        print("* invalid username or password :( Please check the username/password file and device configuration.\n")
        print("* Closing program.., Bye!")
