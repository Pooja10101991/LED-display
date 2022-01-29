# list containing the pattern for all 10 digit
digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]

def prnt_number(num):
	global digits
	dgs = str(num)
	lin = [ '' for i in range(5) ]
	for d in dgs:
		segm = [ [' ',' ',' '] for i in range(5) ]
		p= digits[ord(d) - ord('0')]
		if p[0] == '1':
			segm[0][0] = segm[0][1] = segm[0][2] = '*'
		if p[1] == '1':
			segm[0][2] = segm[1][2] = segm[2][2] = '*'
		if p[2] == '1':
			segm[2][2] = segm[3][2] = segm[4][2] = '*'
		if p[3] == '1':
			segm[4][0] = segm[4][1] = segm[4][2] = '*'
		if p[4] == '1':
			segm[2][0] = segm[3][0] = segm[4][0] = '*'
		if p[5] == '1':
			segm[0][0] = segm[1][0] = segm[2][0] = '*'
		if p[6] == '1':
			segm[2][0] = segm[2][1] = segm[2][2] = '*'
		for j in range(5):
			lin[j] += ''.join(segm[j]) + ' '
	for l in lin:
		print(l)

prnt_number(int(input("Enter the number to display: ")))

