
from storage import load_inventory, save_inventory


def add_product():

    products = load_inventory()

    print("\n--- ADD NEW PRODUCT ---")

    product_id = input("Enter Product ID: ").strip()

    if not product_id:
        print("Product ID cannot be empty!")
        return

    for product in products:
        if product["id"] == product_id:
            print("Product ID already exists!")
            return

    name = input("Enter Product Name: ").strip()

    if not name:
        print("Product name cannot be empty!")
        return

    try:
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative!")
            return

    except ValueError:
        print("Invalid input! Enter valid numbers.")
        return

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

    if save_inventory(products):
        print("Product added successfully!")


def view_products():

    products = load_inventory()

    print("\n--- ALL PRODUCTS ---")

    if not products:
        print("Inventory is empty!")
        return

    print("-" * 75)
    print(f"{'ID':<12}{'NAME':<20}{'PRICE':<15}{'QUANTITY':<12}")
    print("-" * 75)

    for product in products:

        print(
            f"{product['id']:<12}"
            f"{product['name']:<20}"
            f"{product['price']:<15}"
            f"{product['quantity']:<12}"
        )

    print("-" * 75)


def search_product():

    products = load_inventory()

    search = input(
        "Enter Product ID or Name: "
    ).strip().lower()

    found = False

    for product in products:

        if (
            search == product["id"].lower()
            or search in product["name"].lower()
        ):

            print("\nProduct Found!")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

            found = True

    if not found:
        print("Product not found!")


def update_product():

    products = load_inventory()

    product_id = input(
        "Enter Product ID to update: "
    ).strip()

    for product in products:

        if product["id"] == product_id:

            print("\n1. Update Name")
            print("2. Update Price")
            print("3. Update Quantity")

            choice = input("Select option: ").strip()

            if choice == "1":

                name = input("Enter new name: ").strip()

                if not name:
                    print("Name cannot be empty!")
                    return

                product["name"] = name

            elif choice == "2":

                try:
                    price = float(input("Enter new price: "))

                    if price < 0:
                        print("Price cannot be negative!")
                        return

                    product["price"] = price

                except ValueError:
                    print("Invalid price!")
                    return

            elif choice == "3":

                try:
                    quantity = int(
                        input("Enter new quantity: ")
                    )

                    if quantity < 0:
                        print("Quantity cannot be negative!")
                        return

                    product["quantity"] = quantity

                except ValueError:
                    print("Invalid quantity!")
                    return

            else:
                print("Invalid option!")
                return

            if save_inventory(products):
                print("Product updated successfully!")

            return

    print("Product not found!")


def delete_product():

    products = load_inventory()

    product_id = input(
        "Enter Product ID to delete: "
    ).strip()

    product_found = False

    for product in products:

        if product["id"] == product_id:
            product_found = True
            break

    if not product_found:
        print("Product not found!")
        return

    confirm = input(
        "Are you sure you want to delete this product? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Delete operation cancelled!")
        return

    updated_products = [
        product for product in products
        if product["id"] != product_id
    ]

    if save_inventory(updated_products):
        print("Product deleted successfully!")
