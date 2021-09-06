import json
from datetime import date;

#creating the items and attributes

products =  {
"1001":{"item_name" : "dairy milk","price" : 5,"quantity" : 35,"validity" : "6 months","expire": "dec-2021"},
"1002":{"item_name" : "5-star","price" : 5,"quantity" : 45,"validity" : "6 months","expire": "dec-2021"},
"1003":{"item_name" : "munch","price" : 5,"quantity" : 30,"validity" : "6 months","expire": "dec-2021"},
"1004":{"item_name" : "lays","price" : 5,"quantity" : 100,"validity" : "6 months","expire": "dec-2021"},
"1005":{"item_name" : "bingo","price" : 10,"quantity" : 35,"validity" : "6 months","expire": "dec-2021"},
"1006":{"item_name" : "thumbs-up","price" : 40,"quantity" : 30,"validity" : "2 months","expire": "dec-2021"},
"1007":{"item_name" : "sprite","price" : 40,"quantity" : 35,"validity" : "2 months","expire": "dec-2021"},
"1008":{"item_name" : "dairy milk silk","price" : 75,"quantity" : 15,"validity" : "6 months","expire": "dec-2021"},
"1009":{"item_name" : "dairy milk bubble","price" : 95,"quantity" : 5,"validity" : "6 months","expire": "dec-2021"},
"1010":{"item_name" : "5-star medium","price" : 10,"quantity" : 35,"validity" : "6 months","expire": "dec-2021"},
"1011":{"item_name" : "perk","price" : 5,"quantity" : 90,"validity" : "6 months","expire": "dec-2021"},
"1012":{"item_name" : "dairy milk shorts","price" : 2,"quantity" : 35,"validity" : "6 months","expire": "dec-2021"},
"1013":{"item_name" : "perk extra large","price" : 25,"quantity" : 25,"validity" : "6 months","expire": "dec-2021"},
"1014":{"item_name" : "kinder joy","price" : 50,"quantity" : 10,"validity" : "6 months","expire": "dec-2021"},
"1015":{"item_name" : "gems packets","price" : 5,"quantity" : 35,"validity" : "6 months","expire": "dec-2021"},
"1016":{"item_name" : "gems ball","price" : 50,"quantity" : 5,"validity" : "6 months","expire": "dec-2021"},
"1017":{"item_name" : "sprite","price" : 45,"quantity" : 35,"validity" : "2 months","expire": "dec-2021"},
"1018":{"item_name" : "fanta","price" : 45,"quantity" : 35,"validity" : "6 months","expire": "dec-2021"},
"1019":{"item_name" : "maaza","price" : 45,"quantity" : 15,"validity" : "6 months","expire": "dec-2021"},
"1020":{"item_name" : "dairy milk oreo","price" : 75,"quantity" : 5,"validity" : "6 months","expire": "dec-2021"},
"1021":{"item_name" : "britania cake","price" : 25,"quantity" : 35,"validity" : "6 months","expire": "dec-2021"},
"1022":{"item_name" : "good day","price" : 5,"quantity" : 30,"validity" : "6 months","expire": "dec-2021"},
"1023":{"item_name" : "oreo","price" : 10,"quantity" : 30,"validity" : "6 months","expire": "dec-2021"},
"1024":{"item_name" : "haldirams mixture","price" : 5,"quantity" : 30,"validity" : "6 months","expire": "dec-2021"},
"1025":{"item_name" : "haldirams moong dal","price" : 5,"quantity" : 30,"validity" : "6 months","expire": "dec-2021"},
"1026":{"item_name" : "britania cookies","price" : 5,"quantity" : 30,"validity" : "6 months","expire": "dec-2021"},
"1027":{"item_name" : "kisses chocolate","price" : 5,"quantity" : 150,"validity" : "6 months","expire": "dec-2021"},
"1028":{"item_name" : "eclairs","price" : 5,"quantity" : 130,"validity" : "6 months","expire": "dec-2021"},
"1029":{"item_name" : "jim jam","price" : 10,"quantity" : 30,"validity" : "6 months","expire": "dec-2021"},
"1030":{"item_name" : "lolly pops","price" : 5,"quantity" : 150,"validity" : "6 months","expire": "dec-2021"},
} ;

js = json.dumps(products);    #storing in json file
fd = open("products_for_sale-copy.json","w");
fd.write(js);
fd.close();



#asking costumer need to buy   or the person want to sell the items...
print("*********Welcome sir/madam**********");
print("*********do you wanna wish to buy or sell!*********");

choice = int(input("enter 1 if u want to buy!!!"))


