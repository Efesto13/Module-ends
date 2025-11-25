
#Opens lists and variables

books=[{"title":"Chupa_Cabra","author":"shupapi","price":100,"stock":50},{"title":"kamasutra","author":"botero","price":200,"stock":150},
       {"title":"kimetsu","author":"ino","price":150,"stock":400},{"title":"jujutsu","author":"akutami","price":300,"stock":210},
       {"title":"divina_comedia","author":"dante","price":450,"stock":510}]
sales=[]
check=True

def register():                                                             #Open variable for uses as button
    
    title=input("Enter title\n-->")                                      

    while check:                                                            
        author=input(f"Enters de author name of {title}\n-->").lower()
        if not author.isalpha():                                           #Uses isalpha for only admitted words
            print("Character invalid")
        else:
            break

    while check:                                                           #While for repeat the line code 
        category=input(f"Enters category of {title}\n-->").lower()
        if not category.isalpha():
            print("Character invalid")
        else:
            break
    try:                                                                   #Use try and except in cause an error
        while check:
            price=float(input(f"Enters price of {title}\n-->"))                 
            if price <1:
                print("Price invalid")
            else:
                break
    except:
        print("Price invalid")


    while check:
        try:
            stock=int(input(f"Enters stock of {title}\n-->"))
            if stock <1:
                print("insufficient quantity ")
            else:
                break
        except:
            print("Character invalid")

    library={"title":title,"author":author,"price":price,"stock":stock}       #Open dictionary for save keys and values
    books.append(library)                                                     #Introducing in a list

def consult():
    search=input("Book title\n-->")
    located=False                                       #Use variable located for uses with guide the search the book
    for consult in books:
        if search == consult["title"]:                  #If search not same a consult print "Not found book"
            print(f"Tittle:{consult["title"]}|Author:{consult["author"]}|Price:{consult["price"]}|Stock:{consult["stock"]}")#If consult found "title" print information
            located=True
    if located==False:
        print("Not found book")
          
def update():
        search=input("Book title\n-->")
        located=False
        for consult in books:
            if search == consult["title"]:
                located=True
                change=input("--¿What do yo change?--\n (1)Tittle and Author \n (2)Price and Stock\n -->")
                if change =="1":
                     while check:
                        new_tittle=input("Enter new title\n-->")         #Create new variable for chnages values in the diccionary
                        new_author=input("Enter new author\n-->")
                        consult["title"]=new_tittle                     #Here changes values with the help of the iterator
                        consult["author"]=new_author
                        if not new_author.isalpha():
                            print("Character invalid")
                        else:
                            break
                if change == "2":
                    try:
                        while check:    
                            new_price=float(input("Enter new price\n-->"))
                            new_stock=int(input("Enter new stock\n-->"))
                            consult["price"]=new_price
                            consult["stock"]=new_stock                    
                            if new_price <1 and new_stock <1:
                                    print("Character invalid")
                            else:
                                break
                    except:
                        print("Character invalid")
        if located==False:
            print("No found book")

def delete():
    search=input("¿What do yo delete?\n-->")      #Searching the book want the elimited
    located=False
    for detele in books:
        if search == detele["title"]:
            books.remove(detele)              #Uses .remove for delete one part of the list         
            located=True
            print("Book delete")
    if located==False:
        print("Not found book")

def sales_():

    if not books:
       print("No books aviable")
       return
    
    name=input("Buyer's name\n-->")
    if not name:
        print("Names not empty")
        return

    title=input("Enter book title to sell\n-->")
    located=False
    for search in books:
        if title == search["title"]:
            located=True
            break
    if located == False:
        print("Not found book")
        return
    
    if search["stock"]==0:
        print("This book out of store")
        return
    
    while check:
        try:    
            quantity=int(input(f"Enter quantity to sell and (aviable: {search['stock']})\n-->"))
            if 1<= quantity <=search["stock"]:
                break
            else:
                print(f"Enter a quantity between 1 and {books['stock']}.")
        except: 
            print("Invalid quantity")

    while check:
        try:
            discount=float(input("Enter discount porcentage(0 for not discount\n-->)"))
            if 0<= discount <=100:
                break
            else:
                print("Discount beetwen 0 and 10")
        except:
            print("Character invalid")
        
            

    dates=(input("date of purchase of the book\n -->",))

    subtotal=search["price"] * quantity                   
    discount_=subtotal * (discount/100)
    total=subtotal-discount_
    
    sale={"name":name,"b_title":search["title"],"author":search["author"],"quantity":quantity,"price_unid":search["price"],"discount":discount,"date":dates,"total":total}
    sales.append(sale)

    search["stock"] -= quantity

    print(f" Client: {name}\n Book: {search['title']}\n Quantity: {quantity}\n Discount: {discount}\n Total: {total}\n Date: {dates}\n")

def top_3():
    acount_={}
    for search in sales:
        acount_[search["b_title"]]=acount_.get(search["b_title"],0)+ search["quantity"]

        ranking=sorted(acount_.items(),key=lambda x: x[1], reverse=True)

        print(ranking[:3])

def sales_author():
    sales_author={}
    for sell in sales:
        
        author_sell=next(p["author"] for p in books if p["title"]== sell["b_title"])    

        sales_author[author_sell]=sales_author.get(author_sell,0) + sell["total"]

    for author_sell,total in sales_author.items():
        print(f"{author_sell}: {total}|Book:{"b_title"}")
     
def net_gross():
    
    gross=sum(s["total"] for s in sales)  #we add the total y uses iterator
        
    net=gross * 0.90                      #the total of gross use for multiplicacion with 0.90

    print(f"Gross : {gross}")
    print(f"Net(after 10%):{net}")   
        

def menu():                                         #this is the menu we create with the defs
    while check:
        ingresar=(input("----\n (1)Register \n (2)Consult \n (3)Update \n (4)Detele \n (5)Sales \n (6)Ranking \n (7)Sales for author \n (8)Gross and net \n (9)Salir  \n---- \n -->"))
        if ingresar =="1":
            register()
        elif ingresar =="2":
            consult()
        elif ingresar =="3":
            update()
        elif ingresar =="4":
            delete()
        elif ingresar =="5":
            sales_()
        elif ingresar =="6":
            top_3()
        elif ingresar =="7":
            sales_author()
        elif ingresar =="8":
            net_gross()
        else:
            break

menu()  