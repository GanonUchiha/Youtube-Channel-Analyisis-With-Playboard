
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from datetime import date
from tqdm import tqdm
import pandas as pd
import time
import re


class Video():

    def __init__(self, element: WebElement):
        self.element = element
        
        self.find_title()
        self.find_date()
        self.find_status()
        self.find_type()
        self.find_scores()
    
    def find_title(self):
        self.title = self.element.find_element_by_tag_name("h3").text
        # print(self.title)
    
    def find_date(self):
        video_date_tag = self.element.find_element_by_class_name("date")
        self.date = re.search("[0-9]*\.[0-9]*\.[0-9]*", video_date_tag.text).group(0)
        # print(self.date)
    
    def find_status(self):
        self.status="alive"
        class_status = [
            ("icon--deleted", "deleted"),
            ("icon--upcoming", "upcoming"),
            ("icon--live", "streaming")
        ]

        for class_, status in class_status:
            try:
                self.find_element_by_class_name(class_)
                self.status = status
            except:
                continue

        # print(self.status)

    def find_type(self):
        video_date_tag = self.element.find_element_by_class_name("date")
        if re.search("[^0-9.]", video_date_tag.text):
            self.type = "livestream"
        else:
            self.type = "video"
        # print(self.type)
        pass

    def find_scores(self):
        self.find_views()
        self.find_superchat()
        self.find_like()
        self.find_dislike()
        self.find_comment()

    def find_views(self):
        try:
            video_views_tag = self.element.find_element_by_class_name("score__item--play")
            self.views = video_views_tag.find_element_by_class_name("num").text
        except:
            self.views = "-"
        # print(self.views)

    def find_superchat(self):
        try:
            video_superchat_tag = self.element.find_element_by_class_name("score__item--superchat")
            video_superchat = video_superchat_tag.find_element_by_class_name("num").text
            video_superchat = re.search("[0-9,]+", video_superchat).group(0)
        except:
            video_superchat = "0"
        self.superchat = video_superchat
        # print(video_superchat)

    def find_like(self):
        video_like_tag = self.element.find_element_by_class_name("score__item--like")
        video_like = video_like_tag.find_element_by_class_name("num").text
        self.like = video_like
        # print(video_like)
    
    def find_dislike(self):
        video_dislike_tag = self.element.find_element_by_class_name("score__item--dislike")
        video_dislike = video_dislike_tag.find_element_by_class_name("num").text
        self.dislike = video_dislike
        # print(video_dislike)
    
    def find_comment(self):
        video_comment_tag = self.element.find_element_by_class_name("score__item--comment")
        video_comment = video_comment_tag.find_element_by_class_name("num").text
        self.comment = video_comment
        # print(video_comment)

def get_videos_info(driver: webdriver, channel_url, channel_name):

    url = "{}/videos".format(channel_url)
    driver.get(url)

    scroll_down(driver, 24)
    video_list = driver.find_elements_by_class_name("video")
    videos = []
    for elem_video in tqdm(video_list):
        # print("Processing {} of {} videos".format(index, len(video_list)))
        videos.append(Video(elem_video))
        # video_datas.append(video_data)

    save_video_result(channel_name, videos)

def save_video_result(channel_name, videos):
    filename = "{0}/{1} {0} videos.xlsx".format(channel_name, date.today().strftime("%Y-%m-%d"))

    output_array = []
    for video in videos:

        entry = [
            video.date,
            video.title,
            video.type,
            video.views,
            video.superchat,
            video.like,
            video.dislike,
            video.comment,
            video.status
        ]
        output_array.append(entry)
    
    columns = ["日期", "標題", "類型", "觀看數", "SC 金額", "喜歡", "不喜歡", "留言數", "狀態"]
    pd.DataFrame(output_array, columns=columns).to_excel(filename, index=False)

def scroll_down(driver, num_scrolls=10):
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(num_scrolls):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height