
from selenium import webdriver
from datetime import date
import pandas as pd
from pathlib import Path

import videos
import subs
import views
import superchat

PATH="chromedriver.exe"
driver = webdriver.Chrome(PATH)

def get_channel_name(url):
    global driver

    driver.get(url)
    channel_name = driver.find_element_by_class_name("name").text
    channel_name = channel_name.replace("/", "").replace(".", " ")
    Path(channel_name).mkdir(exist_ok=True)
    return channel_name

def main():

    id = input("請輸入欲查詢頻道之 Playboard 頁面或是 YouTube 頻道ID/網址：")
    try:
        id = id.split("/")[5]
    except:
        try:
            id = id.split("/")[4]
        except:
            pass
    print(id)
    url = "https://playboard.co/en/channel/{}".format(id)
    channel_name = get_channel_name(url)

    print("Getting information of videos from {}".format(channel_name))
    videos.get_videos_info(driver, url, channel_name)

    try:
        print("Getting information of channel superchats from {}".format(channel_name))
        superchat.get_superchat_info(driver, url, channel_name)
    except:
        print("No superchats.")

    print("Getting information of channel views from {}".format(channel_name))
    views.get_views_info(driver, url, channel_name)

    print("Getting information of channel subs from {}".format(channel_name))
    subs.get_subs_info(driver, url, channel_name)
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    driver.quit()