header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, sequence)
