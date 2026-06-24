# Part a
print("PART A - Bug Demonstration")


def add_item(item, cart=[]):
    cart.append(item)
    return cart


print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']


#  Part b
print("\nPART B - Fixed Version")


def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print(add_item_fixed("apple"))
print(add_item_fixed("banana"))


# Part c 

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print("Tuple Error:", e)
        print("Tuples are immutable and cannot be modified.")


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)
    return total - discount_amount


# Customer 1
cart1 = create_cart("Aarav", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

# Customer 2
cart2 = create_cart("Riya", 5)

add_to_cart(cart2, "Phone", 30000, 1)

print("\nCustomer 1 Cart")
print(cart1)

print("\nCustomer 2 Cart")
print(cart2)

print("\nCustomer 1 Total:", calculate_total(cart1))
print("Customer 2 Total:", calculate_total(cart2))

# Tuple demonstration
price_info = (1000, "Keyboard")
update_price(price_info, 1200)


