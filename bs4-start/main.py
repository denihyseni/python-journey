from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")


soup = BeautifulSoup(response.text , "html.parser")

news_tag = soup.select("span.titleline a")[0]
news_link = news_tag.get("href")
news_text = news_tag.getText()
news_upvote = soup.find(name="span",class_="score").getText()
print(news_text)
print(news_link)
print(news_upvote)


























#
# with open("website.html") as website:
#     file  = website.read()
#
# soup = BeautifulSoup(file, "html.parser")
# # print(soup.title)
# # print(soup.prettify())
#
# # all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     print(tag.text)
#
# heading = soup.find(name="h1",id="name")
# print(heading.text)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)
#
# company_url = soup.select_one(selector="#name")
# print(company_url)