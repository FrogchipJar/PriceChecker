Price Checker

A simple Python script to track prices and availability of products from various international online shops. The data is stored in a local SQLite database, and the script can be easily extended to support more online retailers.
Features

    Tracks product prices and availability.

    Currently supports Amazon, eBay, and ASOS.

    Saves product information in a local SQLite database (products.db).

    Modular design makes it easy to add new shops.

Setup
1. Prerequisites

    Python 3.7 or newer.

    pip for installing packages.

2. Clone the Repository

Clone this repository to your local machine:

git clone <your-repository-url>
cd price-checker

3. Create a Virtual Environment (Recommended)

It's good practice to create a virtual environment to manage project dependencies.

For macOS:

python3 -m venv venv
source venv/bin/activate

4. Install Dependencies

Install the required Python libraries from the requirements.txt file:

pip install -r requirements.txt

Usage
Step 1: Add Products to Track

    Open the add_products.py file in your editor.

    Inside the main() function, you will see example Product objects.

    Replace the placeholder URLs (<URL_...> or "") with the direct URLs of the products you wish to track.

    You can add as many products as you like by creating new Product objects and calling db.add_product() for each.

After editing the file, run it once to populate your database:

python add_products.py

This will create a products.db file in your project directory.
Step 2: Check Prices

To check the current prices and availability of all products in your database, run the main.py script:

python main.py

The script will loop through your products and print the fetched data to the console.
How to Extend (Add a New Shop)

    models.py: Add a new URL field to the Product class (e.g., new_shop_url: str = "").

    database.py: Update the CREATE TABLE and INSERT SQL statements to include a column for the new shop.

    prices.py: Create a new method in the Prices class for the new shop (e.g., def new_shop(self):). You will need to inspect the shop's product page HTML to find the correct selectors for the price and availability.

    main.py: In the main() function, add a call to your new method in the Prices class to fetch and display the data.