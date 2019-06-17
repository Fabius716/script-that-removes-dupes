import os
l=[]
c=0

with open("psw.txt", "r") as d:
	print("Working...")
	for x in d:
		l.append(x)
		#print(x)
for z in range(len(l)-1):
	try:
		for x in range(len(l)-1):
			#print(c,x)
			if l[c] == l[x]:
				l.pop(c)
	except IndexError:
		continue
	c+=1
	
#print(l)

os.system("echo.>output.txt")
with open("output.txt","w") as f:
	for x in l:
		f.write(x)
print("Done")
