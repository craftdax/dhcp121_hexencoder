"""
Scripts converts list of tuples into hex string for dhcp option 121
"""


def routes_to_dhcp121_hex(route):
    return b"".join([b"%02x" % octet for octet in route])


routes = [
    (16, 10, 14, 10, 14, 252, 5),
    (32, 1, 1, 1, 1, 10, 14, 252, 5),
    (32, 156, 146, 62, 198, 10, 14, 252, 5),
    (32, 212, 102, 36, 176, 10, 14, 252, 5),
]

print(b"".join(routes_to_dhcp121_hex(route) for route in routes))
