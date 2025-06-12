"""
Maintaining temporary database using list of dictionaries
for products
"""
products=[]
ref = iter(range(1, 101))

def create_product(product_name,product_price):
    """
    Create product to add product with name and price
    :return: None
    """
    product_id=next(ref)
    products.append({"id":product_id,"name":product_name,"price":product_price})

def delete_product(product_id):
    """
    Delete product based on product id
    :return: None
    """
    for each_product in products:
        if each_product["id"]==product_id:
            print(f"{each_product['name']} with product_id {each_product['id']}\
            removed from inventory!")
            products.remove(each_product)

def update_product(product_id,product_price):
    """
    Update product price based on product id
    :return: None
    """
    for each_product in products:
        if each_product["id"] == product_id:
            each_product["price"]=product_price


def select_product(product_id):
    """
    To check whether product exists in inventory based on product id
    :return: None
    """
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
