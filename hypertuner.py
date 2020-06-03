

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
printf("from here doe,,,,,")
"""
"import os
if (acc_in_float < 0.80 or val_acc_in_float < 0.80):
    print("altering model")
    new_file_content=""
    reading_file=open("/root/model/model.py",'r')
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("#addlayerhere","top_model = Dense(100, activation='relu')(top_model)")
        new_file_content += new_line + "\n"
        reading_file.close()  
    writing_file = open("/root/model/model.py",'w')
    writing_file.write(new_file_content)
    writing_file.close()
    os.system("sed -ie 's/lr_x=0.001/lr_x=print(round(random.uniform(0.001,0.1),4))/g' /root/model/model.py")
else:
    print("best model has already been created")
 """   
  afile.close()  
  bfile.close()
  

