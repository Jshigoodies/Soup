from bs4 import BeautifulSoup
import requests


# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")
#
#     print(doc.prettify())
#
# tag = doc.title
# print("\n"+tag.string)
# print()
# # you can actually change the string in the title tag manually, but i don't see why you
# # would do that in the first place.
#
# tags = doc.find_all('p')
#
# print(tags.__str__())


url = "https://www.newegg.ca/asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-gaming/p/N82E16814126456?Description=3090&cm_re=3090-_-14-126-456-_-Product"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

print(doc.prettify())

prices = doc.find_all(text="$")

for i in prices: # the other 2 in the array is just other gpus
    print()
    print("$" + i.parent.find("strong").string)

