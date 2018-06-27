def Possibilities(amount, denominations):
	l = len(denominations)
	res = [[0 for i in range(l)] for j in range(amount+1)]
	if l==0:
		return 0;
	for i in range(l):
		res[0][i] = 1
	for j in range(1,amount+1):
		for k in range(l):
			i = result_table[j - denominations[k]][k] if j-denominations[k] >= 0 else 0
			a = result_table[j][k-1] if k >= 1 else 0
			res[i][j]=i+a
	return res[amount][l-1]
