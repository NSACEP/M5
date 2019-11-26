import requests
import bs4

url = "https://www.foodpanda.co.th/restaurants/lat/13.723084/lng/100.514919/city/Krung%20Thep%20Maha%20Nakhon/address/Assumption%2520Cathedral%252C%2520Bangkok%252C%252057%2520Oriental%2520Ave%252C%2520Khwaeng%2520Bang%2520Rak%252C%2520Khet%2520Bang%2520Rak%252C%2520Krung%2520Thep%2520Maha%2520Nakhon%252010500%252C%2520Thailand/Oriental%2520Avenue%2520Alley/Assumption%2520Cathedral%252C%2520Bangkok%252057?postcode=Khwaeng+Bang+Rak"
r = requests.get(url).text
soup = bs4.BeautifulSoup(r,"html.parser")

def proccessRating(r):
    return float(r.text.split("/")[0]) if r else 0

def processCount(c):
    return float(c.text) if c else 0

data = []
for span in soup.find_all("span",attrs={"class": "headline"}):
    name = span.find("span",attrs={"class": "name fn"})
    rating = span.find("span", attrs={"class": "rating"})
    count = span.find("span", attrs={"class": "count"})

    data.append([name.text, proccessRating(rating), processCount(count)])

data.sort(key=lambda x: x[2])
print(data)







