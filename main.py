from typing import List
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
import os

cwd =os.getcwd()
linksn = []
links= []
check_Links = []
index_of_list = []
x = 0
reallinks = []


with open(rf"{cwd}\Links.txt","r", encoding="utf-8") as file:
    a = file.readlines()
    for i in a:
        linksn.append(i)

for i in linksn:
    a = i.replace("\n","")
    links.append(a)

class deneme:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(chrome_options=self.options,executable_path=rf"{cwd}\chromedriver.exe")
        self.start = 0
        self.lenlinks = len(links)
    
    def downvideo(self):
        self.driver.get("https://yt1s.com/tr12")
        self.driver.implicitly_wait(20)

        self.driver.find_element_by_xpath('//*[@id="s_input"]').send_keys(reallinks[self.start])
        time.sleep(2)
        print("Link Gönderildi")
        self.driver.find_element_by_xpath('//*[@id="btn-convert"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="btn-action"]').click()
        time.sleep(1)
        a.continuedownvideo()

    def continuedownvideo(self):
        try:
            if self.driver.find_element_by_xpath('//*[@id="asuccess"]').text == "İndir":
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@id="asuccess"]').click()
                time.sleep(2)
                self.driver.implicitly_wait(20)
                self.driver.get("https://yt1s.com/tr12")
                self.driver.implicitly_wait(20)
        except selenium.common.exceptions.NoSuchElementException:
            print("Süre Aşımı")
            a.continuedownvideo()

        if self.start + 1 == self.lenlinks:
            print("İşlem tamamlandı")
        else:
            self.start +=1
            time.sleep(1)
            a.downvideo()
    
    def convertSpotoYt(self):
        firstIndex = 0
        secondIndex = 0
        countofturn = 1
        while countofturn <= len(index_of_list):
            self.driver.get(links[int(index_of_list[firstIndex])])
            self.driver.implicitly_wait(20)
            try:
                text = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[1]/div[5]/span/h1').text
                text2 = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[1]/div[5]/div/div/a').text
            except selenium.common.exceptions.NoSuchElementException:
                print("Şarkının yapımcısı alınamadı.")
                pass                
            self.driver.get("https://www.youtube.com")
            time.sleep(1)
            self.driver.implicitly_wait(20)
            print(f"TEXT2 : {text}")
            print(f"TEXT2: {text2} ")
            self.driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(f"{text} {text2}")
            self.driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
            self.driver.implicitly_wait(20)
            time.sleep(6)
            href = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').get_attribute("href")
            reallinks.append(href)
            countofturn += 1
            if firstIndex < len(index_of_list):
                firstIndex += 1
            else:
                pass
        print(f"İşlem tamam. Linkler: {reallinks}")


for i in links:
    if i.find("spotify") == 13:
        check_Links.append(links[x])
        index_of_list.append(x)
        x += 1
    else:
        x += 1
        continue

y = 0
for i in links:
    if i.find("youtube") == 12:
        reallinks.append(links[y])
        y += 1
    else:
        y += 1
        continue


a = deneme()
a.convertSpotoYt()
a.downvideo()