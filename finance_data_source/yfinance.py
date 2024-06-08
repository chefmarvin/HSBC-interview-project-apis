import yfinance as yf

class YahooFinanceQuery:
    def __init__(self):
        self.market_indexes = [ "^GSPC", "^DJI" ]
        self.stock_share_initial_symbols = [ "MSFT", "BA", "NKE", "SBUX", "HSBC" ]
        self.mutual_fund_initial_symbols = [ "VSMPX", "FXAIX", "VFIAX", "VTSAX", "VGTSX" ]

    def getMarketIndexesData(self, symbols: list[str] = None):
        if symbols is None:
            symbols = self.market_indexes
        mi_infos = {key: None for key in symbols}
        try:
            mis = yf.Tickers(symbols)
            for key in mis.tickers:
                mi_infos[key] = mis.tickers[key].info
            return mi_infos
        except:
            return mi_infos

    def getMutualFundsInfoBySymbols(self, symbols: list[str] = None):
        if symbols is None:
            symbols = self.mutual_fund_initial_symbols
        funds_infos = {key: None for key in symbols}
        try:
            funds = yf.Tickers(symbols)
            for key in funds.tickers:
                funds_infos[key] = funds.tickers[key].info
            return funds_infos
        except:
            return funds_infos
