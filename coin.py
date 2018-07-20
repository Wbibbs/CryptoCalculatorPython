class Coin(object):
    
    def __init__(self):
        self.nameOfCoin = "a"
        self.rank = "a"
        self.coinSymbol = "a"
        self.coinPrice = "a"
        self.priceBtc = "a"
        self.dayVol = "a"
        self.marketCap = "a"
        self.availableSupply = "a"
        self.totalSupply = "a"
        self.maxSupply = "a"
        self.percentHour = "a"
        self.percentDay = "a"
        self.percentWeek = "a"
        self.circulatingSupply = "a"
        self.priceUSD = "a"

    def setInfo(self, c):

        self.nameOfCoin = c["data"]["name"]
        self.coinSymbol = c["data"]["symbol"]
        self.rank = c["data"]["rank"]
        self.circulatingSupply = c["data"]["circulating_supply"]
        self.totalSupply = c["data"]["total_supply"]
        self.maxSupply = str(c["data"]["max_supply"])
        self.priceUSD = c["data"]["quotes"]["USD"]["price"]
        self.marketCap = c["data"]["quotes"]["USD"]["market_cap"]
        self.percentHour =c["data"]["quotes"]["USD"]["percent_change_1h"]
        self.percentDay = c["data"]["quotes"]["USD"]["percent_change_1h"]
        self.percentWeek = c["data"]["quotes"]["USD"]["percent_change_7d"]
    
    def getPercentWeek(self):
        return self.percentWeek
    
    def getPercentDay(self):
        return self.percentDay
    
    def getPercentHour(self):
        return self.percentHour
    
    def getPriceUSD(self):
        return self.priceUSD
    
    def getMaxSupply(self):
        return self.maxSupply
    
    def getTotalSupply(self):
        return self.totalSupply
    
    def getRank(self):
        return self.rank
    
    def getSymbol(self):
        return self.coinSymbol
    
    def getName(self):
        return self.nameOfCoin
    
    def setPercentWeek(self, a):
        self.percentWeek = a
    
    def setPercentDay(self, a):
        self.percentDay = a
    
    def setPercentHour(self, a):
        self.percentHour = a
    
    def setPriceUSD(self, a):
        self.priceUSD = a
    
    def setMaxSupply(self, a):
        self.maxSupply = a
    
    def setTotalSupply(self, a):
        self.totalSupply = a
    
    def setRank(self, a):
        self.rank = a
    
    def setSymbol(self, a):
        self.coinSymbol = a
    
    def setName(self, a):
        self.nameOfCoin = a