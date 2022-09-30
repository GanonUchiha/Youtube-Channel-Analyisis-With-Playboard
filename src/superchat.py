
from selenium import webdriver
from datetime import date
import pandas as pd

def get_superchat_info(driver: webdriver, channel_url, channel_name):

    url = "{}/superchat".format(channel_url)
    driver.get(url)

    subs_table = driver.find_element_by_class_name("sheet--rounded")
    rows = subs_table.find_elements_by_tag_name("tr")
    columns = [col.text for col in rows[0].find_elements_by_tag_name("th")]
    entries = []
    for row in rows[1:]:
        entries.append([
            row.find_element_by_class_name("date").text,
            row.find_element_by_class_name("count").text,
            row.find_element_by_class_name("avg").text,
            row.find_element_by_class_name("amount").text
        ])
    
    # print(columns, entries)

    save_superchat_result(channel_name, columns, entries)

def save_superchat_result(channel_name, columns, entries):

    filename = "{0}/{1} {0} superchat.xlsx".format(channel_name, date.today().strftime("%Y-%m-%d"))
    pd.DataFrame(entries, columns=columns).to_excel(filename, index=False)
