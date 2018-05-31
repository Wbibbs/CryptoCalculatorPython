from coin import Coin as coinClass
import urllib.request, json, datetime, 
import coin

def getData(coinNum) :
    from urllib.request import urlopen
    url = "https://api.coinmarketcap.com/v2/ticker/" + str(coinNum)
    html = urlopen(url)
    stringContents = html.read().decode("utf-8")
    objectContents = json.load(stringContents)
    return objectContents #Returns a json object

def printInfo(c):
    print(str(c.nameOfCoin) + ", " + str(c.coinSymbol) + ", " + str(c.rank) + ", " + str(c.totalSupply) + ", " + str(c.maxSupply) + ", " + str(c.priceUSD) + ", " + str(c.percentHour) + ", " + str(c.percentDay) + ", " + str(c.percentWeek))

def getInfo(c):
    return str(c.nameOfCoin) + ", " + str(c.coinSymbol) + ", " + str(c.rank) + ", " + str(c.totalSupply) + ", " + str(c.maxSupply) + ", " + str(c.priceUSD) + ", " + str(c.percentHour) + ", " + str(c.percentDay) + ", " + str(c.percentWeek)
    
def printInfoList(c):
    for coin in c:
        printInfo(coin)

def printList(c):
    for coin in c:
        print(coin)
        
def getDictionary():
    tempDict = {}
    url = "https://api.coinmarketcap.com/v2/listings/"
    moreurl = urllib.request.urlopen(url)
    obj = json.load(moreurl)
    
    for x in range(len(obj["data"])):
        if not x in tempDict:
            tempDict[str(obj["data"][x]["name"].lower())] = obj["data"][x]["id"]
            tempDict[str(obj["data"][x]["symbol"].lower())] = obj["data"][x]["id"]
    
    return tempDict

def makeCoins():
    for name in coinLookupList:
        try:
            url = "https://api.coinmarketcap.com/v2/ticker/" + str(coinDict[name])
        except:
            print("Error: " + name + " does not exist!")
        
        moreurl = urllib.request.urlopen(url)
        obj = json.load(moreurl)
        c = coinClass()
        c.setInfo(obj)
        coins.append(c)

def writeCSV():
    file = open("data.csv", "a+")
    header = "Name, Symbol, Rank, Total Supply, Max Supply, Price in USD, Percent Change Last Hour, Percent Change Last 24 Hours, Percent Change Last Week"
    date = datetime.datetime.now()
    
    file.write("\nDate\n\n")
    print("Writing header")
    file.write(header + "\n")
        
    for coin in coins:
        print(getInfo(coin))
        print("Writing " + coin.nameOfCoin)
        file.write(getInfo(coin) + "\n")
    file.close()

def uploadToDrive():
    file_metadata = {
    'name': 'My Report',
    'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload('files/report.csv',mimetype='text/csv',resumable=True)
    file = drive_service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    print 'File ID: %s' % file.get('id')


coinDict = dict()
coinDict = getDictionary()
coinLookupList = []
coins = []
run = True

while run:
    inString = input("Enter a coin to look up: ").lower()
    
    if inString in coinLookupList: #Need to figure out a method to test both full names and symbol names ex. btc and bitcoin count for btc or bitcoin in the lookup list
        print(inString + " is already in the search list")
    else:
        if inString.__eq__("quit"):
            break
        
        if not inString in coinDict:
            print(inString + " does not exist!")
        else:
            coinLookupList.append(inString)

makeCoins()

print("Done with while")

writeCSV()

print("Passed writeCSV")
printInfoList(coins)