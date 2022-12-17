import re

opCodeDict={
        'Add':'0000',
        'Addi':'0001',
        'Sub':'0010',
        'And':'0011', 'Or':'0100','Sll':'0101','Srl':'0110','Lw':'0111','Sw':'1000','Beq':'1001','Bne':'1010','J':'1011','Slt':'1100','Slti':'1101','In':'1110','Out':'1111'
    }

register_code_Dict={
        '$zero':'0000','$s0':'0001','$s1':'0010','$s2':'0011','$s3':'0100','$s4':'0101','$s5':'0110','$s6':'0111','$s7':'1000','$t0':'1001','$t1':'1010','$t2':'1011','$t3':'1100','$t4':'1101',
        '$t5':'1110','$t6':'1111'
    }
datas=[]
with open("input_file.txt",'r') as data_file:
    for line in data_file:
        data=re.split(', |\n| ',line)
        datas.append(data)
for ls1 in datas:
    if(ls1[-1]==""):
        ls1.pop()

#Open output file
# Append-adds at last
outputFile = open("outputfile.txt", "a")

def binToHexa(binaryNumber):
    decimalNum=int(binaryNumber,2)
    hexaDecimalNum=hex(decimalNum)
    return(hexaDecimalNum)


for ls1 in datas:
    try:
        try:
            if((int(ls1[-1])>15 or int(ls1[-1])<0) and (ls1[i]=='Lw' or ls1[i]=='Sw')):
                outputFile.write("Cant store a number bigger than 15!\n")
                continue
        except:
            pass
        if(len(ls1)>3):
            outputFile.write("Can not execute command, Not enough registers assigned!\n")
        else:
            for i in range (len(ls1)):
                if(ls1[i]==''):
                    continue
                elif (ls1[i] == 'Lw' or ls1[i] == 'Sw'):
                    outputFile.write(binToHexa(opCodeDict[ls1[i]])+" ")
                    outputFile.write(
                        binToHexa(register_code_Dict[ls1[i+1]])+" ")
                    if (int(ls1[i+2]) <= 15):
                        number = f'{int(ls1[i+2]):04b}'
                        outputFile.write(binToHexa(number))
                    else:
                        outputFile.write("Insufficient bits!")        
                    break
                    
                elif i==0:
                    outputFile.write(binToHexa(opCodeDict[ls1[i]])+" ")
                elif i==2:
                    try:
                        if(int(ls1[i])<=9 or int(ls1[i])>=0):
                            number=f'{int(ls1[i]):04b}'
                            outputFile.write(binToHexa(number)+" ")
                    except:
                        outputFile.write(binToHexa(register_code_Dict[ls1[i]])+" ")
                else:
                    outputFile.write(binToHexa(register_code_Dict[ls1[i]])+" ")
        outputFile.write('\n')
    except:
         outputFile.write("Sorry An Unexpected Instructuion found which is not in our instruction sets!")    
outputFile.close()