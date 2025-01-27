import os
import random
import re

# Base directory containing markdown files
TARGET_DIR = "./Success"
OUTPUT_FILE = "./daily_random_link.md"  # File to save the random link

def extract_links_from_file(filepath):
    """Extract Markdown links from a file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    # Extract links in the format [text](url)
    return re.findall(r'\[.*?\]\((.*?)\)', content)

def get_all_links(directory):
    """Recursively gather all links from markdown files in the given directory."""
    links = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # Only process .md files
                filepath = os.path.join(root, file)
                links.extend(extract_links_from_file(filepath))
    return links

def main():
    # Extract all links from the markdown directory
    links = get_all_links(TARGET_DIR)
    if not links:
        print("No links found in the markdown files.")
        return
    
    # Randomly select one link
    random_link = random.choice(links)
    
    # Write the selected link to the output file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write(f"Here is a random link from the repository:\n\n{random_link}\n")
    print(f"Random link written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
