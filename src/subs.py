
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

from datetime import date
import pandas as pd

def get_subs_info(driver: Chrome, channel_url, channel_name):

    url = "{}/subscribers".format(channel_url)
    driver.get(url)

    subs_table: WebElement = driver.find_element(By.CLASS_NAME, "sheet--rounded")
    rows: list[WebElement] = subs_table.find_elements(By.TAG_NAME, "tr")
    columns = [col.text for col in rows[0].find_elements(By.TAG_NAME, "th")]
    entries = []
    for row in rows[1:]:
        entries.append([
            row.find_element(By.CLASS_NAME, "label").text,
            row.find_element(By.CLASS_NAME, "fluc-label").text,
            row.find_element(By.CLASS_NAME, "total").text
        ])
    
    # print(columns, entries)

    save_subs_result(channel_name, columns, entries)

def save_subs_result(channel_name, columns, entries):

    filename = "{0}/{1} {0} subs.xlsx".format(channel_name, date.today().strftime("%Y-%m-%d"))
    pd.DataFrame(entries, columns=columns).to_excel(filename, index=False)
