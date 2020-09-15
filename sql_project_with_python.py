import mysql.connector
a = mysql.connector.connect(host="localhost", user="root", password="a1234")
b = a.cursor()
b.execute("use practicle")
# b.execute("update stem set selling_price=cost_price+cost_price*0.10 where selling_price is NULL")
# a.commit()
b.execute("select *from stem")
res = b.fetchall()
for i in res:
    print(i)

# admin display


def admin():
    print()
    print()
    print()
    print()
    while True:
        print()
        print()
        print("*********************************************KEYS TO PERFORM AN ACTION****************************************************")
        print()
        print()
        print("press 1 ---------------------------> Display")
        print("press 2 ---------------------------> Update")
        print("press 3 ---------------------------> Add")
        print("press 4 ---------------------------> Add New Admin")
        print("press 5 ---------------------------> Total  Sales Of a Day")
        print("press 6 ---------------------------> Logout")
        print()
        print()
        print("***************************************************************************************************************************")
        print()
        print()
        choice = int(input("select any key to move forward"))
        if(choice == 1):
            display()
        elif(choice == 2):
            update()
        elif(choice == 3):
            add()
        elif(choice == 4):
            new()
        elif(choice == 5):
            date()
        elif(choice == 6):
            logout()
        else:
            print("SORRY,you have entered wrong key")
        again = (input("do you want again perform a operations"))
        if(again == "y"):
            continue
        else:
            break
    print()


# add welcome
def added():
    print()
    print()
    print("*****************************************************************************************")
    print()
    print()
    print(" **       **       ** *******  **       ******   *****     **     **  ******         ")
    print("  **     ****     **  **       **      **      **     **  ** ** ** ** **           ")
    print("   **   **  **   **   *******  **      **      **     **  **  **   ** ******      ")
    print("    ** **    ** **    **       **      **      **     **  **       ** **         ")
    print("     **       **      *******  *******  ******   *****    **       ** ******             ")
    print()
    print()
    print("*****************************************************************************************")
    print()
    print()

# user display


def display():
    print()
    print()
    print("************************************DISPLAY*****************************************************")
    print()
    print()
    b.execute("select * from stem")
    print()
    print()
    print()
    print()
    h = b.fetchall()
    a = ['Product Id', 'Product Name', 'product company',
         'Stock Available', 'selling Price', 'cost price']
    for i in h:
        for j in range(0, len(h)):
            print(a[j], ":", i[j])
        print()
    print()
    print()
    print()
    print("*****************************************************************************************")
    print()
    print()
    admin()


# user update
def update():
    print()
    print()
    print("*********************UPDATE*******************")
    print()
    print()
    ans1 = (input("do you want to update? y or n"))
    if(ans1 == 'y' or ans1 == 'y'):
        u_id = int(input("enter the product id"))
        up = int(input("enter the update stock"))
        v1 = ("update stem set stock=stock+ %s where product_id= %s")
        v2 = (up, u_id)
        b.execute(v1, v2,)
        a.commit()
    else:
        print("no update")
    print()
    print()
    print()
    print()
    print("*****************************************************************************************")
    print()
    print()
    admin()


# add new products
def add():
    print()
    print()
    print("*********************ADD NEW DATA*******************")
    print()
    print()
    ans = input("do you want to add?")
    if(ans == 'y' or ans == 'Y'):
        p = int(input("enter the id :"))
        q = input("enter the name of product:")
        r = input("enter the campany:")
        r1 = int(input("enter stock: "))
        s = int(input("enter the cost price:"))
        n1 = "insert into stem(product_id,product_name,product_company,stock,cost_price) values(%s,%s,%s,%s,%s)"
        n2 = (p, q, r, r1, s)
        b.execute(n1, n2,)
    else:
        print("no update")
    print()
    print()
    print()
    print("*************************************************************************************************")
    print()
    print()
    a.commit()
    admin()


def date():  # print data from date
    print()
    print()
    print()
    print("***************************************DISPLAY DATA ON CHART**********************************************************")
    print()
    print()

    b.execute("select * from date")
    h = b.fetchall()
    for i in h:
        print(i)
    kl = []
    lk = []
    b.execute("select date from date")
    k = b.fetchall()
    for i in k:
        kl.append(i[0])
    print(kl)
    b.execute("select total from date")
    l = b.fetchall()
    for i in l:
        lk.append(i[0])
    print(lk)
    x = kl
    y = lk
    from matplotlib import pyplot as p
    p.bar(x, y, color="red")
    p.xlabel("total sale")
    p.ylabel("date")
    p.title("sale of day")
    p.show()
    print()
    print()
    print()
    print("************************************************************************************************************************")
    print()
    print()
    admin()


