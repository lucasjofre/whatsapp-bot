import requests
from bs4 import BeautifulSoup

# url = r"https://screenrant.com/every-marvels-spider-man-2-suit-peter-parker/#secret-wars-civil-war-suit"
url = "https://httpbin.org"

# Add headers to prevent being blocked from the website
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())