import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

url = "https://www.youtube.com/user/SSundee/videos?view=0&sort=p&flow=grid"
driver = webdriver.Chrome(options = options, service = Service(ChromeDriverManager().install()))
driver.get(url)

driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button/span').click()

videos = driver.find_elements(By.CLASS_NAME, value = 'style-scope ytd-grid-video-renderer')

"""//*[@id="video-title"]"""

video_list = []

for video in videos:
    title = video.find_elements(By.ID, 'video-title')
    uptime = video.find_elements(By.XPATH, './/*[@id="metadata-line"]/span[2]')
    views = video.find_elements(By.XPATH, './/*[@id="metadata-line"]/span[1]')

    vid_item = {
        "title" : title[0].text,
        "views" : views[0].text,
        "uptime" : uptime[0].text 
    }

    video_list.append(vid_item)

df = pd.DataFrame(video_list)
df.to_excel("D:\Pythonprograms\output.xlsx")
print(df)

