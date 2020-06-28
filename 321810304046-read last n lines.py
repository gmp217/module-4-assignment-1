a,N=input('Enter file name: '),int(input('Enter no of lines: '))
b=open(a)	
for i in (b.readlines() [-N:]):
	print(i,end=' ')