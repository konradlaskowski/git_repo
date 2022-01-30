from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")


mails =["konrad374@gmail.com","grazyna123@gmail.com",'zenek234@gmail.com',"jacek456@gmail.com"]
names = ["jacek!", "paulina", "rafal", "alicja", "maciek"]
b = 1

s=Service("chromedriver.exe")
browser = webdriver.Chrome(service=s, options=option)

while b > 0:
    b -= 1

    a = random.randint(0,3)
    c = random.randint(0,4)
    buton_range=random.randint(0,2)

    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfg-un5ZEzQe7y_EOZVeTrVGa1sCX-MjYDkfPqNvOLqTRNl6Q/viewform")

    textboxes=browser.find_element(By.CLASS_NAME, "quantumWizTextinputPaperinputPlaceholder")
    #textboxes2=browser.find_element(By.CLASS_NAME, "quantumWizTextinputPapertextareaInput")

    #submit=browser.find_element(By.CLASS_NAME, "appsMaterialWizButtonPaperbuttonContent")

    print(textboxes)
    textboxes[0].send_keys(mails[a])
    #textboxes2[0].send_keys(names[c])
    #submit.click()


