import numpy as np
try:
    for l in range(1000, 10000, 10):
        f=open("zeros3SR=20000_N=20/vwf"+str(l)+".vtk")
except IOError:
    print("файла "+str(l)+" не существует, конечный файл - "+str(l-10))
finally:
    f.close()
print(l-10)

    
my_file = open("raskritie_domeni.txt", "w")
filename = "zeros3SR=20000_N=20/vwf"+str(l-10)+".vtk"
r0=0.5
k=0
n=0
c=0
v=0
x=np.zeros(525, dtype=float)
y=np.zeros(525, dtype=float)
z=np.zeros(525, dtype=float)
def F1(x,y,z,j):
    return ((x[j]-x[j-1])**2 +(y[j]-y[j-1])**2 +(z[j]-z[j-1])**2)**0.5
def F2(x,y,z,j):
    return ((x[j]-x[j+1])**2 +(y[j]-y[j+1])**2 +(z[j]-z[j+1])**2)**0.5
with open(filename, "r") as file:
    for i, line in enumerate(file):
        if i in (0, 1, 2, 3, 4, 5):
            continue
        if i in (525, 526):
            break
        nums = line.split()
        x[i]=float(nums[0])
        y[i]=float(nums[1])
        z[i]=float(nums[2])
        #print(x[i]," ", y[i], " ", z[i])
        if not nums:
            continue
    for i in range(6, 502, 26):
        
        r1=F1(x,y,z,i)
        r2=F2(x,y,z,i)
        #print(r1," ",r2)
        if r1>1.5*r0 and r2>1.5*r0:
            k=k+1
        r=0
    for i in range(29, 524, 26):
        
        r_1=F1(x,y,z,i)
        r_2=F2(x,y,z,i)
        #print(r_1," ",r_2)
        if r_1>1.5*r0 and r_2>1.5*r0:
            n=n+1
        r=0
    for i in range(7, 503, 26):
        #print(i)
        r_3=F2(x,y,z,i)
        print(r_3, " ")
        if r_3>1.5*r0:
            c=c+1
    for i in range(27, 522, 26):
        #print(i)
        r_4=F2(x,y,z,i)
        print(r_4)
        if r_4>1.5*r0:
            v=v+1
print("Число раскрытых доменов А1: ", n+k, "\n")
print("Число раскрытых доменов А2: ", c+v)
