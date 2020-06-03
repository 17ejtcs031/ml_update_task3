

#taking the value of accuracy and val_accuracy file

str1 = ""
with open('/root/model/accuracy.txt','r') as afile:
    for line in afile:
        str1 = line
      
acc_in_float=float(str1)

str2 = ""
with open('/root/model/val_accuracy.txt','r') as bfile:
    for line in bfile:
        str2 = line
bfile.close()        
val_acc_in_float=float(str2)     
printf("from here doe")
  afile.close()  
  bfile.close()
  

