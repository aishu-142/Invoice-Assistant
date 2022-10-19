#all the calculations and invoice generation
class purchase_class:
    def purchase(self,List):
        L = List
        a_name = input("Please enter your name: ")
        print("\nHello "+a_name+"!!")
        q = {}
        flag = "Y"
        while flag.upper() == "Y":  
            product = input("\nPlease have a look at the available items above and enter the product you want to purchase: ")  
            product_name = product.upper()
            flag_value = 0
            for i in range(len(L)):
                if product_name == L[i][0].upper():
                    p = True
                    flag_value = 1
                    while p == True:
                        try:
                            p_quantity = int(input("Enter the quantity of "+product+" you want to buy: "))
                            p = False
                        except:             #executes, if customer entered unexpected value.
                            print("\t\tError!!!\nPlease enter integer value!! ")
                    for j in range(len(L)):
                        if product_name == L[j][0].upper() and p_quantity <= int(L[j][2]):
                            q[product_name] = p_quantity
                            break
                    else:
                        print("\nSorry, "+a_name+"!, "+product+" is out of stock.\nWe will upgrade the stock of "+product+" soon.\n")
                           
                    flag=(input(a_name+", Do you want buy more products? Enter Yes or No(Y/N): "))
                    break
                   
            if flag_value == 0:
                print("Sorry, "+a_name+"!! "+product+" is not available in our store.")
                print("----------------------------------------------------------")
                print("PRODUCT\t\tPRICE PER KG\t\tNUMBER OF KGS AVAILABLE")
                print("----------------------------------------------------------")
                for i in range(len(L)):
                    print(L[i][0],"\t\t",L[i][1],"\t\t\t\t",L[i][2]) #prints last updated product name, quantity and price.
                print("-----------------------------------------------------------")
                print("This is the list of available items")
                flag=(input(a_name+", Do you want buy more products? Enter Yes or No(Y/N): "))
                   
        print ("\nThis is the list of items that you've choosen and their quantities respectively:\n",q,"\n")
        
        #final amount
        f_amount=0  
        price_list = {}
        for keys in q.keys():
            for i in range(len(L)):
                if keys == L[i][0].upper():
                    price = int(L[i][1])
                    num = int(q[keys])
                    amount = price * num
                    f_amount += amount
                    price_list[keys] = amount
                    print("\nTotal cost for",keys,":",amount)
        
        print("\nYour discountable total amount is: ", f_amount)

        #discount
        dis=0.0
        if f_amount>=1000:
            discount = 10.0
        elif f_amount>=500:
            discount = 5.0
        else:
            discount = 0.0
           
        print("You have received a discount of",discount,"%on your purchase.")
           
        dis=(discount*f_amount)/100
        total=float(f_amount-dis)
       
       
        #invoice generation
        import datetime  
        dt=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
        invoice=str(dt)    #unique invoice
        t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) #date
        d=str(t)    #date
        u=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second) #time
        e=str(u)    #time
       
        file=open(invoice+" ("+a_name+").txt","w")      #generates a unique invoice name and open it in write mode.
        file.write("===========================================================")
        file.write("\n\t\tGROCERY STORE - INVOICE")
        file.write("\n\nInvoice: "+invoice+"\t\t\tDate: "+d+"\n\t\t\t\t\tTime: "+e+"")
        file.write("\nName of the Customer: "+str(a_name)+"")
        file.write("\n==========================================================")
        file.write("\nITEM NAME\tQUANTITY \tUNIT PRICE\tTOTAL")                    
        file.write("\n---------------------------------------------------------------------------------------------")
             
        for keys in q.keys():  
            for i in range(len(L)):
                if keys == L[i][0].upper():
                    file.write(str("\n"+str(keys)+" \t\t "+str(q[keys])+" \t\t\t "+str(L[i][1])+" \t\t\t "+str(price_list[keys])))
            
           
        file.write("\n\n---------------------------------------------------------------------------------------------")
        file.write("\n\t\t\t\tYour discountable amount: "+str(f_amount))
        file.write("\n------------------------------------------------------------------------------------------------")
        file.write("\n\t\t\tYour "+str(discount)+"% discounted amount is: "+str(dis))
        file.write("\n------------------------------------------------------------------------------------------------")
        file.write("\n\t\t\t\tYour payable amount is: "+str(total))
        file.write("\n-------------------------------------------------------------------------------------------------")
        file.write("\n\n\t\tThank You for shopping with us.\n\t\tPlease visit again!!")
        file.write("\n===========================================================")
        file.close()
       
        return q
