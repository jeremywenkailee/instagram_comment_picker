import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
from dotenv import load_dotenv
import os
import random



load_dotenv()
# print(os.getenv('USERNAME_IG'))
# print(os.getenv('PASSWORD_IG'))

ig_url = sys.argv[1]

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/?next=%2Fp%2FCik64zCJ61d%2F&source=desktop_nav')
driver.implicitly_wait(5)

def check_exists_by(locator, descriptor):
    if locator == 'xpath':
        try:
            driver.find_element(By.XPATH, descriptor)
        except NoSuchElementException:
            return False
        return True
    
    elif locator == 'cssselector':
        try:
            driver.find_element(By.CSS_SELECTOR, descriptor)
        except NoSuchElementException:
            return False
        return True

def check_entry(descriptor):
    try:
        entry.find_element(By.XPATH,descriptor)
    except NoSuchElementException:
        return False
    return True        



username = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
password = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
login = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div')

username.send_keys(os.getenv('USERNAME_IG'))
password.send_keys(os.getenv('PASSWORD_IG'))
login.click()

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img")))
driver.get(ig_url)

while check_exists_by("cssselector",'[aria-label="Load more comments"]'):
    more_comments = driver.find_element(By.CSS_SELECTOR,'[aria-label="Load more comments"]')
    more_comments.click()
    # time.sleep(2)

entries = []

list = driver.find_elements(By.CLASS_NAME,"_a9ym")
for entry in list:
    if check_entry(".//div/li/div/div/div[2]/div[1]/span/a"):
        entry_name = entry.find_element(By.XPATH,".//div/li/div/div/div[2]/h3/div/span/a").text
        entries.append(entry_name)
    else:
        continue

print(entries)
chosen_winner = random.randint(0,len(entries))

print("WINNER FOR GIVEAWAY:" + str(entries[chosen_winner]))


# print(list)
# driver.close()