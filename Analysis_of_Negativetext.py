# Keywords to search for
#keywords = ["", "", "maintenance","shelf-life", "allergy", "pigment", "consistency", "packaging","dial", "design", "battery", "strap","display", "sound quality", "durability","battery life", "processor", "camera quality", "display", "sound quality", "memory", "charging port","battery life", "processor", "display", "memory", "sound quality", "charging port", "usb port", "wifi card"]
keywords=["dial","car","tv","cream","phone","laptop"]
# Initialize a dictionary to store keyword counts
keyword_counts = {keyword: 0 for keyword in keywords}

# Iterate through each sentence and count keyword occurrences
for sentence in sentences:
    for keyword in keywords:
        # Use regular expressions to find the keyword, case insensitive
        matches = re.findall(rf'\b{re.escape(keyword)}\b', sentence, re.IGNORECASE)
        # Update the count for this keyword
        keyword_counts[keyword] += len(matches)

# Find the most occurring keyword
most_occurring_keyword = max(keyword_counts, key=keyword_counts.get)

# Determine if it needs repairing
if keyword_counts[most_occurring_keyword] > 0:
    repair_needed = f"The most occurring part, '{most_occurring_keyword}', needs repairing."
else:
    repair_needed = "No specific part needs repairing."

# Print the keyword counts and repair conclusion
print(repair_needed)
