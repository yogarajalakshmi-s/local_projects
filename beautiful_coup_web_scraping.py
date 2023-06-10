# DAY - 45 : WEB SCRAPING USING BEAUTIFUL SOUP MODULE
from bs4 import BeautifulSoup

with open(file="./website.html", encoding="utf8") as file:
    content = file.read()

# print(content)
soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.name, soup.title.string)
print(soup.prettify())
print(soup.ul.prettify())


# Finding and selecting particular elements
# Finding particular element using name
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText())  # Prints the text in the tag
    print(tag.get("href"))  # Prints the link

# Finding particular element using attribute
heading_1 = soup.find(name="h1", id="name")
print(heading_1)

heading_3 = soup.find(name="h3", class_="heading")
print(heading_3.get("class"))

# Finding element using selectors
# Element selector
company_url = soup.select_one(selector="p a")
print(company_url)

# Id selector
name = soup.select_one(selector="#name")
print(name)

# Class selector
headings = soup.select(selector=".heading")
print(headings)

