# Entry point for the MiniMart data reporting system

from report_generator import generate_report
from utils import view_orders
print("📚 Welcome to the MiniMart reporting.")

while True:
    print("\n1. View Orders\n2. Generate Reports\n3.Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        view_orders()
    elif choice == "2":
        generate_report()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")