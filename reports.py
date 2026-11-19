
from storage import load_inventory


def low_stock_report():

    products = load_inventory()

    print("\n--- LOW STOCK REPORT ---")

    if not products:
        print("Inventory is empty!")
        return

    found = False

    for product in products:

        if product["quantity"] <= 5:

            print(
                f"Product: {product['name']} | "
                f"Quantity: {product['quantity']}"
            )

            found = True

    if not found:
        print("No low-stock products!")


def inventory_report():

    products = load_inventory()

    print("\n--- INVENTORY REPORT ---")

    total_products = len(products)

    total_quantity = sum(
        product["quantity"] for product in products
    )

    total_value = sum(
        product["price"] * product["quantity"]
        for product in products
    )

    print("Total Products:", total_products)

    print("Total Stock Quantity:", total_quantity)

    print("Total Inventory Value: Rs.", total_value)
