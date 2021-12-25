from bs4 import BeautifulSoup
import requests
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

result = doc.find_all("option")

tag = doc.find("option")

print(tag)
# <option selected="" value="course-type">Course type*</option>

tag['selected'] = 'false'
tag['color'] = 'blue'

print(tag)
# <option color="blue" selected="false" value="course-type">Course type*</option>

different_tags = doc.find_all(["p", "div", "li"])
# print(different_tags)

specific_tag = doc.find(["option"], text="Undergraduate", value="undergraduate") # class_
print(specific_tag)

retag = doc.find(text=re.compile("\$.*"))

print(retag.strip())