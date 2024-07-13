def max_pack(pack):
    if not pack:
        return 0

    rem = 0
    max_sz = 0
    for pkt in pack:
        it = 1
        total = pkt + rem
        while it*2 < total:
            it *= 2

        max_sz = max(max_sz,it)
        rem = pkt - it

    return max_sz


packets=[13,25,12,2,8]
packets_2 = [12, 25, 10, 7, 8]
print(max_pack(packets))
print(max_pack(packets_2))