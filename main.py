import re

import requests
from typing import List, Set


def find_phone_number(urls: List[str]) -> Set[str]:

    loc_list = set()

    for page_link in urls:
        page = requests.get(page_link)

        for i in re.findall(r'8\s\(?\d{3}\)?\s\d{3}[-\s]?\d{2}[-\s]?\d{2}', page.text):
            loc_list.add(i.replace(" ", "").replace("(", "").replace(")", "").replace("-", ""))

    return loc_list


website_list = ["https://hands.ru/company/about", "https://repetitors.info/"]

print(find_phone_number(website_list))






