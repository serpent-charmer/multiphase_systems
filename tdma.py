def TDMA(a, b, c, d):

    nf = len(d)
    ac, bc, cc, dc = a[:], b[:], c[:], d[:]
    for it in range(1, nf):
        mc = ac[it-1]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1]
        dc[it] = dc[it] - mc*dc[it-1]

    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for il in range(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    return xc

if __name__ == '__main__':
	a = [3, 1, 3]
	b = [10, 10, 7, 4]
	c = [2, 4, 5]
	d = [3, 4, 5, 6]	
	
	print(TDMA(a, b, c, d))
