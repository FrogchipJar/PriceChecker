import sqlite3
from models import Product


class Database:
    """Handles all database operations for the price checker."""

    def __init__(self, db_name: str = "products.db"):
        """Initializes the database connection and creates the table if it doesn't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                product_category TEXT,
                amazon_url TEXT,
                ebay_url TEXT,
                asos_url TEXT
            )
            """
        )
        self.conn.commit()

    def add_product(self, product: Product):
        """Adds a new product to the database."""
        self.cur.execute(
            """
            INSERT INTO products (name, product_category, amazon_url, ebay_url, asos_url)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                product.name,
                product.category,
                product.amazon_url,
                product.ebay_url,
                product.asos_url,
            ),
        )
        self.conn.commit()
        print(f"Added '{product.name}' to the database.")

    def get_product_by_id(self, product_id: int) -> Product:
        """Retrieves a single product from the database by its ID."""
        row = self.cur.execute(
            "SELECT * FROM products WHERE id = ?", (product_id,)
        ).fetchone()

        if row:
            return Product(
                name=row[1],
                category=row[2],
                amazon_url=row[3],
                ebay_url=row[4],
                asos_url=row[5],
            )
        return None

    def get_all_product_ids(self) -> list[int]:
        """Returns a list of all product IDs in the database."""
        results = self.cur.execute("SELECT id FROM products").fetchall()
        return [row[0] for row in results]

    def __del__(self):
        """Closes the database connection when the object is destroyed."""
        self.conn.close()
