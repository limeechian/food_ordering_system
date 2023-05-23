# LIM EE CHIAN
# TP065138

# admin help customer top up account balance
def admin_topup_customer_account_balance():
    balanceRecs = []
    fh = open("C:\Temp\Data Files\Account Balance.txt","r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        balanceRecs.append(reclist)
    fh.close()

    customer_id = ""
    while True:
        if customer_id == "E":
            break

        while True:
            customer_id = input("Enter Customer ID to top up account balance, or 'E' to Exit: ").upper()
            if customer_id == "E":
                break

            # validate Customer ID
            currRecIndex = -1
            customer_id_exist = False
            for recIndex in range(1,len(balanceRecs)):
                if balanceRecs[recIndex][0] == customer_id:
                    account_balance = balanceRecs[recIndex][1]
                    print(customer_id + "-" + account_balance)
                    customer_id_exist = True
                    currRecIndex = recIndex
                    break

            if customer_id_exist == False:
                print("Invalid Customer ID! Please try again.")
                break

            else:
                topup_amount = input("Enter the top up amount, or 'E' to Exit: ").upper()
                if topup_amount == "E":
                    break

                account_balance = balanceRecs[currRecIndex][1]
                new_account_balance = int(account_balance) + int(topup_amount)
                balanceRecs[currRecIndex][1] = str(new_account_balance)
                print("Top up successfully! New account balance: ",str(new_account_balance))


    # write new account balance to file
    fh = open("C:\Temp\Data Files\Account Balance.txt","w")
    for balanceRec in balanceRecs:
        rec = ":".join(balanceRec) + '\n'
        fh.write(rec)
    fh.close()


#admin add delivery staff
def admin_add_delivery_staff():
    new_staffid = input("Enter a new staff id (Ex.D000): ").upper()
    new_staffname = input("Enter new staff name: ")
    staffpw = new_staffname + new_staffid
    fh = open("C:\Temp\Data Files\Delivery Staff.txt", "a")
    fh.write("\n" + new_staffid + ":" + new_staffname + ":" + staffpw)
    fh.close()

# admin modify, delete Delivery Staff
def admin_mod_del_delivery_staff():
    deliverRecs = []
    fh = open("C:\Temp\Data Files\Delivery Staff.txt", "r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        deliverRecs.append(reclist)
    fh.close()

    delivery_id = ""
    while True:
        if delivery_id == "E":
            break

        while True:
            delivery_id = input("Enter Delivery ID or 'E' to Exit: ").upper()
            if delivery_id == "E":
                break

            # validate delivery id
            currRecIndex = -1
            delivery_id_exist = False
            for recIndex in range(1,len(deliverRecs)):
                if deliverRecs[recIndex][0] == delivery_id:
                    delivery_name = deliverRecs[recIndex][1]
                    delivery_password = deliverRecs[recIndex][2]
                    print(delivery_id + "-" + delivery_name + "-" + delivery_password)
                    delivery_id_exist = True
                    currRecIndex = recIndex
                    break

            if delivery_id_exist == False:
                print("Invalid delivery ID! Please try again.")
                break

            mod_del = input("Enter 'M' to modify or 'D' to Delete or 'E' to cancel: ").upper()
            if mod_del == "M":
                delivery_name = input("Enter the delivery staff name: ")
                delivery_password = input("Enter the delivery staff password: ")
                deliverRecs[currRecIndex][1] = delivery_name
                deliverRecs[currRecIndex][2] = delivery_password
                deliverRec = [delivery_id,delivery_name,delivery_password]
                print(deliverRec)

            elif mod_del == "D":
                deliverRecs.remove(deliverRecs[currRecIndex])
                print("Deleted.")
                break

            else:
                break

    #write delivery staff details to file
    fh = open("C:\Temp\Data Files\Delivery Staff.txt","w")
    for deliverRec in deliverRecs:
        rec = ":".join(deliverRec) + "\n"
        fh.write(rec)
    fh.close()

# admin search and display specific records of Delivery Staff
def view_specific_delivery_staff():
    fh = open("C:\Temp\Data Files\Delivery Staff.txt","r")
    deliverRecs = []
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        deliverRecs.append(reclist)
    fh.close()

    delivery_id = ""
    while True:
        if delivery_id == "E":
            break

        while True:
            delivery_id = input("Enter Delivery ID to view delivery staff, or 'E' to Exit: ").upper()
            if delivery_id == "E":
                break

            #validate Delivery ID
            delivery_id_exist = False
            for recIndex in range(1, len(deliverRecs)):
                if deliverRecs[recIndex][0] == delivery_id:
                    delivery_name = deliverRecs[recIndex][1]
                    delivery_password = deliverRecs[recIndex][2]
                    print(delivery_id + "-" + delivery_name + "-" + delivery_password)
                    delivery_id_exist = True

            if delivery_id_exist == False:
                print("Invalid Delivery ID! Please try again.")
                break

# admin assign order to delivery staff
def admin_assign_order():
    deliStatRecs = []
    recIndex = []
    fh = open("C:\Temp\Data Files\Delivery Status.txt", "r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        deliStatRecs.append(reclist)
    fh.close()

    view_status = ""
    while True:
        if view_status == "E":
            break

        while True:
            print('''Please enter 1/2/E to perform action:
    1. View not assigned orders
    2. View others (assigned/delivering/delivered orders)
    E. Exit
            ''')
            view_status = input("Please perform an action: ")
            if view_status == "E":
                break

            #find not assigned or others
            for recIndex in range(1,len(deliStatRecs)):
                order_id = deliStatRecs[recIndex][0]
                address = deliStatRecs[recIndex][1]
                delivery_id = deliStatRecs[recIndex][2]
                delivery_status = deliStatRecs[recIndex][3]

                if view_status == "1":
                    if delivery_status == "not assigned":
                        print(order_id,"-",address,"-",delivery_id,"-",delivery_status)

                elif view_status == "2":
                    if delivery_status != "not assigned":
                        print(order_id,"-",address,"-",delivery_id,"-",delivery_status)

            if view_status == "2" :
                break

            # start to assign order
            order_id = ""
            while True:
                if order_id == "E":
                    break

                while True:
                    order_id = input("Enter Order ID to assign order & modify it's delivery status, or 'E' to Exit: ").upper()
                    if order_id == "E":
                        break

                    #validate order_id
                    order_id_exist = False
                    for recIndex in range(1,len(deliStatRecs)):
                        if deliStatRecs[recIndex][0] == order_id:
                            order_id_exist = True
                            break

                    if order_id_exist == True:
                        delivery_id = input("Enter the Delivery ID of the delivery staff you want to assign the order to: ").upper()
                        deliStatRecs[recIndex][2] = delivery_id
                        deliStatRecs[recIndex][3] = "assigned"
                        print(deliStatRecs[recIndex])
                        break

                    else:
                        print("Invalid Order ID! Please try again.")
                        break

            # write delivery status to file
            fh = open("C:\Temp\Data Files\Delivery Status.txt", "w")
            for assignedRec in deliStatRecs:
                rec = ":".join(assignedRec) + "\n"
                fh.write(rec)
            fh.close()

# delivery staff update his delivery status
def delivery_staff_update_delivery_status():
    deliStatRecs = []
    recIndex = []
    fh = open("C:\Temp\Data Files\Delivery Status.txt", "r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        deliStatRecs.append(reclist)
    fh.close()

    view_status = ""
    while True:
        if view_status == "E":
            break

        while True:
            delivery_id = input("Enter your Delivery ID: ").upper()
            view_status = input("Enter '1' to view assigned & delivering orders, or Enter 'E' to Exit: ").upper()

            if view_status == "E":
                break

            # find assigned and delivering order
            found_delivery_id = False
            for recIndex in range(1,len(deliStatRecs)):
                order_id = deliStatRecs[recIndex][0]
                address = deliStatRecs[recIndex][1]
                delivery_status = deliStatRecs[recIndex][3]

                if view_status == "1":
                    if delivery_id == deliStatRecs[recIndex][2]:
                        if delivery_status in ["assigned","delivering"]:
                            print(order_id,"-",address,"-",delivery_id,"-",delivery_status)
                            found_delivery_id = True

            if found_delivery_id == False:
                print("Delivery ID not found.")
                break

            # start to assign order
            order_id = ""
            while True:
                if order_id == "E":
                    break

                while True:
                    order_id = input("Enter Order ID to modify your delivery status, or 'E' to Exit: ").upper()
                    if order_id == "E":
                        break

                    # validate order_id
                    order_id_exist = False
                    for recIndex in range(1, len(deliStatRecs)):
                        if deliStatRecs[recIndex][0] == order_id:
                            order_id_exist = True
                            break

                    if order_id_exist == True:
                        delivery_status = input("Enter '1' to start delivering, Enter '2' when the order has been delivered: ")
                        deliStatRecs[recIndex][2] = delivery_id

                        if delivery_status == "1":
                            deliStatRecs[recIndex][3] = "delivering"

                        elif delivery_status == "2":
                            deliStatRecs[recIndex][3] = "delivered"

                        print(deliStatRecs[recIndex])
                        break

                    else:
                        print("Invalid Order ID! Please try again.")
                        break

            # write delivery status to file
            fh = open("C:\Temp\Data Files\Delivery Status.txt", "w")
            for assignedRec in deliStatRecs:
                rec = ":".join(assignedRec) + "\n"
                fh.write(rec)
            fh.close()

# admin access food item category wise - add if food item not found, modify, delete
def admin_add_mod_del_food_item():
    print('''Select the following category code, then Enter new item code to add new item, or Enter existing item code to modify or delete.
        C01: rice
        C02: noodle
        C03: snack 
        C04: dessert
        C05: drink
        ''')
    foodRecs = []
    fh = open("C:\Temp\Data Files\Food.txt","r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        foodRecs.append(reclist)
    fh.close()

    categoryCode = ""
    foodCategory = ""
    while True:
        if categoryCode == "E":
            break

        while True:
            categoryCode = input("Enter Category Code or 'E' to Exit: ").upper()
            if categoryCode == "E":
                break

            #validate category code
            category_code_exist = False
            for recIndex in range(1,len(foodRecs)):
                if foodRecs[recIndex][0] == categoryCode:
                    foodCategory = foodRecs[recIndex][1]
                    print(categoryCode + "-" + foodCategory)
                    category_code_exist = True
                    break
            if category_code_exist == False:
                print("Invalid category code! Please try again.")
                break

            itemCode = ""
            while True:
                if (itemCode == "E"):
                    break

                while True:
                    itemCode = input("Enter Item Code or 'E' to exit: ").upper()
                    if (itemCode == "E"):
                        break

                    # validate item code
                    currRecIndex = -1
                    item_code_exist = False
                    for recIndex in range(1,len(foodRecs)):
                        if foodRecs[recIndex][2] == itemCode:
                            item_code_exist = True
                            currRecIndex = recIndex
                            break

                    if item_code_exist == True :
                        mod_del = input("Enter 'M' to modify or 'D' to Delete or 'E' to cancel: ").upper()
                        if mod_del == "M":
                            recStatus = "M"
                        elif mod_del == "D":
                            recStatus = "D"
                            foodRecs.remove(foodRecs[currRecIndex])
                            print("Deleted")
                            break
                        else :
                            break

                    else :
                        recStatus = "N"

                    foodItem = input("Please enter the name of the new food item: ").lower()
                    price = input("Please enter the price of the new food item: ")

                    if recStatus == "N" :
                        foodRec = [categoryCode,foodCategory,itemCode,foodItem,price]
                        foodRecs.append(foodRec)
                        print(foodRec)
                    else :
                        foodRecs[currRecIndex][3] = foodItem
                        foodRecs[currRecIndex][4] = price
                        print(foodRecs[currRecIndex])

    #write food records to file
    fh = open("C:\Temp\Data Files\Food.txt","w")
    for foodRec in foodRecs:
        rec = ":".join(foodRec) + "\n"
        fh.write(rec)
    fh.close()


# autogenerate customerID
def customerID():
    reclist = []
    newID = ""
    with open ("C:\Temp\Data Files\Customer ID.txt","r") as fh:
        rec = fh.read()
        reclist = rec.split()
        oldID = reclist[0]
        numericPart = str((int(oldID[2:]) + 1))
    if (len(numericPart) == 1):
        newID = "CX000" + numericPart
    elif (len(numericPart) == 2):
        newID = "CX00" + numericPart
    elif (len(numericPart) == 3):
        newID = "CX0" + numericPart
    elif (len(numericPart) == 4):
        newID = "CX" + numericPart
    reclist = newID
    fh = open("C:\Temp\Data Files\Customer ID.txt","w")
    fh.write(reclist)
    return newID


# autogenerate orderID
def orderID():
    reclist = []
    newID = ""
    with open("C:\Temp\Data Files\Order ID.txt","r") as fh:
        rec = fh.read()
        reclist = rec.split()
        oldID = reclist[0]
        numericPart = str((int(oldID[2:]) + 1))
    if (len(numericPart) == 1):
        newID = "AX000" + numericPart
    elif (len(numericPart) == 2):
        newID = "AX00" + numericPart
    elif (len(numericPart) == 3):
        newID = "AX0" + numericPart
    elif (len(numericPart) == 4):
        newID = "AX" + numericPart
    reclist = newID
    fh = open("C:\Temp\Data Files\Order ID.txt","w")
    fh.write(reclist)
    return newID

#check customer account balance
def check_balance(totalPrice,customer_id):
    balanceRecs = []
    balanceStatus = "N"
    fh = open("C:\Temp\Data Files\Account Balance.txt", "r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        balanceRecs.append(reclist)
    fh.close()

    for recIndex in range(1, len(balanceRecs)):
        if balanceRecs[recIndex][0] == customer_id:
            currentAccountBalance = balanceRecs[recIndex][1]
            print("Your account balance is ",currentAccountBalance)

            if int(currentAccountBalance) >= totalPrice:
                balanceStatus = "Y"
                break
    return balanceStatus


#after order food item, update customer account balance
def update_account_balance(totalPrice,customer_id):
    balanceRecs = []
    fh = open("C:\Temp\Data Files\Account Balance.txt","r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        balanceRecs.append(reclist)
    fh.close()

    for recIndex in range(1,len(balanceRecs)):
        if balanceRecs[recIndex][0] == customer_id:
            currentAccountBalance = balanceRecs[recIndex][1]
            newBalance = int(currentAccountBalance) - int(totalPrice)
            balanceRecs[recIndex][1] = str(newBalance)
            break

    # write account balance to file
    fh = open("C:\Temp\Data Files\Account Balance.txt","w")
    for balanceRec in balanceRecs:
        rec = ":".join(balanceRec) + "\n"
        fh.write(rec)
    fh.close()


#customer order food item by entering item code
def order_food_item(customer_id):
    orderRecs = []
    foodRecs = []
    order_id = orderID()
    fh =  open("C:\Temp\Data Files\Food.txt", "r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        foodRecs.append(reclist)
    fh.close()

    code = ""
    totalPrice = 0
    while True:
        if code == "E":
            break

        while True:
            code = input("Enter Item Code that you would like to order or 'E' to Exit: ").upper()
            if code == "E":
                break

            item_code_exist = False
            for recIndex in range(1,len(foodRecs)):
                item_code = foodRecs[recIndex][2]
                food_item = foodRecs[recIndex][3]
                price = float(foodRecs[recIndex][4])

                if item_code == code:
                    item_code_exist = True
                    quantity = int(input("Enter quantity: "))
                    print(item_code + "-" + food_item + "-" + "RM" + str(price) + "- Qty: " + str(quantity))
                    paid_amount = price * quantity
                    if check_balance((totalPrice + paid_amount),customer_id) == "N":
                        print("Insufficient balance! Please top up account balance with admin.")
                        break

                    totalPrice = totalPrice + paid_amount
                    orderRec = [order_id,customer_id,item_code,food_item,str(price),str(quantity),str(paid_amount)]
                    orderRecs.append(orderRec)
                    break

            if item_code_exist == False :
                print("Invalid item code!")

        print("Total price is RM: " + str(totalPrice))
        if totalPrice > 0:
            confirm_order = input("Proceed to payment? Enter 'Y' to confirm order, or 'E' to cancel order: ").upper()
            if confirm_order == "Y":
                update_account_balance(totalPrice,customer_id)
                address_delivery_status_after_order(order_id)
                feedback()

                # write customer order to file
                fh = open("C:\Temp\Data Files\Customer Order.txt", "a")
                for orderRec in orderRecs:
                    rec = ":".join(orderRec) + "\n"
                    fh.write(rec)
                fh.close()
            else:
                return


# admin display all records of Customer Orders and Customer Payment
def view_all_customer_orders_payment():
    fh = open("C:\Temp\Data Files\Customer Order.txt","r")
    rec = fh.read()
    print(rec)
    fh.close()

# admin search amd display specific records of Customer Orders and Customer Payment
def view_specific_customer_orders_payment():
    fh = open("C:\Temp\Data Files\Customer Order.txt","r")
    orderRecs = []
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        orderRecs.append(reclist)
    fh.close()

    order_id = ""
    while True:
        if order_id == "E":
            break

        while True:
            order_id = input("Enter Order ID to view customer order & payment, or 'E' to Exit: ").upper()
            if order_id == "E":
                break

            # validate Order ID
            order_id_exist = False
            for recIndex in range(1, len(orderRecs)):
                if orderRecs[recIndex][0] == order_id:
                    customer_id = orderRecs[recIndex][1]
                    item_code = orderRecs[recIndex][2]
                    food_item = orderRecs[recIndex][3]
                    price = orderRecs[recIndex][4]
                    quantity = orderRecs[recIndex][5]
                    paid_amount = orderRecs[recIndex][6]
                    print(order_id + "-" + customer_id + "-" + item_code + "-" + food_item + "-" + price + "-" + quantity + "-" + paid_amount)
                    order_id_exist = True

            if order_id_exist == False:
                print("Invalid Order ID! Please try again.")
                break

# update address, not assigned to Delivery Status file. deliStatRecs = deliveryStatusRecords
def address_delivery_status_after_order(order_id):
    deliStatRecs = []
    fh = open("C:\Temp\Data Files\Delivery Status.txt","r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        deliStatRecs.append(reclist)
    fh.close()

    address = input("Please enter the address where you want to deliver your order: ")
    delivery_id = "not assigned"
    delivery_status = "not assigned"
    deliStatRec = [order_id,address,delivery_id,delivery_status]
    deliStatRecs.append(deliStatRec)

    # write order_id,address,delivery_id,delivery_status to file
    fh = open("C:\Temp\Data Files\Delivery Status.txt", "w")
    for deliStatRec in deliStatRecs:
        rec = ":".join(deliStatRec) + "\n"
        fh.write(rec)
    fh.close()


# new customer register account
def register():
    customerRecs = []
    fh = open("C:\Temp\Data Files\Customer Details.txt", "r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        customerRecs.append(reclist)
    fh.close()

    validAccount = False
    while True:
        if validAccount == True:
            break

        while True:
            customer_name = input("Create username, or Enter 'E' to cancel: ")
            if customer_name == "E":
                validAccount = True
                break

            invalidName = "N"
            for checkName in range(0,10):
                if customer_name.find(str(checkName)) > -1:
                    print("Username cannot contain number! Please try again")
                    invalidName = "Y"
                    break
            if (invalidName == "Y"):
                break

            if len(customer_name) == 0:
                print("Username too short! Please try again")
                break

            customer_pw = input("Create customer password: ")
            if len(customer_pw) < 6:
                print("Your password is too short! Please try again")
                break

            else:
                customer_pw1 = input("Please confirm your password: ")
                if customer_pw != customer_pw1:
                    print("Passwords are not matched! Please try again")
                    break

            validAccount = True
            customer_id = customerID()
            print("Create account successfully!! This is your Customer ID: ", customer_id)

            customerRec = [customer_id,customer_pw1,customer_name]
            customerRecs.append(customerRec)

            # write customer_id,customer_password,customer_name to file
            fh = open("C:\Temp\Data Files\Customer Details.txt", "w")
            for customerRec in customerRecs:
                rec = ":".join(customerRec) + "\n"
                fh.write(rec)
            fh.close()

            create_account_balance(customer_id)
            break


# create account balance for new users
def create_account_balance(customer_id):
    balanceRecs = []
    fh = open("C:\Temp\Data Files\Account Balance.txt", "r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        balanceRecs.append(reclist)
    fh.close()

    balanceRec = [customer_id,"0"]
    balanceRecs.append(balanceRec)

    # write account balance to file
    fh = open("C:\Temp\Data Files\Account Balance.txt", "w")
    for balanceRec in balanceRecs:
        rec = ":".join(balanceRec) + "\n"
        fh.write(rec)
    fh.close()


# delivery staff login success or not
def delivery_staff_login():
    loginID = input("Enter your ID: ").upper()
    loginPassword = input("Enter your password: ")
    loginSuccess = False
    fh = open("C:\Temp\Data Files\Delivery Staff.txt", "r")
    lines = fh.readlines()
    line_count = 0
    for line in lines:
        if line_count > 0:
            line = line.replace("\n","")
            rec_field = line.split(":")
            if loginID == rec_field[0]:
                if loginPassword == rec_field[2]:
                    loginSuccess = True
                    break
        line_count += 1
    fh.close()

    if loginSuccess:
        print('Login successfully')
        delivery_staff_menu()
    else:
        print('Invalid user or password')
        delivery_staff_login()


#registered customer login success or not
def customer_login():
    loginID = input("Enter your ID: ").upper()
    loginPassword = input("Enter your password: ")
    loginSuccess = False
    fh = open("C:\Temp\Data Files\Customer Details.txt", "r")
    lines = fh.readlines()
    line_count = 0
    for line in lines:
        if line_count > 0:
            rec_field = line.split(":")
            if loginID == rec_field[0]:
                if loginPassword == rec_field[1]:
                    loginSuccess = True
                    break
        line_count += 1
    fh.close()

    if loginSuccess:
        print('Login successfully')
        customer_menu(loginID)
    else:
        print('Invalid user or password')
        customer_login()


# admin staff login success or not
def admin_login():
    loginID = input("Enter your ID: ").upper()
    loginPassword = input("Enter your password: ")
    loginSuccess = False
    fh = open("C:\Temp\Data Files\Admin Staff.txt", "r")
    lines = fh.readlines()
    line_count = 0
    for line in lines:
        if line_count > 0:
            line = line.replace("\n","")
            rec_field = line.split(":")
            if loginID == rec_field[0]:
                if loginPassword == rec_field[2]:
                    loginSuccess = True
                    break
        line_count += 1
    fh.close()

    if loginSuccess:
        print('Login successfully!!')
        admin_menu()
    else:
        print('Invalid user or password')
        admin_login()


# view food item by category & admin view all food item
def display_food_item_category_wise():
    print("To see food items by category, select the following category code")
    print("C01: rice\nC02: noodle\nC03: snack\nC04: dessert\nC05: drink")
    foodRecs = []
    fh = open("C:\Temp\Data Files\Food.txt","r")
    fileLines = fh.readlines()
    for rec in fileLines:
        reclist = rec.strip().split(":")
        foodRecs.append(reclist)
    fh.close()

    categoryCode = ""
    foodCategory = ""
    while True:
        if categoryCode == "E":
            break

        while True:
            categoryCode = input("Enter Category Code or 'E' to exit: ").upper()
            if categoryCode == "E":
                break

            #validate category code
            count = 0
            category_code_exist = False
            for recIndex in range(1,len(foodRecs)):
                if foodRecs[recIndex][0] == categoryCode:
                    count += 1
                    foodCategory = foodRecs[recIndex][1]
                    itemCode = foodRecs[recIndex][2]
                    foodItem = foodRecs[recIndex][3]
                    price = foodRecs[recIndex][4]
                    if count == 1 :
                        print(categoryCode + "-" + foodCategory)
                    print("    " + itemCode + "-" + foodItem + "-RM " + price)
                    category_code_exist = True

            if category_code_exist == False :
                print("Invalid category code! Please try again.")
                break


# write/append feedback into Feedback file
def feedback():
    give_feedback = input("Enter '1' to give feedback or 'E' to Exit: ").upper()
    while True:
        if give_feedback == "E":
            break
        if give_feedback == "1":
            customer_id = input("Please enter your customer id(Ex.CX0000): ").upper()
            feed_back = input("Please enter your feedback: ")
            fh = open("C:\Temp\Data Files\Feedback.txt","a")
            fh.write("\n" + customer_id + ":" + feed_back)
            fh.close()
        break

# to exit APU ONLINE FOOD SERVICES
def exitPage():
    print("Thankyou for visiting APU ONLINE FOOD SERVICES. We hope to see you soon!!")

####################################################################################

# start system
def menuOptions():
    print('''Welcome to APU ONLINE FOOD SERVICES!! Choose any of the given options: 
    1. Login/Sign-in
    2. View food menu item as per category
    3. Register/Sign-up
    E. Exit
    ''')
    userInput = input("Select your options: ")
    return userInput


# log in to APU ONLINE FOOD SERVICES
def login():
    while True:
        print("""Choose any of the given options: 
    1: Log in to customer page
    2: Log in to admin page
    3: Log in to delivery staff page
    E: Exit""")
        action = input("Please select an option: ")
        if action == "1":
            customer_login()
        elif action == "2":
            admin_login()
        elif action == "3":
            delivery_staff_login()
        elif action == "E":
            exitPage()
            break
        else:
            print("Invalid option, please try again")
            login()

# to access to functionalities of customer
def customer_menu(customer_id):
    while True:
        print("""Choose any of the given options: 
        1: To view food menu item as per category
        2: To place order
        E: Exit
        """)
        action = input("Please select an option: ")
        if action == "1":
            display_food_item_category_wise()
        elif action == "2":
            order_food_item(customer_id)
        elif action == "E":
            exitPage()
            break
        else:
            print("Invalid option, please try again")


# to access to functionalities of admin
def admin_menu():
    while True:
        print("""Please enter 1/2/3/4/5/6/E to perform action:
        1: Access food menu (add, modify, delete)
        2: Display all food records by category
        3: Display all customer orders and payments
        4: Search specific record of customer order and payment
        5: Delivery management (add, modify, search, delete, assign orders)
        6: Help customer top up account balance
        E: Exit
        """)
        action = input("Please perform an action: ")
        if action == "1":
            admin_add_mod_del_food_item()
        elif action == "2":
            display_food_item_category_wise()
        elif action == "3":
            view_all_customer_orders_payment()
        elif action == "4":
            view_specific_customer_orders_payment()
        elif action == "5":
            delivery_management()
        elif action == "6":
            admin_topup_customer_account_balance()
        elif action == "E":
            exitPage()
            return
        else:
            print("Invalid code, please try again")


def delivery_management():
    print('''Please enter 1/2/3/4/E to perform action:
    1. Add delivery staff
    2. Modify / Delete delivery staff
    3. Search delivery staff
    4. Assign orders to delivery staff
    E. Exit
    ''')
    action = input("Please perform an action: ")
    if action == "1":
        admin_add_delivery_staff()
    elif action == "2":
        admin_mod_del_delivery_staff()
    elif action == "3":
        view_specific_delivery_staff()
    elif action == "4":
        admin_assign_order()
    elif action == "E":
        exitPage()
        return
    else:
        print("Invalid action! Please try again.")
        delivery_management()


# to access to functionalities of delivery staff
def delivery_staff_menu():
    while True:
        print("""Choose any of the given options: 
           1: To view delivery status and select order to update delivery status
           E: Exit
           """)
        action = input("Please select an option: ").upper()
        if action == "1":
            delivery_staff_update_delivery_status()
        elif action == "E":
            exitPage()
            break
        else:
            print("Invalid code, please try again")

# MAIN lOGIC
while True:
    userInput = menuOptions()
    if userInput == "1":
        login()
    elif userInput == "2":
        display_food_item_category_wise()
    elif userInput == "3":
        register()
    elif userInput == "E":
        exitPage()
        break
    else:
        print("Invalid option! Please try again.")
        menuOptions()
