import sys
from database import Database
from prices import Prices


def main():
    """
    Main script to check prices for all products stored in the database.
    """
    db = Database()
    product_ids = db.get_all_product_ids()

    if not product_ids:
        print("Database is empty. Please run 'add_products.py' to add items to track.")
        sys.exit(0)

    print(f"Found {len(product_ids)} products to check...")

    for product_id in product_ids:
        product = db.get_product_by_id(product_id)
        if not product:
            continue

        price_checker = Prices(product)

        print(f"\n--- [{product.name}] ---")

        if product.amazon_url:
            amazon = price_checker.amazon()
            print(f"  Amazon:      Price = {amazon.price}, Available = {amazon.available}")

        if product.ebay_url:
            ebay = price_checker.ebay()
            print(f"  eBay:        Price = {ebay.price}, Available = {ebay.available}")

        if product.asos_url:
            asos = price_checker.asos()
            print(f"  ASOS:        Price = {asos.price}, Available = {asos.available}")

    print("\nPrice check complete.")


if __name__ == "__main__":
    main()
