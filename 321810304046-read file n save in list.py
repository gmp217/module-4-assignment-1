a=input('Enter file name: ')
with open (a, "r") as myfile:
                b=[]
                for i in myfile:
                	b.append(i)
print(b)
              