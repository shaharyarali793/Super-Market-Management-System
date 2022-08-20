import prettytable
import random

def add_an_item():
    filename=open('item.txt','a')
    times=int(input("Enter how many items are there of which you want to input data : "))
    for i in range(times):
        print(f"Information for Item {i+1}")
        item_id= str(random.randint(1,100000))
        item_name=str(input("Enter Item name : ")).capitalize() 
        item_price="$"+" "+str(input("Enter Item price : "))
        expiry_date=input("Enter Item expiry date : ")
        amount=str(input("Enter total Item count : "))
        item_sold = str("")
        filename.write(item_id+","+item_name+","+item_price+","+expiry_date+","+amount+","+item_sold+"\n")
    filename.close()
    
    
def display_items():
    #Text-Based Tables python
    filename = open('item.txt', 'r')

    table = prettytable.PrettyTable(["Item ID", "Item Name","Item Price","Expiry Date","Amount","Item Sold"])
    for lines in filename:
        x = lines.split(",")
        table.add_row([x[0],x[1],x[2],x[3],x[4],x[5]])
       
    print(table)
    filename.close()
def delete():
    file=open("item.txt","r+")
    d=[]
    name=str(input("Enter Item name : ")).capitalize()
    for lines in file:
        x=lines.split(",")
        if x[1]==name:
            r=""
            d.append(r)
        else:
            d.append(lines)
    file.close()
    file=open("item.txt","w")
    for lin in d:
        file.writelines(lin)
    file.close()

#updating
def update():
    files=open("item.txt","r+")
    u=[]
    name=str(input("Enter Item name : ")).capitalize()
    for lines in files:
        x=lines.split(",")
        if x[1]==name:
            item_name=input("Enter Item name : ")
            item_price= "$"+" "+str(input("Enter Item price : ")) 
            expiry_date=input("Enter Item expiry date : ")
            amount=str(input("Enter total Item count : "))
            filesy=(x[0]+","+item_name+","+item_price+","+expiry_date+","+amount+x[5]+'\n')
            u.append(filesy)
        else:
            u.append(lines)
    files.close()
    file=open('item.txt',"w")
    for lines in u:
        file.writelines(lines)
    file.close()

def search():
    files=open("item.txt","r+")
    name=str(input("Enter Item name : ")).capitalize()
    for lines in files:
        x=lines.split(",")
        if x[1]==name:
       
            table = prettytable.PrettyTable(["Item ID", "Item Name","Item Price","Expiry Date","Amount"])

            table.add_row([x[0],x[1],x[2],x[3],x[4]])
    print(table)
    files.close()

def sell_item():
    files=open("item.txt","r+")
    item_name=str(input("Enter Item name : ")).capitalize()
    item_count=int(input("Enter total Item count : "))
    u=[]
    for lines in files:
        x=lines.split(",")
        if x[1]==item_name:
            if int(x[4]) >= item_count:  #check quanitty
                new_amount =str(int(x[4])-item_count)
                filesy=(x[0]+","+x[1]+","+x[2]+","+x[3]+","+new_amount+","+str(item_count)+'\n')
                u.append(filesy)
            else:
                print("Insufficient Stock!")
                files.close()
                break
        else:
            u.append(lines)
    files.close()
    file=open('item.txt',"w")
    for lines in u:
        file.writelines(lines)
    file.close()

def total_sell():
    filename = open("item.txt","r+")
    table = prettytable.PrettyTable(["Item Name", "Item Price","Item Sold","Amount Earned"])
    for lines in filename:
        x = lines.split(",")
        if len(x[5])>1:
            price = x[2].strip("$")
            total_amount = "$" + " "+str(int(price) * int(x[5])) 
            table.add_row([x[1],x[2],x[5],total_amount])
    print(table)
    filename.close()
while True:
    print("                           ........Select Option........")
    print("                           1.Add an item ")
    print("                           2.Sell an item")
    print("                           4.Edit item")
    print("                           3.Delete an item")
    print("                           6.Display items")
    print("                           5.Display total sale of the day")
    print("                           7.exit")
    print("                           8.Search for a item")
    decision=int(input("Enter : "))
    if decision==1:
        add_an_item()
        print("press B for back")
        fr=input("Enter : ")
        if fr=="B" or fr=="b":
            continue
    if decision==2:
        sell_item()
        print("press B for back")
        fr = input("Enter : ")
        if fr == "B" or fr=="b":
            continue
    if decision==3:
        delete()
        print("press B for back")
        fr = input("Enter : ")
        if fr == "B" or fr=="b":
            continue
    if decision==4:
        update()
        print("press B for back")
        fr = input("Enter : ")
        if fr == "B" or fr=="b":
            continue
      
    if decision==5:
        total_sell()
        print("press B for back")
        fr = input("Enter : ")
        if fr == "B" or fr=="b":
            continue
    if decision==6:
        display_items()
        print("press B for back")
        fr = input("Enter : ")
        if fr == "B" or fr == "b":
            continue
    if decision==7:
        break
    if decision==8:
        search()
        print("press B for back")
        fr = input("Enter : ")
        if fr == "B" or fr == "b":
            continue