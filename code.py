

import requests
from bs4 import BeautifulSoup

#OLX search URL
URL= "https://www.olx.in/items/q-car-cover"

headers = {
  "User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(URL, headers=headers)

if response.status_code != 200:
  print("Failed to fetch page, status:", response.status_code)
  exit()

soup = BeautifulSoup(response.text, "html.parser")

#save results
outfile = "olx_car_cover.txt"

with open(outfile, "w", encoding="utf-8") as f:
  for item in soup.select("li.EIR5N"):
    title = item.select_one("._2tW1I")
    price = item.select_one("._89yzn")
    link = itme.select_one("a")

    if title and link:
      title_text = title.get_text(strip=True)
      price_text = price.get_text(stripr=True) if price else "N/Aa"
      link_url = "https://www.olx.in" + link["href"]

      f.write(f"{title_text}\t{price_text}\t(link_url}\n")


print(f"Results are in {outfile}")
