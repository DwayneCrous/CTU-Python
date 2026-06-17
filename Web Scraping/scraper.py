import requests
import re
import csv
import json
from bs4 import BeautifulSoup

# The website we want to scrape
url = "https://quotes.toscrape.com/"

try:
    # Send a request to the website and get the response
    response = requests.get(url)

    # Only continue if the request was successful
    if response.status_code == 200:
        # Parse the HTML content so we can search through it
        soup = BeautifulSoup(response.content, "html.parser")
        print("Success!")

        # Save the raw HTML to a file for reference
        with open("raw.html", "w") as file:
            file.write(response.text)
        print("HTML saved to raw.html")

        # Find every quote block on the page
        quotes = soup.find_all("div", class_="quote")

        # This list will hold all the extracted quote data
        data = []

        # Loop through each quote and pull out the text, author, and tags
        for quote in quotes:
            text = re.sub(r'["""]', '', quote.find("span", class_="text").text).strip()
            author = quote.find("small", class_="author").text.strip()
            tags = [tag.text.strip() for tag in quote.find_all("a", class_="tag")]

            # Only add the quote if all three fields are present
            if text and author and tags:
                data.append({
                    "quote": text,
                    "author": author,
                    "tags": tags
                })

        # Print each quote to the console
        for item in data:
            print(f"Quote: {item['quote']}")
            print(f"Author: {item['author']}")
            print(f"Tags: {item['tags']}")
            print("---")

        # Save the data to a CSV file
        with open("output.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
            writer.writeheader()
            writer.writerows(data)
        print("Data saved to output.csv")

        # Save the data to a JSON file
        with open("output.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Data saved to output.json")

        # Flatten all tags and authors into simple lists for analysis
        all_tags = [tag for item in data for tag in item["tags"]]
        all_authors = [item["author"] for item in data]

        # Calculate some basic stats about the scraped data
        most_common_author = max(set(all_authors), key=all_authors.count)
        most_common_tag = max(set(all_tags), key=all_tags.count)
        avg_tags = len(all_tags) / len(data)

        # Print the summary report
        print("\n--- Summary Report ---")
        print(f"1. Total quotes scraped: {len(data)}")
        print(f"2. Unique authors: {len(set(all_authors))}")
        print(f"3. Most common author: {most_common_author}")
        print(f"4. Most common tag: {most_common_tag}")
        print(f"5. Unique tags: {len(set(all_tags))}")
        print(f"6. Average tags per quote: {avg_tags:.1f}")
    else:
        print("Error:", response.status_code)

except Exception as e:
    print("Something went wrong:", e)
