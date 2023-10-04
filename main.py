import asyncio
import os
from nikescraperbykejora.scrapingresult import ProductScraperHandler


async def main():
    # User input for scraping multi products
    target_url_multi = "https://www.nike.com/id/w/mens-1500001-2999999-football-shoes-1gdj0z2952fznik1zy7ok"  # Change with url you want to scrape
    csv_file_name = "Men's Rp1.500.001 - Rp2.999.999 Football Shoes.csv"  # Change with the name of product category you want to scrape, DON'T skip .CSV
    product_count = 14  # Change with product count that displayed on the page
    timeout_seconds = 10  # Change with a higher integer value if scraping fails due to timeout

    # Setting result directory
    project_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_directory)
    result_directory = os.path.join(project_directory, "result")

    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    result_file_path = os.path.join(result_directory, csv_file_name)

    await ProductScraperHandler.multi_product(target_url_multi, result_file_path, product_count, timeout_seconds)

if __name__ == "__main__":
    asyncio.run(main())
