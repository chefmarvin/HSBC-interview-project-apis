import yfinance as yf
import pandas as pd
import requests_cache
import json

# Set up a cache with a specific expiration time (e.g., 1 hour)
cache_expiration = 3600  # Cache duration in seconds
requests_cache.install_cache('yfinance_cache', expire_after=cache_expiration)

class YahooFinanceQuery:
    def __init__(self):
        self.market_indexes = [ "^GSPC", "^DJI" ]
        self.mutual_fund_initial_symbols = [ "VSMPX", "FXAIX", "VTSAX", "VGTSX" ] # "VFIAX"
        self.stock_share_initial_symbols = ["HSBC"] # "MSFT", "BA", "NKE", "SBUX"

    def getSymbolsData(self, symbols: list[str] = None):
        if symbols is None:
            symbols = self.market_indexes + self.mutual_fund_initial_symbols + self.stock_share_initial_symbols
        symbol_data = {key: None for key in symbols}
        try:
            ins = yf.Tickers(symbols)
            for key in ins.tickers:
                symbol_data[key] = {}
                symbol_data[key]['metadata'] = ins.tickers[key].history_metadata
                symbol_data[key]['info'] = ins.tickers[key].info
            return symbol_data
        except:
            raise ValueError('Error when get data by symbol(s).')
            return symbol_data

    def getHistoryBySymbol(self, symbol: str, period: str = '1mo'):
        try:
            ticker = yf.Ticker(symbol)
            historical_data_csv = ticker.history(period=period)
            historical_data_csv.reset_index(inplace=True)
            historical_data_json_str = historical_data_csv.to_json(orient='records', date_format='iso')
            historical_data_json = json.loads(historical_data_json_str)
            return historical_data_json
        except:
            raise ValueError('Error when get history data.')
            return None

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