def date1(t):  # insert data on date

    import mysql.connector
    a = mysql.connector.connect(
        host="localhost", user='root', password="a1234")
    b = a.cursor()
    b.execute("use practicle")

    from datetime import date
    day = date.today()
    print(day)

    # print("today",day)
    b.execute("select date from date where date ='%s'" % (day))
    h = b.fetchall()
    if h == []:
        #print("date is not avilabe........you can insert")
        ab = "insert into date(date,total)values(%s,%s)"
        ba = (day, t)
        b.execute(ab, ba)
        a.commit()

    else:
        abt = "update date set total=(total+%s) where date =%s"
        bat = (t, day)
        b.execute(abt, bat)
        a.commit()



def new():
    print()
    print()
    print()
    print("*******************************************ADDITION OF NEW ADMIN******************************************************")
    print()
    print()
    f = open("user.txt", "a")
    user = input("enter new user name")
    password = input("enter the password")
    f.writelines(["\n", user, ",", password])
    f.close()
    print()
    print()
    print()
    print("*************************************************************************************************")
    print()
    print()


# user logout
def logout():
    print()
    print()
    print()
    print("*****************************************************************************************")
    print()
    print()
    print("you are logout from admin")
    print()
    print()
    print("**************************************************************************************************")
    main()

 # **************************************guest*****************************************************
 # guest


def guest():
    print()
    print()
    print()
    print("*****************************************GUEST LOGIN PAGE************************************************")
    print()
    print()
    while True:
        print("press 1 for display")
        print("press 2 for purchase")
        print("press 3 for carts")
        print("press 4 for returns")
        print("press 5 for billing")
        print("press 6 for logout ")
        print()
        print()
        print()
        print("*******************************************************************************************************")
        print()
        print()
        choices = int(input("enter your choice to perform an action :\n"))
        if(choices == 1):
            g_display()
        elif(choices == 2):
            g_purchase()
        elif(choices == 3):
            carts()
        elif(choices == 4):
            returns()
        elif(choices == 5):
            bill()
        elif(choices == 6):
            g_logout()
        else:
            print("SORRY,you have entered wrong key")
        agains = (input("do you want again perform a operations"))
        if(agains == "y"):
            continue
        else:
            break
    print()
    print()
    print()
    print("***************************************************************************************************")
    print()
    print()


# guest display
def g_display():
    import mysql.connector
    a = mysql.connector.connect(
        host="localhost", user="root", password="a1234")
    b = a.cursor()
    b.execute("use practicle")
    b.execute(
        "select product_id,product_name,product_company,stock,selling_price from stem")
    h = b.fetchall()
    print()
    print()
    print("*********************DISPLAY PAGE*******************")
    print()
    print()
    a = ['Product Id', 'Product Name', 'product company',
         'Stock Available', 'Selling price']
    for i in h:
        for j in range(0, len(a)):
            print(a[j], ":", i[j])
        print()
    print()
    print()
    print()
    print("**********************************************************************************************************")
    print()
    print()
    guest()


# purchase
def g_purchase():
    import mysql.connector
    a = mysql.connector.connect(
        host="localhost", user="root", password="a1234")
    b = a.cursor()
    b.execute("use practicle")

    print()
    print()
    print("*********************PURCHASE*******************")
    print()
    print()
    while True:
        code = int(input("enter the id of product which you want to buy"))
        b.execute(
            "select selling_price from stem where product_id='%s'" % (code))
        cd = list(b.fetchone())
        cd1 = cd
        number = int(input("enter the quantity you need"))
        date1(number)
        a1 = ("select * from stem where product_id = %s ")
        a2 = (code,)
        b.execute(a1, a2,)
        data = b.fetchone()
        if(data == []):
            print("not any id match,try again")
        else:
            print(number, code)
            b1 = ("select * from carts where id='%s'")
            b2 = (code,)
            b.execute(b1, b2,)
            res = b.fetchall()
            # print(res)
            if(res == []):
                k1 = ("select stock from stem where product_id='%s' ")
                k2 = (code,)
                b.execute(k1, k2)
                total = b.fetchone()
                for i in total:
                    if(i < number):
                        print("sorry ,we have less present")
                    else:
                        #print("flow in else ")
                        print(number)
                        print(code)
                        # b.execute("update stem set stock=stock - '%s' where stem.product_id='%s'" %(number,code))

                        up = "update stem set stock=stock - %s where stem.product_id=%s"
                        dation = (number, code,)
                        b.execute(up, dation)
                        #print("running ................")

                        print(
                            "the quantity of the product you enter is added")
                        order(code, number)
                        asd = ("update carts set total=%s*%s where id='%s'")
                        bs = (cd1, number, code)
                        b.execute(asd, bs)
                        a.commit()
            else:

                b.execute(
                    "select stock from stem where product_id='%s'" % (code))
                se = b.fetchone()
                for i in se:
                    print(i)
                    if number > i:
                        print("enter valid quantity we have less stock  ")
                    else:
                        a1 = "update carts set quantity=quantity + %s where carts.id=%s"
                        a2 = (number, code)
                        b.execute(a1, a2)
                        print("your purched item will be updated ")
                a.commit()
            agains = (input("do you want again perform a operations"))
            if(agains == "y"):
                continue
            else:
                print(
                    "********************THANKS FOR SHIPPING***************************")
                break


