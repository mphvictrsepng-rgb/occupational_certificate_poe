import math

# 1.1 - returning the minimum number of rooms needed
# Each room can take up to 3 people, so I round up if there are leftover guests

def rooms_needed(guests):
    return math.ceil(guests / 3)         #ceil rounds up to the nearest whole number


# 1.2 - calculate how many /24 subnets can hold 30 hosts each
# A /24 network has 256 addresses and a /27 has 32 addresses (minus 2 for network and broadcast, so 30 usable hosts)

def subnets_for_30_hosts():
    addresses = 256
    subnet_size = 32
    return addresses // subnet_size


# quick examples to show the results
print("1.1 - rooms needed =", rooms_needed(10))
print("1.2 - subnets for 30 hosts =", subnets_for_30_hosts())
