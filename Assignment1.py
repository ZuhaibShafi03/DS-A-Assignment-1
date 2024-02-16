#Zuhaib Shafi - 100820952
#Algorithms and Data Structures Assignment 1
# Define a Product class with attributes for ID, name, price, and category
class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

# Function to load products from a file and return a list of Product objects
def load_products(file_path):
    products = []
    with open(file_path, 'r') as file:  # Open file for reading
        for line in file:  # Iterate over each line in the file
            # Split each line by comma and create a Product object
            product_id, name, price, category = line.strip().split(',')
            products.append(Product(product_id, name, float(price), category))
    return products  # Return the list of Product objects

# Function to add a new product to the list of products
def insert_product(products, new_product):
    products.append(new_product)

# Function to update an existing product's details
def update_product(products, product_id, **updates):
    for product in products:  # Iterate over the products
        if product.product_id == product_id:  # Find the product by ID
            product.__dict__.update(updates)  # Update the product's attributes
            break

# Function to remove a product from the list by its ID
def delete_product(products, product_id):
    products[:] = [product for product in products if product.product_id != product_id]

# Function to search for products that match given criteria
def search_product(products, **query):
    result = []
    for product in products:  # Iterate over the products
        # If product matches all query criteria, add to result list
        if all(getattr(product, key) == value for key, value in query.items()):
            result.append(product)
    return result  # Return the list of matching products

# Function to sort the products by their price using Bubble Sort algorithm
def bubble_sort(products):
    n = len(products)  # Get the number of products
    for i in range(n):
        for j in range(0, n-i-1):  # Perform Bubble Sort on the list
            # If the current product is more expensive than the next, swap them
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]

# Main function to orchestrate the loading and processing of product data
def main():
    products = load_products('product_data.txt')  # Load products from file
    # Example operations 
    insert_product(products, Product("0044", "T-shirt", 10.99, "Clothing"))
    update_product(products, "0044", price=11.99)
    # delete_product(products, "0044")
    found_products = search_product(products, name="T-shirt")
    bubble_sort(products)  # Sort products by price
    # Print sorted products
    for product in products:
        print(f"{product.product_id}, {product.name}, {product.price}, {product.category}")

# Check if the script is run directly and if so, call the main function
if __name__ == "__main__":
    main()