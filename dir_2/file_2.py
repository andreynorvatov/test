import requests
from bs4 import BeautifulSoup

nice_case_urls = {
    "macbook_air": "https://nice-case.ru/catalog/apple/macbook/macbook_air/",
    "macbook_pro": "https://nice-case.ru/catalog/apple/macbook/macbook_pro/",
    "airpods_pro": "https://nice-case.ru/catalog/apple/airpods_1/",
    "iphone_14_pro_max": "https://nice-case.ru/catalog/apple/iphone/iphone_14_pro_max/",
    "iphone_13_pro_max": "https://nice-case.ru/catalog/apple/iphone/iphone_13_pro_max/"
}

css_selectors = {
    "macbook_name_css_selector": "div > div.item_info > div.item_info--top_block > div > a > span",
    "macbook_coast_css_selector": "div > div.item_info > div.item_info--bottom_block > div > div > div > span > span.price_value",
    "airpods_and_iphone_name_css_selector": "div > div.item_info > div.item_info--top_block > div.item-title > a > span",
    "airpods_and_iphone_coast_css_selector":  "div.price_matrix_wrapper > div > span > span.price_value"
}

for products, url in nice_case_urls.items():

    resp = requests.get(url).text
    soup = BeautifulSoup(resp, "lxml")

    if "macbook" in products:
        name_css_selector = css_selectors["macbook_name_css_selector"]
        coast_css_selector = css_selectors["macbook_coast_css_selector"]
    elif "airpods" or "iphone" in products:
        name_css_selector = css_selectors["airpods_and_iphone_name_css_selector"]
        coast_css_selector = css_selectors["airpods_and_iphone_coast_css_selector"]

    item_name_row_list = soup.select(name_css_selector)
    item_coast_row_list = soup.select(coast_css_selector)

    item_name_list = [i.string for i in item_name_row_list]
    item_coast_list = [i.string.replace("\xa0", "") for i in item_coast_row_list]
    rez = zip(item_name_list, item_coast_list)

    for i in rez:
        print(i)