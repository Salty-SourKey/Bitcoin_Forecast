# -*- coding: utf-8 -*-
import urllib3
import datetime
import time
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def get_data2CSV():
    f = pd.read_csv('Bitstamp_btc_usd_hourly_data.csv')

    last_timestamp = f.iloc[-1][0].split()[0] 
    last_date = last_timestamp.split('-')
    last_hour = (int)(f.iloc[-1][0].split()[1].split(':')[0])

    last_data_date = datetime.date((int)(last_date[0]), (int)(last_date[1]), (int)(last_date[2])) + datetime.timedelta(days=1)
    date_obj = datetime.date.today()+datetime.timedelta(days=1)
    date = date_obj.strftime('%Y-%m-%d') 


    url = "https://bitcoincharts.com/charts/bitstampUSD#rg360zigHourlyzczsg{0}zeg{1}ztgSzm1g10zm2g25zv".format(last_data_date,date)
    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="content_chart"]/div/div[2]/a').click()
    time.sleep(3)

    table = driver.find_element_by_class_name('data')
    tbody = table.find_element_by_tag_name("tbody")
    rows = tbody.find_elements_by_tag_name("tr")

    for index, val in enumerate(rows):
        temp = val.find_elements_by_tag_name("td")
        timestamp = (int)(temp[0].text.split()[1].split(':')[0])

        if (last_hour < timestamp or temp[0].text.split()[0] != last_timestamp) and index < len(rows)-1:
            df = pd.DataFrame({'timestamp': [temp[0].text.split()[0]+' '+str(timestamp)+":00"], 'open': [temp[1].text],
                'high': [temp[2].text], 'low': [temp[3].text], 'close': [temp[4].text]})
            df.to_csv('Bitstamp_btc_usd_hourly_data.csv', mode='a', sep=',', header=False, index=False)
    driver.quit()

get_data2CSV()