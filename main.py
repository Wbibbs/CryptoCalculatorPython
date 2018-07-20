import gui
import json
import urllib.request
import datetime

import coin
from coin import Coin as coinClass
# from oauth2client.service_account import ServiceAccountCredentials
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload


def get_data(coin_num):
    from urllib.request import urlopen
    url = "https://api.coinmarketcap.com/v2/ticker/" + str(coin_num)
    html = urlopen(url)
    string_contents = html.read().decode("utf-8")
    object_contents = json.load(string_contents)
    return object_contents  # Returns a json object


def print_info(c):
    print(str(c.nameOfCoin) + ", "
          + str(c.coinSymbol) + ", "
          + str(c.rank) + ", "
          + str(c.totalSupply) + ", "
          + str(c.maxSupply) + ", "
          + str(c.priceUSD) + ", "
          + str(c.percentHour) + ", "
          + str(c.percentDay) + ", "
          + str(c.percentWeek))


def get_info(c):
    return str(c.nameOfCoin) + ", " \
           + str(c.coinSymbol) + ", " \
           + str(c.rank) + ", " \
           + str(c.totalSupply) + ", " \
           + str(c.maxSupply) + ", " \
           + str(c.priceUSD) + ", " \
           + str(c.percentHour) + ", " \
           + str(c.percentDay) + ", " \
           + str(c.percentWeek)


def print_info_list(c):
    for coin in c:
        print_info(coin)


def print_list(c):
    for coin in c:
        print(coin)


def get_dictionary():
    temp_dict = {}
    url = "https://api.coinmarketcap.com/v2/listings/"
    more_url = urllib.request.urlopen(url)
    obj = json.load(more_url)
    
    for x in range(len(obj["data"])):
        if x not in temp_dict:
            temp_dict[str(obj["data"][x]["name"].lower())] = obj["data"][x]["id"]
            temp_dict[str(obj["data"][x]["symbol"].lower())] = \
                obj["data"][x]["id"]
    
    return temp_dict


def make_coins():
    for name in coin_lookup_list:
        try:
            url = "https://api.coinmarketcap.com/v2/ticker/" + str(coin_dict[name])
        except:
            print("Error: " + name + " does not exist!")
        
        moreurl = urllib.request.urlopen(url)
        obj = json.load(moreurl)
        c = coinClass()
        c.setInfo(obj)
        coins.append(c)


def write_CSV():
    file = open("data.csv", "a+")
    header = "Name, Symbol, Rank, Total Supply, Max Supply, Price in USD," \
             "Percent Change Last Hour, Percent Change Last 24 Hours," \
             "Percent Change Last Week"
    date = datetime.datetime.now()
    
    file.write("\nDate\n\n")
    print("Writing header")
    file.write(header + "\n")
        
    for coin in coins:
        print(get_info(coin))
        print("Writing " + coin.nameOfCoin)
        file.write(get_info(coin) + "\n")
    file.close()
    
# def upload_to_drive():
#    file_metadata = {
#    'name': 'My Report',
#    'mimeType': 'application/vnd.google-apps.spreadsheet'
#    }
#    media = MediaFileUpload('files/report.csv',mimetype='text/csv',
#    resumable=True)
#    file = drive_service.files().create(body=file_metadata,media_body=media,
#    fields='id').execute()
#    print ('File ID: %s' % file.get('id'))


coin_dict = dict()
coin_dict = get_dictionary()
coin_lookup_list = []
coins = []
run = True

while run:
    in_string = input("Enter a coin to look up: ").lower()
    
    if in_string in coin_lookup_list:
        print(in_string + " is already in the search list")
    else:
        if in_string.__eq__("quit"):
            break
        
        if in_string not in coin_dict:
            print(in_string + " does not exist!")
        else:
            coin_lookup_list.append(in_string)

make_coins()
write_CSV()
print_info_list(coins)
