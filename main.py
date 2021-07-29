import time
import selenium
from playsound import playsound
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://tokcount.com/?user=officialdankhumor")

while True:
    start_time = time.time()
    seconds = 10
    old_followers = 0
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > seconds:
            xpaths = ["/html/body/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/span[1]/span[2]/span/span/span",
                      "/html/body/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/span[2]/span[2]/span/span/span",
                      "/html/body/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/span[4]/span[2]/span/span/span",
                      "/html/body/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/span[5]/span[2]/span/span/span",
                      "/html/body/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/span[6]/span[2]/span/span/span"]
            digits = []
            ten_thousands = driver.find_element_by_xpath(xpaths[0])
            digits.append(ten_thousands.text)
            thousands = driver.find_element_by_xpath(xpaths[1])
            digits.append(thousands.text)
            hundreds = driver.find_element_by_xpath(xpaths[2])
            digits.append(hundreds.text)
            tens = driver.find_element_by_xpath(xpaths[3])
            digits.append(tens.text)
            ones = driver.find_element_by_xpath(xpaths[4])
            digits.append(ones.text)
            new_followers = int("".join(x for x in digits))
            if new_followers > old_followers:
                print(f"Total Followers: {new_followers}")
                playsound("/Users/jaxson/PycharmProjects/annoying-follower-bot/mask.mp3")
                old_followers = new_followers
            continue
