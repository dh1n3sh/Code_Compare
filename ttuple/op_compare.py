
op1 = open('op1.txt','r').readlines()
op2 = open('op2.txt','r').readlines()
inp = open('inp.txt','r')
inp.readline()
for i in range(len(op1)):
    l1 = inp.readline()
    l2 = inp.readline()
    try:
        # print(i,op1[i].strip('\n'),op2[i].strip('\n'),op1[i]==op2[i])
        if op1[i] != op2[i]:
            print(i)
            print(l1.strip('\n'))
            print(l2.strip('\n'))
            print('op1 : ',op1[i].strip('\n') )
            print('op2 : ',op2[i].strip('\n') )
            break
    except Exception as ex:
        print(ex)