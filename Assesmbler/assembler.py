import re
def get_Machine_Value_Of_OpCodes():
    opCodeDict={
        'Add':'0000',
        'Addi':'0001',
        'Sub':'0010',
        'And':'0011', 'Or':'0100','Sll':'0101','Srl':'0110','Lw':'0111','Sw':'1000','Beq':'1001','Bne':'1010','J':'1011','Slt':'1100','Slti':'1101','In':'1110','Out':'1111'
    }

def get_Machine_Register_Codes():
    register_code_Dict={
        '$zero':'0000','$s0':'0001','$s1':'0010','$s2':'0011','$s3':'0100','$s4':'0101','$s5':'0110','$s6':'0111','$s7':'1000','$t0':'1001','$t1':'1010','$t2':'1011','$t3':'1100','$t4':'1101',
        '$t5':'1110','$t6':'1111'
    }
with open("input_file.txt",'r') as data_file:
    for line in data_file:
        data=re.split(', |\n| ',line)
        data.append(data)
