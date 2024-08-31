import requests
from bs4 import BeautifulSoup
import csv


def get_product_info(url) :
	# Send HTTP request to the URL
	response = requests.get ( url )
	# Parse HTML content
	soup = BeautifulSoup ( response.text, 'html.parser' )

	products = []

	# Find all product containers
	product_containers = soup.find_all ( 'div', class_='s-result-item' )

	for container in product_containers :
		# Extract product name
		name = container.find ( 'span', class_='a-size-medium' ).text.strip ( )

		# Extract product price
		price_element = container.find ( 'span', class_='a-price' )
		if price_element :
			price = price_element.find ( 'span', class_='a-offscreen' ).text.strip ( )
		else :
			price = 'N/A'

		# Extract product rating
		rating_element = container.find ( 'span', class_='a-icon-alt' )
		if rating_element :
			rating = rating_element.text.strip ( )
		else :
			rating = 'N/A'

		# Extract product URL
		product_url = container.find ( 'a', class_='a-link-normal' )['href']
		full_product_url = 'https://www.amazon.com' + product_url

		# Extract product availability
		availability_element = container.find ( 'span', class_='a-size-base' )
		if availability_element :
			availability = availability_element.text.strip ( )
		else :
			availability = 'N/A'

		# Extract seller information
		seller_element = container.find ( 'div', class_='a-row a-size-base' )
		if seller_element :
			seller_info = seller_element.text.strip ( )
		else :
			seller_info = 'N/A'

		# Append product information to the list
		products.append (
			{'Name' : name, 'Price' : price, 'Rating' : rating, 'URL' : full_product_url, 'Availability' : availability,
			 'Seller Info' : seller_info} )

	return products


def save_to_csv(products, filename='products.csv') :
	with open ( filename, 'w', newline='', encoding='utf-8' ) as csvfile :
		fieldnames = ['Name', 'Price', 'Rating', 'URL', 'Availability', 'Seller Info']
		writer = csv.DictWriter ( csvfile, fieldnames=fieldnames )

		writer.writeheader ( )
		for product in products :
			writer.writerow ( product )


if __name__ == "__main__" :
	url = 'https://www.amazon.com/s?k=laptop'  # Example URL of Amazon's laptop category
	products = get_product_info ( url )
	save_to_csv ( products )
	print ( "Product information has been scraped and saved to 'products.csv'." )
