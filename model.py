from typing import Union, Optional
from pydantic import BaseModel, Field

class IYFinanceMarketIndexesInfo(BaseModel):
    # index
    open: Union[float, None] = None,
    dayLow: Union[float, None] = None,
    dayHigh: Union[float, None] = None,
    regularMarketOpen: Union[float, None] = None,
    regularMarketDayLow: Union[float, None] = None,
    regularMarketDayHigh: Union[float, None] = None,
    volume: Union[int, None] = None,
    regularMarketVolume: Union[int, None] = None,
    averageVolume: Union[int, None] = None,
    averageVolume10days: Union[int, None] = None,
    averageDailyVolume10Day: Union[int, None] = None,
    bid: Union[float, None] = None,
    ask: Union[float, None] = None,
    # common
    maxAge: Union[int, None] = None,
    priceHint: Union[int, None] = None,
    previousClose: Union[float, None] = None,
    regularMarketPreviousClose: Union[float, None] = None,
    fiftyTwoWeekLow: Union[float, None] = None,
    fiftyTwoWeekHigh: Union[float, None] = None,
    fiftyDayAverage: Union[float, None] = None,
    twoHundredDayAverage: Union[float, None] = None,
    currency: Union[str, None] = None,
    exchange: Union[str, None] = None,
    quoteType: Union[str, None] = None,
    symbol: Union[str, None] = None,
    underlyingSymbol: Union[str, None] = None,
    shortName: Union[str, None] = None,
    longName: Union[str, None] = None,
    firstTradeDateEpochUtc: Union[int, None] = None,
    timeZoneFullName: Union[str, None] = None,
    timeZoneShortName: Union[str, None] = None,
    uuid: Union[str, None] = None,
    messageBoardId: Union[str, None] = None,
    gmtOffSetMilliseconds: Union[int, None] = None,
    trailingPegRatio: Union[float, None] = None

class IYFinanceMutualFundInfo(BaseModel):
    # mutual fund
    address1: Union[str, None] = None
    address2: Union[str, None] = None
    address3: Union[str, None] = None
    phone: Union[str, None] = None
    longBusinessSummary: Union[str, None] = None
    trailingPE: Union[float, None] = None
    yield_: Union[float, None] = Field(..., alias='yield')
    ytdReturn: Union[float, None] = None
    totalAssets: Union[float, None] = None
    trailingAnnualDividendRate: Union[float, None] = None
    trailingAnnualDividendYield: Union[float, None] = None
    morningStarOverallRating: Union[float, None] = None
    morningStarRiskRating: Union[float, None] = None
    annualReportExpenseRatio: Union[float, None] = None
    beta3Year: Union[float, None] = None
    fundInceptionDate: Union[float, None] = None
    lastDividendValue: Union[float, None] = None
    lastCapGain: Union[float, None] = None
    annualHoldingsTurnover: Union[float, None] = None
    # common
    maxAge: Union[int, None] = None
    priceHint: Union[int, None] = None
    previousClose: Union[float, None] = None
    regularMarketPreviousClose: Union[float, None] = None
    fiftyTwoWeekLow: Union[float, None] = None
    fiftyTwoWeekHigh: Union[float, None] = None
    fiftyDayAverage: Union[float, None] = None
    twoHundredDayAverage: Union[float, None] = None
    currency: Union[str, None] = None
    exchange: Union[str, None] = None
    quoteType: Union[str, None] = None
    symbol: Union[str, None] = None
    underlyingSymbol: Union[str, None] = None
    shortName: Union[str, None] = None
    longName: Union[str, None] = None
    firstTradeDateEpochUtc: Union[int, None] = None
    timeZoneFullName: Union[str, None] = None
    timeZoneShortName: Union[str, None] = None
    uuid: Union[str, None] = None
    messageBoardId: Union[str, None] = None
    gmtOffSetMilliseconds: Union[int, None] = None
    trailingPegRatio: Union[float, None] = None