#read the stock products and store them in a list
class read_class:
    def read_file(self): 
        file=open("products.txt","r") #open stock file (products.txt) in read mode. 
        lines=file.readlines() 
        L=[] 
        for line in lines:
            L.append(line.replace("\n","").split(","))
        file.close()
        
        print("\nWelcome to our Store!!")
        print("Following products are avilable in our Store")
        print("--------------------------------------------------------")
        print("PRODUCT\t\tPRICE PER KG\t\tNUMBER OF KGS AVAILABLE")
        print("--------------------------------------------------------")
        for i in range(len(L)):
            print(L[i][0],"\t\t",L[i][1],"\t\t\t\t",L[i][2]) 
        print("--------------------------------------------------------")
        return L