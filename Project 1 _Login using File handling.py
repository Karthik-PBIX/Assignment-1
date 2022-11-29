ac = []
ad = []
def getoption():
    print('Press 1 for Registration \nPress 2 for Login \nPress 3 for Forgot Password')
    opt = int(input())
    return opt

def countindex(sym, string1):
    count = 0
    list1 = []
    for i in range(0, len(string1)):
        if string1[i] == sym:
            count += 1
            list1.append(i)
    return count, list1

def registration_username():
    print('Enter your E-Mail id / User Name')
    username = input()
    c, d = countindex('@', username)
    e, f = countindex('.', username)
    diff = f[0] - d[0]
    firstchar = username[0].isalpha()
    if c > 1 or e > 1 or diff <= 1 or d[0] == 0 or firstchar == False:
        print('Enter correct email id')
    else:
        return username

def registration_password():
    print('Enter your Password')
    print('Your password length should be min of 6 and max of 15.')
    print('It should have one special character \none digit \none uppercase \none lowercase character')
    password = input()
    numcount = 0
    uppercount = 0
    lowercount = 0
    specialcount = 0
    for i in password:
        if i.isnumeric():
            numcount += 1
        elif i.isupper():
            uppercount += 1
        elif i.islower():
            lowercount += 1
        else:
            specialcount += 1
    if len(password) <= 5 or len(password) >= 16 or numcount == 0 or uppercount == 0 or lowercount == 0 or specialcount == 0:
        print('Invalid Password. Enter password as per the instruction')
    else:
        return password
def unamepworddict():
    file = open('Accessdetails_final.txt', 'a')
    file.close()
    file = open('Accessdetails_final.txt', 'r')
    for i in file:
        aa, ab = i.split(',')
        ab = ab.strip()
        if aa not in ac:
            ac.append(aa)
            ad.append(ab)
    data = dict(zip(ac, ad))
    return data, ac, ad

def unamepwordlist(uname, unamelist):
    if uname in unamelist:
        print('Username exists already. Please login')
    else:
        file = open('Accessdetails_final.txt', 'a')
        file.write(uname + "," + pword + '\n')
        file.close()

def login(unamelist,data):
    print('Enter your username')
    login_uname = input()

    if login_uname not in unamelist:
        print('Username does not exits. Please Register')
    else:
        print('Enter your password')
        login_pword = input()
        dict_value = data.get(login_uname)
        if dict_value == login_pword:
            print('login success')
        else:
            print('You have entered wrong password. To login Press 1 to enter username and password again \npress 2 if your forget password')
            optionlogin = int(input())
            if optionlogin == 1:
                login(unamelist, data)
            else:
                dictvalue, unamelist, pwordlist = unamepworddict()
                username_forgot(dictvalue, unamelist, pwordlist)

def username_forgot(data, ac, ad):
    print('enter your username')
    username_forgot = input()
    if username_forgot not in ac:
        print('id not available')
    else:
        print('press 1 to retrieve password \npress 2 to reset password')
        option1 = int(input())
        if option1 == 1:
            dict_value1 = data.get(username_forgot)
            print(dict_value1)
        else:
            newpassword = registration_password()
            dictvalue[username_forgot] = newpassword
            listindex = ac.index(username_forgot)
            ad[listindex] = newpassword
            file = open('Accessdetails_final.txt', 'w')
            for i in range(0, len(ac)):
                file.write(ac[i] + "," + ad[i] + '\n')
            file.close()



option = getoption()

if option == 1:
    uname = ''
    uname = registration_username()
    if uname != None:
        pword = ''
        pword = registration_password()
        if pword != None:
            dictvalue, unamelist, pwordlist = unamepworddict()
            unamepwordlist(uname, unamelist)
            dictvalue, unamelist, pwordlist = unamepworddict()

elif option == 2:
    dictvalue, unamelist, pwordlist = unamepworddict()
    login(unamelist, dictvalue)

else:
    dictvalue, unamelist, pwordlist = unamepworddict()
    username_forgot(dictvalue, unamelist, pwordlist)