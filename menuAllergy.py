#-*- coding:utf-8 -*-

class menuAllergy:

    menuName = []
    allergyComment = {"raw food":["무침","생채","모듬쌈","샐러드"],"raw":"은(는) 비가열음식입니다. ", "8":"게", "9":"새우", "15":"닭고기", "17":"오징어", "18":"조개류", "include":"이(가) 포함되어 있습니다."}

    def __init__(self):
        self.menuName = []

    def addMenu(self,menuName):
        # menuName: Korean str
        self.menuName.append(menuName)
    
    def menuComment(self,menu):
        comment = ""
        spaceIndex = menu.find(" ")
        if (spaceIndex == -1):
            spaceIndex = len(menu)
        name = menu[:spaceIndex]
        allergyMenu = []

        for food in self.allergyComment["raw food"]:
            if (food in menu):
                comment += "\n" + name + self.allergyComment["raw"]
        # 비가열식품 확인
        for allergy in list(self.allergyComment):
            if (allergy in menu):
                allergyMenu.append(self.allergyComment[allergy])
        # 각 재료에 해당하는 번호를 포함하고 있으면 그 재료를 allergyMenu list에 저장
        if len(allergyMenu) > 0:
            comment += "\n" + name + "은(는)"
            for allergy in allergyMenu:
                comment += " " + allergy
            comment += "을(를) 포함하고 있습니다."
        return comment  

    def totalComment(self):
        message = "\n"
        for menu in self.menuName:
            message += self.menuComment(menu)
        if message != "\n":
            message += "\n" + "재료 손질 시 식중독 감염에 유의하세요." + "\n"
        return message


