from typing import Literal
from pydantic import BaseModel


class Product(BaseModel):
    """
    Defines the structure for a product, including its name,
    category, and URLs for various online shops.
    """
    name: str
    category: str = ""
    amazon_url: str = ""
    ebay_url: str = ""
    asos_url: str = ""
    # To add a new shop, add a new URL field here.
    # Example: zara_url: str = ""


class ShopResponse(BaseModel):
    """
    Defines the structure for the response received from scraping a shop.
    Includes the price and an availability status.
    """
    price: float = None
    available: Literal["yes", "no", "delayed", "only-in-store", "None"] = None