# order
def order(code, number):
    sql = "insert into carts(id,quantity) values(%s,%s)"
    v = (code, number)
    b.execute(sql, v)
    a.commit()

# carts


def carts():
    sum=0
    print()
    print()
    print("************************************CARTS***********************************************************")
    print()
    print()
    b.execute("select * from carts")
    h = b.fetchall()
    for i in h:
        print(i)
    a.commit()
    print()
    print()
    print()
    print("***********************************************************************************************************")
    print()
    print()
    guest()


# returns of products from carts
def returns():
    print()
    print()
    print("*********************RETURN PRODUCT*******************")
    print()
    print()
    re = int(input("enter the product code which you want to return"))
    print("re", re)
    d = ("delete from carts where id= '%s' ")
    t = (re,)
    b.execute(d, t)
    a.commit()
    print("your product had been return")
    print()
    print()
    print("************************************************************************************************************")
    print()
    print()
    guest()


# bill pay
def bill():
    print()
    print()
    print()
    print("*********************************************BILL***********************************************************")
    print()
    print()
    import mysql.connector
    a = mysql.connector.connect(
        host="localhost", user="root", password="a1234")
    b = a.cursor()
    b.execute("use net")
    k = 0
    while True:
        print("do you want to pay for product")
        req = (input("press y or n"))
        if(req == 'y'):
            print("enter your product id for billing")
            id = int(int(input("?")))
            it = ("select total from carts where id ='%s' ")
            td = (id,)
            print(td)
            b.execute(it, td)
            ha = list(b.fetchall())
            k = k+sum(ha)
            print("your total bill is", k)
            de = ("delete from carts where id = '%s'")
            le = (id,)
            b.execute(de, le)
            print("billing done")
            print()
            print()
            a.commit()
            print("do want to pay for another product?")
            requ = (input("press y or n"))
            if(requ == "y"):
                continue
            else:
                print("thanku for shipping")
            guest()

        else:
            print("see you next time")
            guest()
            print()
    print()
    print()
    print("*************************************************************************************************")
    print()
    print()


# logout()
def g_logout():
    print()
    print()
    print("*************************************************************************************************")
    print()
    print()
    print("you are logout from guest")
    print()
    print()
    print("**************************************************************************************************")
    main()


# main def
def main():
    user = (input("your are admin or guest otherwise press any key to go out?"))
    res = False
    if(user == "admin"):
        for i in range(0, 3):
            names = input("enter your name : ")
            password = input("plz enter your password : ")
            with open("user.txt", "r") as f:
                for i in f:
                    u, p = i.split(",")
                    p = p.strip()
                    if(names == u and password == p):
                        res = True
                        break
                if(res == True):
                    added()
                    admin()
                else:
                    print("sorry entered password is wrong plz try again")
        print('do you want to reset your password?')
        ne = input("y or n")
        if(ne == 'y'):
            print("rest your password")
            u = input("enter your user name")
            p = input("enter your new password : ")
            retype = input("enter again new password : ")
            if(p == retype):
                f = open("user.txt", "w")
                f.writelines(u)
                p = "\n"+p
                f.writelines(p)
                f.close()
                admin()

            else:
                print("retype again")

    elif(user == "guest"):
        name = input("enter your name")
        added()
        guest()
    else:
        print("thanku for visit")


main()
