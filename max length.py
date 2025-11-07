import sys
import os

for m in range(5000, 21000, 1000):
    if m==1000 or m==2000 or m==5000 or m==10000 or m==20000:
        outdir = "/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
        my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".1.txt", "w")
        my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".1(excel).txt", "w") 
        for var in range(10, 100, 10):
            filename = "/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/zeros1SR="+str(m)+"_N=20/vwf00" + str(var) + ".vtk"
            max_val = None
            a=0
            b=0
            with open(filename, "r") as file:
                for i, line in enumerate(file):
                    if i in (0, 1, 2, 3, 4, 5):
                        continue
                    if i in (525, 526):
                        break
                    nums = line.split()
                
                    if not nums:
                        continue
                    
                    val_0 = float(nums[1])
                    if i==524:
                        l1=val_0
                    if max_val is None or val_0 > max_val:
                        max_val = val_0
                    if i==524:
                        a = val_0
                        b=a
            if l1 < max_val:
                l1= 320 + l1
            else:
                l1=max_val                 
            my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".1.txt", "a+")
            my_file.write(str(var/100)+" "+ str(max_val*10)+"\n")
            my_file.close()
            my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".1(excel).txt", "a+")
            my_file.write(str(max_val*10)+"\n")
            my_file.close()
        
        my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".2.txt", "w")
        my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".2(excel).txt", "w")
        for var1 in range(100, 1000, 10):
            filename = "/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/zeros1SR="+str(m)+"_N=20/vwf0" + str(var1) + ".vtk"
            max_val1 = None
            c=0
            d=0
            with open(filename, "r") as file:
                for i, line in enumerate(file):
                    if i in (0, 1, 2, 3, 4, 5):
                        continue
                    if i in (525, 526):
                        break
                    
                    nums = line.split()
                
                    if not nums:
                        continue
                    
                    val_1 = float(nums[1])
                    if i==524:
                        l2=val_1
                
                    if max_val1 is None or val_1 > max_val1:
                        max_val1 = val_1
                    
            if l2 < max_val1 and max_val1 >319:
                l2= 320 + l2
            else:
                l2=max_val1                
            my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".2.txt", "a+")
            my_file.write(str(var1/100)+" "+ str(l2*10)+"\n")
            my_file.close()
            my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".2(excel).txt", "a+")
            my_file.write(str(l2*10)+"\n")
            my_file.close()
        
        my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".3.txt", "w")
        my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".3(excel).txt", "w")
        for var2 in range(1000, 10000, 10):
            filename = "/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/zeros1SR="+str(m)+"_N=20/vwf" + str(var2) + ".vtk"
            max_val2 = None
            e=0
            f=0
            with open(filename, "r") as file:
                for i, line in enumerate(file):
                    if i in (0, 1, 2, 3, 4, 5):
                        continue
                    if i in (525, 526):
                        break
                    
                    nums = line.split()
                
                    if not nums:
                        continue
                    
                    val_2 = float(nums[1])
                    if i==524:
                        l3=val_2
                
                    if max_val2 is None or val_2 > max_val2:
                        max_val2 = val_2
                    
            if l3 < max_val2 and max_val2 >319:
                l3= 320 + l3
            else:
                l3=max_val2
            my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".3.txt", "a+")
            my_file.write(str(var2/100)+" "+ str(l3*10)+"\n")
            my_file.close()
            my_file = open("/home/ilya/diplom/ScientificSOFT/5Build_4.0.0.2/v2-new-VWF/results/out-multi-newVWF-1/Определение max значения/zeros1SR="+str(m)+"/zeros1SR="+str(m)+".3(excel).txt", "a+")
            my_file.write(str(l3*10)+"\n")
            my_file.close()
        else:
            continue
