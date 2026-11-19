
from inventory import (
    add_product,
    view_products,
    search_product,
    update_product,
    delete_product
)

from reports import (
    low_stock_report,
    inventory_report
)


def main():

    while True:

        print("\n")
        print("=" * 45)
        print("       INVENTORY MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Low Stock Report")
        print("7. Inventory Report")
        print("8. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            low_stock_report()

        elif choice == "7":
            inventory_report()

        elif choice == "8":
            print("Thank you for using Inventory Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 8.")


if __name__ == "__main__":
    main()
