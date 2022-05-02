inputs = float(input())
while True:
	n = float(input())
	if(n==999): break
	print('{:0.2f}'.format(n-inputs))
	inputs = n