import requests
from bs4 import BeautifulSoup
from models import Product, ShopResponse
import re


class Prices:
    """
    Contains methods for scraping product prices and availability from various online shops.
    Note: Web scraping is fragile. If a website changes its HTML structure,
    these methods will need to be updated.
    """

    def __init__(self, product: Product):
        self.product = product
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def _get_soup(self, url: str) -> BeautifulSoup | None:
        """Fetches a URL and returns a BeautifulSoup object, or None on error."""
        if not url:
            return None
        try:
            page = requests.get(url, headers=self.headers, timeout=10)
            page.raise_for_status()
            return BeautifulSoup(page.content, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def amazon(self) -> ShopResponse:
        """Scrapes the price and availability from an Amazon product page."""
        soup = self._get_soup(self.product.amazon_url)
        if not soup:
            return ShopResponse()

        price = None
        # Find price element
        price_whole = soup.select_one('span.a-price-whole')
        price_fraction = soup.select_one('span.a-price-fraction')
        if price_whole and price_fraction:
            price_str = f"{price_whole.get_text(strip=True)}{price_fraction.get_text(strip=True)}"
            price = float(re.sub(r"[^0-9.]", "", price_str))

        # Find availability element
        availability_div = soup.select_one('#availability')
        availability_text = availability_div.get_text(strip=True).lower() if availability_div else ""
        
        available = "no"
        if "in stock" in availability_text:
            available = "yes"

        return ShopResponse(price=price, available=available)

    def ebay(self) -> ShopResponse:
        """Scrapes the price and availability from an eBay product page."""
        soup = self._get_soup(self.product.ebay_url)
        if not soup:
            return ShopResponse()

        price = None
        price_span = soup.select_one('.x-price-primary span.ux-textspans')
        if price_span:
            price_str = price_span.get_text(strip=True)
            price = float(re.sub(r"[^0-9.]", "", price_str))

        available = "yes" if price else "no"

        return ShopResponse(price=price, available=available)

    def asos(self) -> ShopResponse:
        """Scrapes the price and availability from an ASOS product page."""
        soup = self._get_soup(self.product.asos_url)
        if not soup:
            return ShopResponse()

        price = None
        price_span = soup.find("span", {"data-testid": "current-price"})
        if price_span:
            price_str = price_span.get_text(strip=True)
            price = float(re.sub(r"[^0-9.]", "", price_str))
        
        available = "no"
        if soup.find("button", {"data-testid": "add-to-bag-button"}):
            available = "yes"

        return ShopResponse(price=price, available=available)
