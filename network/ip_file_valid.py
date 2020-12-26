import os.path
import sys

# Check IP address file and content validity
def ip_file_valid():

    # Prompt user for input
    ip_file = input("\n# Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ")

    # Check if the file exists
    if os.path.isfile(ip_file) == True:
        print("\n* IP file is valid :) \n")
    else:
        print("\n* File {} does not exist L(  Please check and try again.\n".format(ip_file))
        sys.exit()

    # Open user selected file for reading (IP addresses file)
    selected_ip_file = open(ip_file, "r")

    # Start from the beginning of the file
    selected_ip_file.seek(0)

    # Read each line (IP address) in the file
    ip_list = selected_ip_file.readlines()

    # Close the file
    selected_ip_file.close()

    return ip_list