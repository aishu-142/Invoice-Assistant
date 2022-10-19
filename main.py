#module : main
import read
import purchase
import write
again="Y"
while again.upper()=="Y":
    obj1 = read.read_class()
    a = obj1.read_file()
    obj2 = purchase.purchase_class()
    b = obj2.purchase(a)
    obj3 = write.write_class()
    obj3.over_write(a,b)
    print("\nThank you for shopping from our store!!")
    print("Please check your Invoice for your shopping details which is generated in the form of a text file.")
    again = input("\nIs any new customer waiting in the queue? ")
