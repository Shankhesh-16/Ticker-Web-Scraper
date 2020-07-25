import requests
from bs4 import BeautifulSoup
import pandas as pd

portfolio = ['hdfcbank','itc','reliance','LTTS','wipro','recltd','infy','sbicard']

name_list = []
cp_list = []
pc_list = []
th_list = []
tl_list = []
yh_list = []
yl_list = []

for share_name in portfolio:

    link_blueprint = "https://ticker.finology.in/company/"

    page = requests.get(link_blueprint + share_name.upper())
    link_soup = BeautifulSoup(page.content, 'html.parser')

    # Name
    name = link_soup.find(id="mainContent_ltrlCompName").get_text()

    name_list.append(name)

    # Price
    price_class = link_soup.find(class_="d-block h1 currprice")
    current_price = price_class.find(class_="Number").get_text()

    cp_list.append(current_price)

    # Price change
    price_change = link_soup.find(id="mainContent_pnlPriceChange").get_text()

    pc_list.append(price_change)

    # Today's High and Low
    today_high = link_soup.find(id="mainContent_ltrlTodayHigh").get_text()
    today_low = link_soup.find(id="mainContent_ltrlTodayLow").get_text()

    th_list.append(today_high)
    tl_list.append(today_low)

    # 52 week high and low
    year_high = link_soup.find(id="mainContent_ltrl52WH").get_text()
    year_low = link_soup.find(id="mainContent_ltrl52WL").get_text()

    yh_list.append(year_high)
    yl_list.append(year_low)


live_portfolio = pd.DataFrame(
    {
        ' Share Name': name_list,
        ' Current Price': cp_list,
        " Today's High": th_list,
        " Today's Low": tl_list,
        " 52 week high": yh_list,
        " 52 week low": yl_list
    })

print(live_portfolio)

# Uncomment the line below this to save the file
live_portfolio.to_csv('Live Portfolio.csv')