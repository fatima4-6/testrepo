f=open("students.csv",'r')
data=f.read()
a= data.split("\n")
Table=[]
for i in range (0,len(a)):
    if(a[i]==''):
        continue
    Table.append(a[i].split(","))
    
for i in range(0,len(Table)):
    for j in range(0,len(Table[0])):
        print(Table[i][j],end="\t")
    print()



sum=[]
mean=[]
for i in range(1,len(Table)):
    total=0
    for j in range(1,len(Table[0])):
        total+=int(Table[i][j])
    mean.append(total/len(Table)-1)
    sum.append(total)

Table[0].append("Total")
for i in range(1,len(Table)):
    Table[i].append(sum[i-1])

Table[0].append("Mean")
for i in range(1,len(Table)):
    Table[i].append(mean[i-1])

for i in range(0,len(Table)):
    for j in range(0,len(Table[0])):
        print(Table[i][j],end="\t")
    print()
f.close()

g = open("student.csv","w")

for i in range(len(Table)):
    for j in range(len(Table[0])):
        g.write(str(Table[i][j]))
        g.write(",")
    g.write("\n")
g.close()
