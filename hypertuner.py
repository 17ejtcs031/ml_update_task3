

#taking the value of accuracy and val_accuracy file

str1 = ""
af=open('/root/model/accuracy.txt','r') 
    for line in af:
        str1 = line
af.close()
      
acc_in_float=float(str1)
str2 = ""
vf=open('/root/model/val_accuracy.txt','r') 
    for line in bfile:
        str2 = line
vf.close()       
val_acc_in_float=float(str2)     
printf("from here doe")
