#Key Points to remeber:

#Validation is must. Exception Handling should be done.

#1. Check corner cases
#2. Check budget left before adding another item to list




while True:  
    try: 
        budget = float(input("Enter your budget : "))  
    except ValueError: 
        print("Enter an Integer") 
        continue
    else: 
        break

product_info={"Product name":[], "Quantity":[], "Price":[]} 
  
product_lst = list(product_info.values()) 
  
name_item = product_lst[0] 
quant_item = product_lst[1] 
price_item = product_lst[2] 
  
amnt = budget

while True: 
    try: 
        choice = int(input("1.Add an item\n2.Exit\nEnter your choice : ")) 
    except ValueError: 
        print("\nInvalid input") 
        continue
    else: 
        if choice == 1 and amnt>0:                  
            p = input("Enter product : ")  
            q = int(input("Enter quantity : ")) 
            pr = float(input("Enter Price: "))   
  
            if pr>amnt: 
                print("\nCan't Buy the product (because budget left is less than price of the item)")  
                continue
  
            else: 
                if p in name_item:   
                    ind = name_item.index(p)  
                    s1 = quant_item[ind]  
                    s2 = price_item[ind]
                    quant_item.remove(quant_item[ind])  
                    price_item.remove(price_item[ind])   
                    quant_item.insert(ind, q+s1)    
                    price_item.insert(ind, pr+s2)    
                    amnt = budget-sum(price_item)    
  
                    print("\namount left ", amnt) 
                else:  
                    name_item.append(p)   
                    quant_item.append(q)    
                    price_item.append(pr)  
                    amnt = budget-sum(price_item)    
  
                    print("\namount left ", amnt) 
        elif amnt<= 0 and choice ==1:  
            print("\nNo Amount left")   
        else:
            break 


print("\n\nAmount left : Rs.", amnt)  
  
if amnt in price_item:  
    print("\nAmount left can buy you ", name_item[price_item.index(amnt)])   
  
print("\n\nGROCERY LIST is:")
print("Product-name Quantity Price") 
for i in range(len(name_item)):  
    print(name_item[i], quant_item[i], price_item[i]) 