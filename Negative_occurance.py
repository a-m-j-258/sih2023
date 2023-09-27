import re

# Define the sentence
#sentence = "The most occurring part, 'dial', needs repairing."

# Define the products and their associated keywords
products = {
    "car": ["mileage", "engine", "maintenance"],
    "cosmetics": ["shelf-life", "allergy", "cream", "consistency", "packaging"],
    "watch": ["dial", "design", "battery", "strap"],
    "tv": ["display", "sound quality", "durability"],
    "phone": ["battery life", "processor", "camera quality", "display", "sound quality", "memory", "charging port"],
    "laptops": ["battery life", "processor", "display", "memory", "sound quality", "charging port", "usb port", "wifi card"]
}

# Initialize a dictionary to store keyword counts
keyword_counts = {keyword: 0 for keywords in products.values() for keyword in keywords}

# Iterate through each product and keyword
for product, keywords in products.items():
    for keyword in keywords:
        # Use regular expressions to find the keyword, case insensitive
        matches = re.findall(rf'\b{re.escape(keyword)}\b', repair_needed, re.IGNORECASE)
        # Update the count for this keyword
        keyword_counts[keyword] += len(matches)

# Find the most occurring keyword in the sentence
most_occurring_keyword = max(keyword_counts, key=keyword_counts.get)

# Find the product associated with the most occurring keyword
associated_product = [product for product, keywords in products.items() if most_occurring_keyword in keywords][0]

# Print the associated product
print("Associated Product:", associated_product.capitalize())
