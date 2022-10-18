# YouTube Channel Analysis With Playboard

A Python web scrapper that scrapes YouTube channel and video analytics from a thrid party website, [Playboard](https://playboard.co).

## Objective
Familiarize myself with the browser automation library [selenium](https://selenium-python.readthedocs.io/) and apply it on some simple web scraping jobs.

## Usage
1. Download a [Chrome WebDriver executable](https://chromedriver.chromium.org/downloads) whose version matches that of your Chrome browser. You can check the browser version [here](chrome://settings/help). Place the executable under this directory.
1. Run `python src\main.py`, then paste a link of a YouTube channel. The results should show up in the `output` folder.

## Known Issue(s)
Due to a strict quota on usage without an account, the current state of the program (which doesn't have a login feature) is nearly impossible to test or use. Solutions may be adding an automatic login feature, or utilize cookies from external sources. The when and how to solve this issue is undetermined.

## Environment
This project uses the following packages:
| Package | Version |
|---|---|
| python | 3.10.6 |
| pandas | 1.5.0 |
| tqdm | 4.64.1 |
| openpyxl | 3.0.10 |
| selenium | 4.5.0 |

Detailed packages and versions can be found in [environment.yml](environment.yml). To create an identical virtual environment in Anaconda, use the command `conda env create -f requirements.yml`.