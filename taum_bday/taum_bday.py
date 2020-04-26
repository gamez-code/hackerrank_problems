def taumBday(b, w, bc, wc, z):
    # Write your code here
    if bc < wc and bc + z < wc:
        wc = bc + z
    elif wc < bc and wc + z < bc:
        bc = wc + z

    return b * bc + w * wc


if __name__ == '__main__':
    print(taumBday(3, 6, 9, 1, 1))
