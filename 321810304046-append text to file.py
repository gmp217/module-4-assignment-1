n=input('Enter file name: ')
with open(n, 'a') as f:
	f.write('\nappend me\n')
t=open(n,'r+')
print(t.read())