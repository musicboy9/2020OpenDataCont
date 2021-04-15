#-*- coding:utf-8 -*-

import json
from menuAllergy import *

class jsonExtract:

    json_data = []
    time_dict = {0:"brst", 1:"lunc", 2:"dinr"}
    time_message = {0:"의 아침식사 메뉴입니다.", 1:"의 점심식사 메뉴입니다", 2:"의 저녁식사 메뉴입니다"}

    def __init__(self,filename):
        with open(filename, 'rt', encoding='UTF8') as json_file:
            self.json_data = json.load(json_file)

    def messageDateFormat(self,date,time):
        message = "\n" + date[0:4] + "년 " + date[4:6] + "월 " + date[6:8] + "일" + self.time_message[time] + "\n"
        return message

    def getMenu(self,date,time):
        # date: "YYYYMMDD" str type
        # time: 0 for breakfast, 1 for lunch, 2 for dinner
        menu_message = self.messageDateFormat(date,time)
        time_str = self.time_dict[time]
        mAllergy = menuAllergy()

        data_list = self.json_data["DATA"]
        for menu_index in range(len(data_list)):
            date_start_index = 0
            if data_list[menu_index]["dates"] == date:
                date_start_index = menu_index
                for i in range(5):
                    menu_elements = data_list[date_start_index+i][time_str]
                    spaceIndex = menu_elements.find(" ")
                    if (spaceIndex == -1):
                        spaceIndex = len(menu_elements)
                    name = menu_elements[:spaceIndex]
                    menu_message += "\n"+ name
                    
                    mAllergy.addMenu(menu_elements)
                break
        # 식단을 추가하는 부분

        menu_message += mAllergy.totalComment()

        return menu_message
    
    def dateMenu(self,date):
        message = ""
        for i in range(3):
            message += self.getMenu(date,i)
        return message

js = jsonExtract('C:/Users/W11486/Desktop/dev/test.json')

print(js.dateMenu("20191024"))
