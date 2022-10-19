#Update quantity of product after customer transaction and print the remaining stock products.
class write_class:
    def over_write(self,List,Dictionary):  
        L=List 
        d=Dictionary 
        for key in d.keys():
            for i in range(len(L)):
                if key == L[i][0].upper():
                    break
                    
            L[i][2]=str(int(L[i][2])-d[key])
            
        print("\nRemaining Stock Products:\n",L)
            
        files=open("products.txt","w")  #opens stock file (products.txt) file in write mode.
        
        for each in L:
            files.write(str(",".join(each)))
            files.write("\n")         
        files.close()
        return L