from selenium import webdriver
import random
option = webdriver.ChromeOptions()
option.add_argument("-incognito")

mails =["konrad374@gmail.com","grazyna123@gmail.com",'zenek234@gmail.com',"jacek456@gmail.com"]

a = random.randint(0,3)
buton_range=random.randint(0,2)
browser=webdriver.chrome(executable_path="chromedriver.exe",options=option)
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfg-un5ZEzQe7y_EOZVeTrVGa1sCX-MjYDkfPqNvOLqTRNl6Q/viewform")

textboxes=browser.find_element_by_class_name("quantumWizTextinputPaperinputInput")
submit=browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")


textboxes[0].send_keys(mails[a])
submit.click()


