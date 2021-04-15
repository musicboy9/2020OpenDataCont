import time
from selenium import webdriver
from bs4 import BeautifulSoup

class weatherData:

    def __init__(self):
        self.driver = webdriver.Chrome("/Users/W11486/Desktop/dev/chromedriver")
        self.driver.get("https://www.weather.go.kr/weather/lifenindustry/life_jisu.jsp")
        page = self.driver.page_source
        self.soup = BeautifulSoup(page, 'html.parser')
        self.driver.quit()

    def getWeatherData(self):
        searchTemp = self.soup.select(".A01_2_list")
        sicknessList = searchTemp[0].findAll("li")

        data = []
        for i in range(2):
            daySickness = sicknessList[i].findAll("span")[1]
            daySicknessPoint = int(daySickness.contents[0][1:3])
            pointText = ""
            if(daySicknessPoint < 55):
                pointText = "관심"
            elif(daySicknessPoint < 71):
                pointText = "주의"
            elif(daySicknessPoint < 86):
                pointText = "경고"
            else:
                pointText = "위험"
            data.append((daySicknessPoint,pointText))

        return data

weather = weatherData()
print(weather.getWeatherData())