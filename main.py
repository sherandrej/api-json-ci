#!/bin/python3
from requests import get
import json
import time
from datetime import datetime
# https://www.nbrb.by/api/exrates/currencies


def in_data():
    url = 'https://www.nbrb.by/api/exrates/rates/840?parammode=1'
    # res_json = response.json()
    response = get(url)
    todos = json.loads(response.text)
    return todos


def my_func():
    sleep_time = 10
    try:
        res = in_data()
    except Exception as ex:
        print('Something wrong', ex)
        exit(1)
    print('Currency:', res['Cur_Abbreviation'])
    dt = datetime.now()
    print(dt.year, '/', dt.month, '/', dt.day, ' ', dt.hour, ':', dt.minute, ':', dt.second,\
          sep='', flush=True)
    print(res['Cur_OfficialRate'], flush=True)
#   print('sleeping', sleep_time, 'seconds')
    time.sleep(sleep_time)


if __name__ == '__main__':
    while True:
        my_func()
    #    print(todos['Cur_Name','Cur_OfficialRate'])
    #    print(todos{'Cur_Abbreviation"})
    #    print(todos)     # print(type(todos))      # break
