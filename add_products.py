from database import Database
from models import Product


def main():
    """
    This script adds products to the database.
    Edit the Product objects below with the details of the items you want to track.
    Run this script once to populate the database.
    """
    db = Database()

    # --- ADD YOUR PRODUCTS HERE ---

    # Example 1: A tech gadget available on Amazon and eBay
    product1 = Product(
        name="Logitech MX Master 3S Mouse",
        category="Electronics",
        amazon_url="https://www.amazon.com/Logitech-Master-Wireless-Mouse-Graphite/dp/B09HM94V27/",
        ebay_url="https://www.ebay.com/itm/204297298668"
    )
    db.add_product(product1)

    # Example 2: A fashion item available only on ASOS
    product2 = Product(
        name="Nike Air Force 1 '07",
        category="Fashion",
        asos_url="https://www.asos.com/us/nike/nike-air-force-1-07-sneakers-in-white/prd/200922354"
    )
    db.add_product(product2)

    # Example 3: Add another product
    # product3 = Product(
    #     name="<PRODUCT_NAME>",
    #     category="<PRODUCT_CATEGORY>",
    #     amazon_url="<URL_TO_AMAZON_PRODUCT>",
    #     ebay_url="<URL_TO_EBAY_PRODUCT>",
    #     asos_url="<URL_TO_ASOS_PRODUCT>"
    # )
    # db.add_product(product3)


if __name__ == "__main__":
    main()
