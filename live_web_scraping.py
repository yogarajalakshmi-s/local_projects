from bs4 import BeautifulSoup
import requests

yc_webpage = requests.get("https://news.ycombinator.com/")
# print(yc_webpage.text)

soup = BeautifulSoup(yc_webpage.text, "html.parser")

# Both returns the same output
# print(soup.select_one(selector=".athing .titleline a").getText())
# print(soup.find(name="span", class_="titleline").find(name="a").getText())

articles = soup.select(selector=".athing .titleline a")
print(articles)
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_score = max(article_upvotes)
index = article_upvotes.index(max_score)

print(article_texts[index])
print(article_links[index])
print(article_upvotes)
# print(max(article_upvotes))
