"""
Product Management System to manage products in the inventory
"""
products=[]
ref = iter(range(1, 101))

def create_product():
    """
    Create product to add product with name and price
    :return: None
    """
    product_id=next(ref)
    product_name=input("Enter product name ")
    product_price=float(input("Enter price of product"))
    products.append({"id":product_id,"name":product_name,"price":product_price})

def delete_product():
    """
    Delete product based on product id
    :return: None
    """
    product_id = float(input("Enter product id"))
    for each_product in products:
        if each_product["id"]==product_id:
            print(f"{each_product['name']} with product_id {each_product['id']}\
             removed from inventory!")
            products.remove(each_product)

def update_product():
    """
    Update product price based on product id
    :return: None
    """
    product_id = float(input("Enter product id"))
    product_price = float(input("Enter price to update"))
    for each_product in products:
        if each_product["id"] == product_id:
            each_product["price"]=product_price


def select_product():
    """
    To check whether product exists in inventory based on product id
    :return: None
    """
    product_id = float(input("Enter product id"))
    if any(products):
        for each_record in products:
            if product_id== each_record["id"]:
                print(each_record["id"], each_record["name"], each_record["price"])
    else:
        print("Inventory is empty!")

def display_products():
    """
    Display all products from inventory
    :return: None
    """
    if any(products):
        for each_record in products:
            print(each_record["id"],each_record["name"],each_record["price"])
    else:
        print("Inventory is empty!")


SELECT_CHOICE="""
1. create product
2. delete product
3. update product
4. select product
5. display products
6. Quit
Enter your choice: 
"""


def menu():
    """
    Display menu options
    :return: None
    """
    choice = int(input(SELECT_CHOICE))
    while choice!=6:
        if choice==1:
            create_product()
        elif choice==2:
            delete_product()
        elif choice==3:
            update_product()
        elif choice==4:
            select_product()
        elif choice==5:
            display_products()
        choice = int(input(SELECT_CHOICE))

menu()
