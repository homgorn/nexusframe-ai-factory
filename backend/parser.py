import asyncio
from typing import Dict, Any, List
from playwright.async_api import async_playwright
import json
import logging

logger = logging.getLogger(__name__)

class ListingParser:
    """Parses real estate listings from popular portals."""
    
    @classmethod
    async def parse(cls, url: str) -> Dict[str, Any]:
        """Parse a given URL and extract property details."""
        logger.info(f"Starting to parse URL: {url}")
        
        async with async_playwright() as p:
            # Use firefox or webkit if chromium is blocked by anti-bot, but chromium is default
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            page = await context.new_page()
            
            result = {
                "title": "",
                "price": "",
                "address": "",
                "area": "",
                "rooms": "",
                "images": []
            }
            
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                await asyncio.sleep(2) # Wait for dynamic content to load
                
                # Determine portal based on URL
                if "cian.ru" in url:
                    result = await cls._parse_cian(page)
                elif "avito.ru" in url:
                    result = await cls._parse_avito(page)
                else:
                    # Generic fallback parser
                    result = await cls._parse_generic(page)
                    
            except Exception as e:
                logger.error(f"Error parsing URL {url}: {str(e)}")
                raise e
            finally:
                await browser.close()
                
            return result
            
    @staticmethod
    async def _parse_cian(page) -> Dict[str, Any]:
        """Specific parser for CIAN."""
        result = {}
        
        # Title
        try:
            title_element = await page.query_selector('h1')
            result["title"] = await title_element.inner_text() if title_element else "Квартира"
        except:
            result["title"] = "Неизвестно"
            
        # Price
        try:
            # CIAN usually uses specific data-name attributes for price
            price_element = await page.query_selector('[data-testid="price-amount"]')
            if not price_element:
                price_element = await page.query_selector('span[itemprop="price"]')
            result["price"] = await price_element.inner_text() if price_element else ""
        except:
            result["price"] = ""
            
        # Address
        try:
            address_element = await page.query_selector('address')
            result["address"] = await address_element.inner_text() if address_element else ""
            # Clean up the address (often contains "На карте")
            if "На карте" in result["address"]:
                result["address"] = result["address"].replace("На карте", "").strip()
        except:
            result["address"] = ""
            
        # Images
        try:
            images = []
            # Find image elements. CIAN often uses picture > img or div > img for galleries
            img_elements = await page.query_selector_all('img[src*="cdn-p.cian.site"]')
            for img in img_elements:
                src = await img.get_attribute('src')
                if src and src not in images:
                    # Try to get high-res version if possible by modifying the URL (CIAN specific logic)
                    high_res = src.replace('2.jpg', '1.jpg').replace('-2.jpg', '-1.jpg')
                    images.append(high_res)
            result["images"] = images[:10] # Limit to 10 images
        except:
            result["images"] = []
            
        # Area and Rooms - usually embedded in the title or a specific summary block
        title_lower = result["title"].lower()
        if "квартира" in title_lower:
            parts = title_lower.split(",")
            if len(parts) > 0:
                result["rooms"] = parts[0].strip().capitalize()
            if len(parts) > 1:
                result["area"] = parts[1].strip()
        else:
            result["area"] = "Неизвестно"
            result["rooms"] = "Неизвестно"
            
        return result

    @staticmethod
    async def _parse_avito(page) -> Dict[str, Any]:
        """Specific parser for Avito."""
        # Note: Avito has strong anti-bot protection. This is a basic attempt.
        result = {}
        
        try:
            title_element = await page.query_selector('h1[data-marker="item-view/title-info"]')
            result["title"] = await title_element.inner_text() if title_element else "Объявление"
        except:
            result["title"] = "Неизвестно"
            
        try:
            price_element = await page.query_selector('span[data-marker="item-view/item-price"]')
            result["price"] = await price_element.inner_text() if price_element else ""
        except:
            result["price"] = ""
            
        try:
            address_element = await page.query_selector('div[itemprop="address"]')
            result["address"] = await address_element.inner_text() if address_element else ""
        except:
            result["address"] = ""
            
        try:
            images = []
            img_elements = await page.query_selector_all('div[data-marker="image-frame/image-wrapper"] img')
            for img in img_elements:
                src = await img.get_attribute('src')
                if src and src not in images:
                    images.append(src)
            result["images"] = images[:10]
        except:
            result["images"] = []
            
        result["area"] = "См. описание"
        result["rooms"] = "См. название"
        
        return result

    @staticmethod
    async def _parse_generic(page) -> Dict[str, Any]:
        """Generic fallback parser using common semantic tags."""
        result = {}
        
        try:
            title_element = await page.query_selector('h1')
            result["title"] = await title_element.inner_text() if title_element else "Объект недвижимости"
        except:
            result["title"] = "Объект"
            
        try:
            # Try to find something that looks like a price
            price_element = await page.query_selector('xpath=//*[contains(text(), "₽") or contains(text(), "руб")]')
            result["price"] = await price_element.inner_text() if price_element else "Цена по запросу"
        except:
            result["price"] = ""
            
        try:
            address_element = await page.query_selector('address')
            result["address"] = await address_element.inner_text() if address_element else "Адрес не указан"
        except:
            result["address"] = ""
            
        try:
            images = []
            # Get largest images on the page
            img_elements = await page.query_selector_all('img')
            for img in img_elements:
                src = await img.get_attribute('src')
                width = await img.get_attribute('width')
                # Try to filter out small icons
                if src and (width is None or (width.isdigit() and int(width) > 200)):
                    if src.startswith('http') and src not in images:
                        images.append(src)
            result["images"] = images[:10]
        except:
            result["images"] = []
            
        result["area"] = ""
        result["rooms"] = ""
        
        return result

# Example usage:
# async def main():
#     parser = ListingParser()
#     data = await parser.parse("https://cian.ru/...")
#     print(data)
