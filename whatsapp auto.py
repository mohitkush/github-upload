from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
#location of text file from which you want to send texts
f = open(r"E:\downloads\friends_season1episode1.txt", "r")
#enter name of your whatsapp contact below 
contact = "friends name here"
#enter location of chromedriver
driver = webdriver.Chrome('E:/downloads/chrome/chromedriver.exe')
driver.get("https://web.whatsapp.com/")
time.sleep(10)
print("Logged In")
time.sleep(3)
inp_xpath_search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
input_box_search = WebDriverWait(driver,1000).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact + Keys.ENTER)
time.sleep(2)

inp_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
for line in f:
    input_box.send_keys(line + Keys.ENTER)
    time.sleep(1)
    try:
        endloop = driver.find_element_by_xpath("//*[text()='Stop']")
        print("found")
        driver.quit()
    except NoSuchElementException:
        print("not found")
        pass
    
        
driver.quit()
