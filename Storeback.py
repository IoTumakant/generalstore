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


#selectedItem=[]     #empty list declaration


class purchage():
    #selectedItem=[]    # class variable shared by all instances
    def __init__(self):
        self.CustomerName="CustName" # instance variable unique to each instance
        self.selectedItem=[]
        ### function for select item
    def selectItem(self):
        print("Select your Items:")
        while True:
            yourItem=int(input())
            if yourItem==0:
                break #code correction
            else:
                #selectedItem.add(yourItem)
                self.selectedItem.append(yourItem) #list declaration of selectItem
                print(item_dict.get(yourItem))
    ### function to print invoice
    def printInvoice(self):
        clear()
        TotalAmt=0   
        print('\n------------------\nInvoice: ',self.CustomerName,'\n------------------')
        for item in self.selectedItem:
            print(item_dict.get(item),"|",item_rate.get(item))#correction here
            TotalAmt+=itemPrice(item)
        print("------------------\nTotal Amount: ",TotalAmt,"\n------------------")



### dictonary for items
item_dict={
    1:'Peas White',
    2:'Ashirwaad Atta',
    3:'Masoor Dal',
    4:'Chana Black',
    5:'Sugar',
    6:'Moong Dal',
    7:'Jeera',
    8:'Mastard Oil',
    9:'Poha',
    10:'Ashirwaad Salt'}

### dictionary for item rate
item_rate={
    1:95.24,
    2:357.44,
    3:80.96,
    4:40,
    5:52.38,
    6:57.44,
    7:124.76,
    8:619.04,
    9:63.80,
    10:18
}

### dictionary for options
option_list={
    'M':'Menu',
    'R':'Rate list',
    'P':'Purchage',
    'I':'Invoice',
    'Q':'Quit'
}

def OptionList():
    print('-----------------------------------')
    print('Options')
    print('-----------------------------------')
    for item in option_list:
        print(item,':',option_list.get(item),end='\t')
    print('\n-----------------------------------')

### functon for price list display
def priceList():
    clear()
    print('-----------------------------------')
    print('PRICE')
    print('-----------------------------------')
    for item in item_dict:
        if item in range(1,13,2):
            print(item_dict.get(item),':',item_rate.get(item),end='\t')
        else:
             print(item_dict.get(item),':',item_rate.get(item),end='\n')
    print('-----------------------------------')

### function for Menu display  
def dispMenu():
    clear()
    print('-----------------------------------')
    print('MENU')
    print('-----------------------------------')
    for item in item_dict:
        if item in range(1,13,2):
            print(item,':',item_dict.get(item),end='\t')
        else:
            print(item,':',item_dict.get(item),end='\n')
    print('-----------------------------------')

### function to get item price
def itemPrice(item):
     return item_rate.get(item)
#print('Price of \"',item_dict.get(3),"\" is ",itemPrice(3))



       



#clear()
#dispMenu()
#priceList()
#selectItem()
