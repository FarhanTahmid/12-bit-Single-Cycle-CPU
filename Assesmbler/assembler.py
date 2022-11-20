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
    for i in range (len(ls1)):
        if(ls1[i]==''):
            continue
        elif i==0:
            print(opCodeDict[ls1[i]])
        elif i==2:
            try:
                 if(int(ls1[i])<=9 or int(ls1[i])>=0):
                    print(f'{int(ls1[i]):04b}')
            except:
                print(register_code_Dict[ls1[i]])
        else:
            print(register_code_Dict[ls1[i]])