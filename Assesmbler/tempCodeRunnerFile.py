for ls1 in datas:
#     print(ls1)
#     if(len(ls1)>2):
#         print("Can not execute command, Not enough registers assigned!")
#     else:
#         for i in range (len(ls1)):
#             if(ls1[i]==''):
#                 continue
#             elif i==0:
#                 print(opCodeDict[ls1[i]])
#             elif i==2:
#                 try:
#                     if(int(ls1[i])<=9 or int(ls1[i])>=0):
#                         print(f'{int(ls1[i]):04b}')
#                 except:
#                     print(register_code_Dict[ls1[i]])
            
#             else:
#                 print(register_code_Dict[ls1[i]])