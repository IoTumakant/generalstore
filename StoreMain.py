import Storeback as STB 
import os 
import sys
if sys.platform.startswith("linux"): # could be "linux", "linux2", "linux3", ...
   #linux code
   clear=lambda:os.system('clear') 
elif sys.platform == "darwin":
   #Mac code
   clear=lambda:os.system('clear') 
elif sys.platform == "win32":
   #windows code
   clear=lambda:os.system('cls')
###Store main page
def Options():
    print('-----------------------------------')
    print('Options:')
    print('M: Menu\tR: Rate List\tQ: Quit')
    print('-----------------------------------') 
def StoreMain():
    while True:
        STB.OptionList()
        choice=input('Enter your option:')
        if choice=='Q':
            break
        elif choice=='M':
            STB.dispMenu()# display Menu call
        elif choice=='R':
            STB.priceList()# display Price list call
        elif choice=='P':
            Name=input("Your name:")
            P=STB.purchage()    #object instantiation
            P.CustomerName=Name #attributes assignment
            P.selectItem()      #attribute call
        elif choice=='I':   
            Name=input("Your name:")
            if Name==P.CustomerName:
                P.printInvoice()
            else:
                print(Name, ": Your invoice is not available")
        else:
            clear()
            print('Wrong choice!')

StoreMain()
