#-*- coding:utf-8 -*-

from xml.etree import ElementTree   # xml 파싱 모듈 import
tree = ElementTree.parse("testSeoul.xml") # 기상청 정보를 xml 형식으로 파싱
root = tree.getroot()               # xml의 root 요소를 추출
print(root)

for data in root.findall("channel/item/description/body/data"):
    if(data.find("hour").text == "3" and data.find("day").text == "2"):
        tmEf = data.find("tmx").text
        print(tmEf)
    
    
