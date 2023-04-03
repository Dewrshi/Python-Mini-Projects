import requests
from bs4 import BeautifulSoup

# Enter the search query
search_query = input("Enter the search query: ")

# Generate the Google search URL
url = "https://www.google.com/search?q=" + search_query

# Send a request to the URL and get the HTML response
response = requests.get(url)

# Use BeautifulSoup to parse the HTML response
soup = BeautifulSoup(response.content, "html.parser")

# Extract the search results
search_results = soup.find_all("div", class_="g")

# Create a file to store the search results
file = open(search_query + ".txt", "w")

# Loop through the search results and extract the text
for result in search_results:
    text = result.find("a").text
    file.write(text + "\n")

# Close the file
file.close()
