from bs4 import BeautifulSoup
import requests

URL = "https://wowpedia.fandom.com/wiki/Zul%27jin"


soup = BeautifulSoup(requests.get(URL).content, "html.parser")
print(soup)
table = soup.find("table", class_="infobox darktable")
print(table)
# Remove all the footnotes from the table using the `decompose()` method
for tag in table.find_all(class_="reference"):
    tag.decompose()

for th in table.find_all("th")[1:]:  # <-- Using `[1:]` since we don't want the image
    print(f"{th.text}:  {th.next_sibling.get_text(strip=True)}")