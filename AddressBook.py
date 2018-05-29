dict1 = {'Daniel':'1000', 'Lucy':'1001', 'Haha':'1002'}
while 1:
    print('-Welcome to book program-\n'+'-1:Find contact number-\n'+'-2:Add new contact-\n'+'-3:Delete contact-\n'+'-4:Edit Contact-\n'+'-5:Exit')
    n = int(input("Enter the instruction:"))
    if n==1:
        name = input("Enter contact name:")
        if name in dict1:
            print(name+':'+dict1[name])
        else:
            print(name + ' is not exist')
    elif n==2:
        name = input("Enter new contact name:")
        num = input("Enter new contact num:")
        dict1[name] = num
    elif n==3:
        name = input("Enter delete name:")
        del dict1[name]
        print(name+' is moved')
    elif n==4:
        name = input("Enter contact name:")
        if name in dict1:
            print('The contact is exist -->> '+name+' : '+dict1[name])
            q = input('Edit contact info\(YES\\NO\)?')
            if q=='YES':
                num = input('Enter new num:')
                dict1[name] = num
        else:
            print(name + ' is not exist')
    elif n==5:
        break
    else:
         n = int(input("Re-Enter the instruction:"))

        
