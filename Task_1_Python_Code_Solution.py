# Steps to use the code
# 1 - Enter the quantity of products asked repectively.
# 2 - Enter "yes" or "no" for gift wrapping and press enter.


# Make a list for the Products with Product Name and Price
list_of_product = {
    "A": 20,
    "B": 40,
    "C": 50
}


# Make a function for bulk_5_discount with the required condition
def bulk_5_discount(quantity_of_products):
    # Make the list of Product Name
    key_list = list(quantity_of_products.keys())
    # Make the list of Product Quantity
    val_list = list(quantity_of_products.values())
    # Find the product with Maximum Quantity
    position = val_list.index(max(val_list))
    # Fetch the price from list of product and multiply it with the Maximum Quantity Product
    product_total_amount = list_of_product[key_list[position]] * max(val_list)
    # Return the 5% discount applied
    return (product_total_amount * (-0.05))


# Make a function for bulk_10_discount with the required condition
def bulk_10_discount(products_total_amount):
    # Return the 10% discount applied on total cart
    return (products_total_amount*(-0.1))


# Make a function for tiered_50_discount with the required condition and return the Product total amount
def tiered_50_discount(quantity_of_products):
    # Initialize the total discount with 0
    total_discount = 0
    # Iterate over the quantity_of_products list
    for key,value in quantity_of_products.items():
        # If the quantity of any product is greater than 15 apply the condition
        if value > 15:
            # 50% Discount applied after the 15th item
            total_discount += (value-15)*list_of_product[key]*0.5
    # Return the total discount applied
    return (total_discount*-1)


# Make a function applicable_discounts and apply all the condtion to get minimum ammount and maximum discount
def applicable_discounts(quantity_of_products,product_total_quantity,products_total_amount):
    # Make the list for discounts
    discounts = []
    # Condition for getting flat_10_discount
    if products_total_amount >200:
        discounts.append(["flat_10_discount",-10])
    # Condition for getting bulk_5_discount
    if max(quantity_of_products.values()) > 10:
        discounts.append(["bulk_5_discount",bulk_5_discount(quantity_of_products)])
    # Condition for getting bulk_10_discount
    if product_total_quantity>20:
        discounts.append(["bulk_10_discount",bulk_10_discount(products_total_amount)])
    # Condition for getting tiered_50_discount
    if (product_total_quantity > 30) and (max(quantity_of_products.values()) > 15):
        discounts.append(["tiered_50_discount",tiered_50_discount(quantity_of_products)])
    # Return discounts array
    return discounts


# Make a function best_discount for getting best discount and maximum discount
def best_discount(discounts_applicable):
    # if there is no discount_applicable then return the required prompt
    if discounts_applicable == []:
        return "No Discount",0
    # Initialize the best_dis string
    best_dis = ""
    # Initialize the best_amount with 0
    best_amount = 0
    # Iterate through the discount_applicable list and find the minimum discount
    for discount,amount in discounts_applicable:
        if abs(best_amount) < abs(amount):
            best_amount = amount
            best_dis = discount
    # Return best discount with best amount
    return best_dis,best_amount


# Make a function total_amount for multiplying qunatity_of_product and list_of_product
def total_amount(quantity_of_products):
    # Initialize the total with 0
    total = 0
    # Iterate the quantity_of_product and get total amount
    for i in quantity_of_products.keys():
        total+= quantity_of_products[i]*list_of_product[i]
    # Return the total amount
    return total


# Make a function for gift wrap fee is $1 per unit.
def gift_wrap_fee(product_total_quantity):
    # Return the total amount after adding gift wrap fee
    return (product_total_quantity*1)


# Make a function for Shipping fee, 10 units can be packed in one package,
# and the shipping fee for each package is $5.
def shipping_fee(product_total_quantity):
    # apply the condition for shipping fee
    if product_total_quantity%10==0:
        return (product_total_quantity/10)*5
    else:
        return ((product_total_quantity//10)+1)*5


# Make a function cart which contain all the details about the Products and billing
def cart(quantity_of_products,gift_wrap):
    # Total quantity of product
    product_total_quantity = sum(quantity_of_products.values())
    # Total amount of product
    products_total_amount = total_amount(quantity_of_products)
    # Apply the discount
    discounts_applicable = applicable_discounts(quantity_of_products,product_total_quantity,products_total_amount)
    # top_discount selected and discount_amount applied
    top_discount,discount_amount = best_discount(discounts_applicable)
    # Initialize the fee_gift_wrap with 0
    fee_gift_wrap = 0
    # if gift_wrap is yes then apply gift wrap function
    if gift_wrap=="yes":
        fee_gift_wrap = gift_wrap_fee(product_total_quantity)
    # Amount after Shipping charges
    shipping_charge = shipping_fee(product_total_quantity)
    # grand Total of all
    grand_total = products_total_amount + discount_amount + shipping_charge + fee_gift_wrap
    # Return Product_total_amount, top_discount, discount_amount, fee_gift_wrap, shipping_charges, grand_total
    return products_total_amount, top_discount, discount_amount, fee_gift_wrap, shipping_charge, grand_total





# Initialize the Quantity of products
quantity_of_products = {"A":0,"B":0,"C":0}
# Iterate the quantity of products and print
for i in quantity_of_products.keys():
    quantity_of_products[i] = int(input(f"Quantity of Product {i} = "))

# Gift wrap prompt for getting the desired condition
gift_wrap = input("Do you want a gift wrap yes or no ? ")

# Then the program will show / output below details.
# The product name, quantity & total amount of that product.
# Subtotal
# The discount name applied & the discount amount.
# The shipping fee & the gift wrap fee.
# Total

print("\n************************** cart details **********************************\n")

# Initialize all
subtotal , top_discount , discount_amount , fee_gift_wrap , shipping_charge , grand_total = cart(quantity_of_products,gift_wrap)
print(f"{'Product Name':<15} {'Quantity':<10} {'Amount':<15}")

# Iterate the quantity_of_products list
for key,value in quantity_of_products.items():
    product_amount = value*list_of_product[key]
    print(f"{key:<15} {value:<10} {product_amount:<15}")
print()
# Print the Subtotal, top_discount, discount_amount, fee_gift_wrap, shipping_charge, grand_total
print(f"{'Subtotal':<26} {subtotal:<15}")
print(f"{top_discount:<26} {discount_amount:<15}")
print(f"{'Shipping Charge':<26} {shipping_charge:<15}")
print(f"{'Gift Wrap Fee':<26} {fee_gift_wrap:<15}")
print(f"\n{'Grand Total':<26} {grand_total:<15}")


# Sample Output

# Quantity of Product A = 32
# Quantity of Product B = 21
# Quantity of Product C = 11
# Do you want a gift wrap yes or no ? yes

# ************************** cart details **********************************

# Product Name    Quantity   Amount         
# A               32         640            
# B               21         840            
# C               11         550            

# Subtotal                   2030           
# tiered_50_discount         -290.0         
# Shipping Charge            35             
# Gift Wrap Fee              64             

# Grand Total                1839.0         