if choice==1:
    print("*********What do you want to buy sir/madam*******");
    print("****These are the list items available in our store sir/madam****");


    #displaying items
    for i in products:
        print("           ",i , "       -         " , products[i]["item_name"]);


    #asking from costumer

    no_of_items = 1;
    bill = 0;


    items_bought ={};     #items bought is keeping in the dictionary

    while(no_of_items):

        fr = open("products_for_sale.json","r");
        txt = fr.read();
        fr.close();

        products = json.loads(txt);


        id = input("Enter the id of the item sir/madam");
        quant = int(input("enter no.of items do u want"));



        #if id is not present :

        if id in products:
            pass;
        else:
            print("sorry sir/madam.. there is no such item matching to your entered id");
            continue;



        #if entered quant is more than item quantity in the store
        if(quant > products[id]["quantity"]):
            print("Sorry sir/madam , quantity of items are less than you have entered");
            continue;


        ##items a costumer bought storing in dictionary
        new_item = {id : {"name" : products[id]["item_name"] , "quantity" : quant , "price" : products[id]["price"]}};
        if id in items_bought:  ##if costumer opts same product 2 times
            items_bought[id]["quantity"] += quant;
        else:
            items_bought.update(new_item) ;



        #modifying values

        products[id]["quantity"] = products[id]["quantity"] - quant ;

        js = json.dumps(products);
        fd = open("products_for_sale.json","w");
        fd.write(js);
        fd.close();


        bill = bill + quant * (products[id]["price"]);

        no_of_items = int(input("Do you want another item - then enter 1"));



    #billing and storing the data

    link_number  =   {};

    phone_number  =  input("sir/madam... please enter your phone number");

    for i in link_number:

        if phone_number in i:
            discount = 2;
            break;
    else:
        discount = 0;

    #{9099999999 : {id : "1001" , "item_name" : "dairy_milk" , "quantity" : 10" }};
    link_number_with_items = {phone_number : items_bought }     #making dict with the items bought


    #forming a 3d dict day wise(keys)
    #{2021-09-03  :  { 9099999999 :  {  id : "1001" , "item_name": "dairy milk"  , "quantity" : 10  }  }}

    sold_items = {str(date.today()) : link_number_with_items}
    js_sold = json.dumps(sold_items);
    fd_sold = open("js_sold_items_days.json","a");
    fd_sold.write(js_sold) ;
    fd_sold.write("\n");
    fd_sold.close();


    #BILLING using items_bought

    index_in_bill =1;

    print("index   item id            item name     quantity item_price items_price")
    for item_id in items_bought :
        print(index_in_bill , ".     " , item_id ,"          " , items_bought[item_id]["name"], "        " ,items_bought[item_id]["quantity"], "   *  " , items_bought[item_id]["price"],"   =    "  ,  items_bought[item_id]["quantity"] * items_bought[item_id]["price"]);
        index_in_bill+=1;


    #discount purpose
    if bill > 1500:
        discount+=3;
    elif bill > 500:
        discount+=2;

    print("             Your bill is :" ,            (bill*(100-discount))/100.0);

    print("Thank you sir/madam.... Please visit again");



elif choice==0:

    #when selling products


    no_of_items =1 ;
    pay_slip =0;

    items_sold_update={};

    while(no_of_items):


        fr = open("products_for_sale.json", "r");
        txt = fr.read();
        fr.close();

        products = json.loads(txt);


        id = input("enter the id of the product: ");


        #if the element is present in the product store
        if id in products:

            quant = int (input( "enter no.of items to be added:" ));
            products[id]["quantity"]  += quant ;
            pay_slip +=  products[id]["price"]* quant ;
            new_item = {id : {"name" : products[id]["item_name"] , "quantity" : quant , "price" : products[id]["price"]}};

        else:

            name = input("Enter product name:");
            price = int(input("Enter price of product:"));
            quant = int(input("Enter quantity of product:"));
            validity = input("Enter validate months:");
            expire = input("Enter expiration details:");

            products[id] = {"item_name" : name ,"price" : price,"quantity" : quant,"validity" : validity,"expire": expire};

            pay_slip = quant * price ;
            new_item = {id: {"name": products[id]["item_name"], "quantity": quant, "price": products[id]["price"]}};


        ##adding the sold items to a seperate file

        items_sold_update.update(new_item);


        ##again dunping the dictionary to a file

        js = json.dumps(products);
        fd = open("products_for_sale.json", "w");
        fd.write(js);
        fd.close();


        no_of_items = int(input("Do you want to sell another item: "));


    #linking the phone number of the seller

    # {9099999999 : {id : "1001" , "item_name" : "dairy_milk" , "quantity" : 10" }};
    phone_number = int(input("enter your number: "));
    link_number_with_items = {phone_number: items_sold_update}  # making dict with the items bought

    #linking date with the items

    bought_items = {str(date.today()): link_number_with_items};
    js_bought = json.dumps(bought_items);
    fd_bought = open("js_bought_items_days.json", "a");
    fd_bought.write(js_bought);
    fd_bought.write("\n");
    fd_bought.close();


    #paying money items to the seller

    index_in_bill = 1;

    print("index   item id            item name     quantity item_price items_price")
    for item_id in items_sold_update:
        print(index_in_bill, ".     ", item_id, "          ", items_sold_update[item_id]["name"], "        ",items_sold_update[item_id]["quantity"], "   *  ", items_sold_update[item_id]["price"], "   =    ",items_sold_update[item_id]["quantity"] * items_sold_update[item_id]["price"]);
        index_in_bill += 1;


    print("the amount ", pay_slip ," is paid to you");
    print("thank You");

else:
    print("enter either 0 or 1 only");





