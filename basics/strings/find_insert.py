my_string = "Cisco model: 2600XM, 2 WAN slots, IOS 12.4"

b = "Cisco" in my_string
b = "turd" not in my_string

s = my_string * 3

s = "Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4)
s = "Cisco model: %s, %d WAN slots, IOS %.2f" % ("7200XR", 8, 15.4)
s = "Cisco model: %s, %d WAN slots, IOS %.f" % ("7200XR", 8, 15.4)

s = "Cisco model: {}, {} WAN slots, IOS {}".format ("7200XR", 8, 15.4)      # absolute order
s = "Cisco model: {0}, {1} WAN slots, IOS {2}".format ("7200XR", 8, 15.4)   # can switch order
s = "Cisco model: {0}, {2} WAN slots, IOS {1}".format ("7200XR", 8, 15.4)   # can switch order
s = "Cisco model: {2}, {1} WAN slots, IOS {1}".format ("7200XR", 8, 15.4)   # can switch order and repeat






