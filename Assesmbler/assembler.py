import re


def findTwoscomplement(str):
    n = len(str)

    # Traverse the string to get first

    # '1' from the last of string

    i = n - 1

    while (i >= 0):

        if (str[i] == '1'):
            break

        i -= 1

    # If there exists no '1' concatenate 1

    # at the starting of string

    if (i == -1):
        return '1' + str

    # Continue traversal after the

    # position of first '1'

    k = i - 1

    while (k >= 0):

        # Just flip the values

        if (str[k] == '1'):

            str = list(str)

            str[k] = '0'

            str = ''.join(str)

        else:

            str = list(str)

            str[k] = '1'

            str = ''.join(str)

        k -= 1

    # return the modified string

    return str


opCodeDict={
        'Add':'0000','Addi':'0001','Sub':'0010','And':'0011',
        'Or':'0100','Sll':'0101','Srl':'0110','Lw':'0111',
        'Sw':'1000','Beq':'1001','Bne':'1010','J':'1011','Slt':'1100',
        'Slti':'1101','NAND':'1110','NOR':'1111'
    }

register_code_Dict={
        '$zero':'0000','$s0':'0001','$s1':'0010','$s2':'0011',
        '$s3':'0100','$s4':'0101','$s5':'0110','$s6':'0111','$s7':'1000',
         '$t0':'1001','$t1':'1010','$t2':'1011','$t3':'1100','$t4':'1101',
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
    hexaDecimalNum=format(decimalNum,'x')
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
                    outputFile.write(binToHexa(opCodeDict[ls1[i]]))
                    outputFile.write(
                        binToHexa(register_code_Dict[ls1[i+1]]))
                    if (int(ls1[i+2]) <= 15):
                        number = f'{int(ls1[i+2]):04b}'
                        outputFile.write(binToHexa(number))
                    else:
                        outputFile.write("Insufficient bits!")        
                    break
                    
                elif i==0:
                    outputFile.write(binToHexa(opCodeDict[ls1[i]]))

                elif i==1:
                    try:
                        if(int(ls1[1])<=255 or int(ls1[1])>=0):
                            number=f'{int(ls1[i]):08b}'
                            outputFile.write(binToHexa(number))
                            break
                        if (int(ls1[i] < 0)):
                            print(ls1[1])
                            number = f'{(int(ls1[i])*(-1)):08b}'

                            twosComp = findTwoscomplement(str(number))
                            outputFile.write(binToHexa(twosComp))
                            break
                    except:
                        outputFile.write(binToHexa(register_code_Dict[ls1[i]]))

                elif i==2:
                    try:
                        if(int(ls1[i])<=9 or int(ls1[i])>=0):
                            number=f'{int(ls1[i]):04b}'
                            outputFile.write(binToHexa(number))
                    except:
                        outputFile.write(binToHexa(register_code_Dict[ls1[i]]))
                else:
                    outputFile.write(binToHexa(register_code_Dict[ls1[i]]))
        outputFile.write('\n')
    except:
         outputFile.write("Sorry An Unexpected Instructuion found which is not in our instruction sets!")    
outputFile.close()