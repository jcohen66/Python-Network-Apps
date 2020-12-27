import random
import sys


def subnet_calc():

    try:
        print("\n")

        # Check IP address validity
        while True:
            ip_address = input("Enter an IP address: ")

            # Check octets
            ip_octets = ip_address.split('.')

            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (
                    int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (
                    0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break

            else:
                print("\nThe IP address is INVALID! Please retry!\n")
                continue

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        while True:

            # Check validity of subnet mask
            subnet_mask = input("Enter a subnet mask: ")

            # Check octets
            mask_octets = subnet_mask.split(".")

            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (
                    int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (
                    int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break

            else:
                print("\nThe subnet mask is INVALID! Please retry!\n")
                continue

        # Algorithm for subnet identification, based on IP and subnet mask.

        # Convert mask to binary string
        mask_octets_binary = []

        for octet in mask_octets:
            # Strip out the python decoration for binary.
            binary_octet = bin(int(octet)).lstrip('0b')
            # print(binary_octet)

            # Ensure that we have 8 bits after conversion.
            mask_octets_binary.append(binary_octet.zfill(8))

        # print(mask_octets_binary)

        binary_mask = "".join(mask_octets_binary)

        # Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)     # return a positive value for the /32 mask (all 255s)

        # print(no_of_zeros)
        # print(no_of_ones)
        # print(no_of_hosts)

        # Obtain wildcard mask by subtracting the mask from 255.255.255.255
        wildcard_octets = []
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))

        wildcard_mask = ".".join(wildcard_octets)
        # print(wildcard_mask)


        # Convert IP to binary string
        ip_octets_binary = []

        for octet in ip_octets:
            ip_octet_binary = bin(int(octet)).lstrip('0b')
            # print(ip_octet_binary)

            ip_octets_binary.append(ip_octet_binary.zfill(8))

        # print(ip_octets_binary)

        binary_ip = "".join(ip_octets_binary)

        # Get the network address and broadcast address from the binary strings obtained above
        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        # print(network_address_binary)

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        # print(broadcast_address_binary)

        # Convert everything back to decimal (readable format)
        net_ip_octets = []

        # range(0, 32, 8) means 0-32 by step 8 ie 0, 8, 16, 24
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)

        # End up with 4 slices of the binary IP address: [0: 8], [8: 16], [16: 24] and [24: 32]

        # print(net_ip_octets)

        net_ip_address = []

        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        # print(net_ip_address)

        network_address = ".".join(net_ip_address)
        # print(network_address)

        bst_ip_octets = []

        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)

        # print(bst_ip_octets)

        bst_ip_address = []

        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        # print(bst_ip_address)

        broadcast_address = ".".join(bst_ip_address)
        # print(broadcast_address)

        # Results for selected IP/mask
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % no_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")

        # Generate random IP addresses in the subnet
        while True:
            generate = input("Generate random IP address from this subnet? (y/n)")

            if generate == "n":
                print("\n\nDone.  Bye!")
                break

            # Obtain available IP address in range,  based on the difference between octets
            # in the broadcast address and the ip address.
            generated_ip = []
            for indexb, oct_bst in enumerate(bst_ip_address):
                # print(indexb, oct_bst)
                for indexn, oct_net in enumerate(net_ip_address):
                    if indexb == indexn:
                        if oct_bst == oct_net:
                            # Add identical octets to the generated_ip list
                            generated_ip.append(oct_bst)
                        else:
                            # Generate random number(s) from within octet intervals and add ot list
                            generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

            # IP address generated from the subnet pool
            y_iaddr = ".".join(generated_ip)
            print("Random IP is: {}".format(y_iaddr))
            print("\n")
            continue


    except KeyboardInterrupt:
        print("\n\nProgram aborted by user.  Exiting...\n")
        sys.exit()


subnet_calc()