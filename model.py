from typing import Union, List
from pydantic import BaseModel, Field

class ICompanyOfficers(BaseModel):
    maxAge: Union[int, None] = None
    name: Union[str, None] = None
    age: Union[int, None] = None
    title: Union[str, None] = None
    yearBorn: Union[int, None] = None
    fiscalYear: Union[int, None] = None
    totalPay: Union[int, None] = None
    exercisedValue: Union[int, None] = None
    unexercisedValue: Union[int, None] = None

    class Config:
        exclude_unset = True

class IYFinanceGenericHistoryMetadata(BaseModel):
    symbol: Union[str, None] = None
    isin: Union[str, None] = None
    exchange: Union[str, None] = None
    currency: Union[str, None] = None
    regularMarketTime: Union[int, None] = None
    gmtoffset: Union[int, None] = None
    timezone: Union[str, None] = None
    exchangeTimezoneName: Union[str, None] = None
    regularMarketPrice: Union[float, None] = None
    chartPreviousClose: Union[float, None] = None
    previousClose: Union[float, None] = None
    scale: Union[int, None] = None
    priceHint: Union[int, None] = None
    currentTradingPeriod: Union[dict, None] = None
    # tradingPeriods: Union[List[dict], None] = None
    dataGranularity: Union[str, None] = None
    range: Union[str, None] = None
    validRanges: Union[List[str], None] = None

    class Config:
        exclude_unset = True

class IYFinanceGenericInfo(BaseModel):
    quoteType: Union[str, None] = None
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
    # for stock and mutual fund
    address1: Union[str, None] = None
    lastDividendValue: Union[float, None] = None
    longBusinessSummary: Union[str, None] = None
    # for mutual fund only
    address2: Union[str, None] = None
    address3: Union[str, None] = None
    yield_: Union[float, None] = Field(None, alias='yield')
    ytdReturn: Union[float, None] = None
    totalAssets: Union[float, None] = None
    morningStarOverallRating: Union[float, None] = None
    morningStarRiskRating: Union[float, None] = None
    annualReportExpenseRatio: Union[float, None] = None
    beta3Year: Union[float, None] = None
    fundInceptionDate: Union[float, None] = None
    lastCapGain: Union[float, None] = None
    annualHoldingsTurnover: Union[float, None] = None
    # stock and index
    city: Union[str, None] = None
    state: Union[str, None] = None
    zip: Union[str, None] = None
    country: Union[str, None] = None
    phone: Union[str, None] = None
    website: Union[str, None] = None
    industry: Union[str, None] = None
    industryKey: Union[str, None] = None
    industryDisp: Union[str, None] = None
    sector: Union[str, None] = None
    sectorKey: Union[str, None] = None
    sectorDisp: Union[str, None] = None
    fullTimeEmployees: Union[int, None] = None
    companyOfficers: Union[List[ICompanyOfficers], None] = None
    auditRisk: Union[int, None] = None
    boardRisk: Union[int, None] = None
    compensationRisk: Union[int, None] = None
    shareHolderRightsRisk: Union[int, None] = None
    overallRisk: Union[int, None] = None
    governanceEpochDate: Union[int, None] = None
    compensationAsOfEpochDate: Union[int, None] = None
    irWebsite: Union[str, None] = None
    open: Union[float, None] = None
    dayLow: Union[float, None] = None
    dayHigh: Union[float, None] = None
    regularMarketOpen: Union[float, None] = None
    regularMarketDayLow: Union[float, None] = None
    regularMarketDayHigh: Union[float, None] = None
    dividendRate: Union[float, None] = None
    dividendYield: Union[float, None] = None
    exDividendDate: Union[int, None] = None
    payoutRatio: Union[float, None] = None
    fiveYearAvgDividendYield: Union[float, None] = None
    beta: Union[float, None] = None
    trailingPE: Union[float, None] = None
    forwardPE: Union[float, None] = None
    volume: Union[int, None] = None
    regularMarketVolume: Union[int, None] = None
    averageVolume: Union[int, None] = None
    averageVolume10days: Union[int, None] = None
    averageDailyVolume10Day: Union[int, None] = None
    bid: Union[float, None] = None
    ask: Union[float, None] = None
    bidSize: Union[int, None] = None
    askSize: Union[int, None] = None
    marketCap: Union[int, None] = None
    priceToSalesTrailing12Months: Union[float, None] = None
    trailingAnnualDividendRate: Union[float, None] = None
    trailingAnnualDividendYield: Union[float, None] = None
    enterpriseValue: Union[int, None] = None
    profitMargins: Union[float, None] = None
    floatShares: Union[int, None] = None
    sharesOutstanding: Union[int, None] = None
    sharesShort: Union[int, None] = None
    sharesShortPriorMonth: Union[int, None] = None
    sharesShortPreviousMonthDate: Union[int, None] = None
    dateShortInterest: Union[int, None] = None
    sharesPercentSharesOut: Union[float, None] = None
    heldPercentInsiders: Union[float, None] = None
    heldPercentInstitutions: Union[float, None] = None
    shortRatio: Union[float, None] = None
    shortPercentOfFloat: Union[float, None] = None
    impliedSharesOutstanding: Union[int, None] = None
    bookValue: Union[float, None] = None
    lastFiscalYearEnd: Union[int, None] = None
    nextFiscalYearEnd: Union[int, None] = None
    mostRecentQuarter: Union[int, None] = None
    earningsQuarterlyGrowth: Union[float, None] = None
    netIncomeToCommon: Union[int, None] = None
    trailingEps: Union[float, None] = None
    forwardEps: Union[float, None] = None
    pegRatio: Union[float, None] = None
    lastSplitFactor: Union[str, None] = None
    lastSplitDate: Union[int, None] = None
    enterpriseToRevenue: Union[float, None] = None
    enterpriseToEbitda: Union[float, None] = None
    Week52Change: Union[float, None] = Field(None, alias='52WeekChange')
    SandP52WeekChange: Union[float, None] = None
    lastDividendDate: Union[int, None] = None
    currentPrice: Union[float, None] = None
    targetHighPrice: Union[float, None] = None
    targetLowPrice: Union[float, None] = None
    targetMeanPrice: Union[float, None] = None
    targetMedianPrice: Union[float, None] = None
    recommendationMean: Union[float, None] = None
    recommendationKey: Union[str, None] = None
    numberOfAnalystOpinions: Union[int, None] = None
    totalCash: Union[int, None] = None
    totalCashPerShare: Union[float, None] = None
    ebitda: Union[int, None] = None
    totalDebt: Union[int, None] = None
    quickRatio: Union[float, None] = None
    debtToEquity: Union[float, None] = None
    currentRatio: Union[float, None] = None
    totalRevenue: Union[int, None] = None
    revenuePerShare: Union[float, None] = None
    returnOnAssets: Union[float, None] = None
    freeCashflow: Union[int, None] = None
    operatingCashflow: Union[int, None] = None
    earningsGrowth: Union[float, None] = None
    revenueGrowth: Union[float, None] = None
    grossMargins: Union[float, None] = None
    ebitdaMargins: Union[float, None] = None
    operatingMargins: Union[float, None] = None
    financialCurrency: Union[str, None] = None
    fax: Union[str, None] = None
    priceToBook: Union[float, None] = None
    returnOnEquity: Union[float, None] = None

    class Config:
        exclude_unset = True

class IYFinanceGenericData(BaseModel):
    metadata: Union[IYFinanceGenericHistoryMetadata, None] = None
    info: Union[IYFinanceGenericInfo, None] = None

    class Config:
        exclude_unset = True

class IYFinanceHistoryData(BaseModel):
    Date: Union[str, None] = None
    Open: Union[float, None] = None
    High: Union[float, None] = None
    Low: Union[float, None] = None
    Close: Union[float, None] = None
    Volume: Union[int, None] = None
    Dividends: Union[float, None] = None
    StockSplits: Union[float, None] = Field(None, alias='Stock Splits')
    CapitalGains: Union[float, None] = Field(None, alias='Capital Gains')
    # AdjClose: Union[float, None] = None
    # Divident: Union[float, None] = None
    # SplitCoefficient: Union[float, None] = None

    class Config:
        exclude_unset = True

# class IYFinanceMutualFundInfo(BaseModel):
#     # mutual fund only
#     address1: Union[str, None] = None
#     address2: Union[str, None] = None
#     address3: Union[str, None] = None
#     phone: Union[str, None] = None
#     longBusinessSummary: Union[str, None] = None
#     trailingPE: Union[float, None] = None
#     yield_: Union[float, None] = Field(..., alias='yield')
#     ytdReturn: Union[float, None] = None
#     totalAssets: Union[float, None] = None
#     trailingAnnualDividendRate: Union[float, None] = None
#     trailingAnnualDividendYield: Union[float, None] = None
#     morningStarOverallRating: Union[float, None] = None
#     morningStarRiskRating: Union[float, None] = None
#     annualReportExpenseRatio: Union[float, None] = None
#     beta3Year: Union[float, None] = None
#     fundInceptionDate: Union[float, None] = None
#     lastDividendValue: Union[float, None] = None
#     lastCapGain: Union[float, None] = None
#     annualHoldingsTurnover: Union[float, None] = None
#     # common
#     maxAge: Union[int, None] = None
#     priceHint: Union[int, None] = None
#     previousClose: Union[float, None] = None
#     regularMarketPreviousClose: Union[float, None] = None
#     fiftyTwoWeekLow: Union[float, None] = None
#     fiftyTwoWeekHigh: Union[float, None] = None
#     fiftyDayAverage: Union[float, None] = None
#     twoHundredDayAverage: Union[float, None] = None
#     currency: Union[str, None] = None
#     exchange: Union[str, None] = None
#     quoteType: Union[str, None] = None
#     symbol: Union[str, None] = None
#     underlyingSymbol: Union[str, None] = None
#     shortName: Union[str, None] = None
#     longName: Union[str, None] = None
#     firstTradeDateEpochUtc: Union[int, None] = None
#     timeZoneFullName: Union[str, None] = None
#     timeZoneShortName: Union[str, None] = None
#     uuid: Union[str, None] = None
#     messageBoardId: Union[str, None] = None
#     gmtOffSetMilliseconds: Union[int, None] = None
#     trailingPegRatio: Union[float, None] = None

# class IYFinanceMarketIndexesInfo(BaseModel):
#     # index only
#     open: Union[float, None] = None
#     dayLow: Union[float, None] = None
#     dayHigh: Union[float, None] = None
#     regularMarketOpen: Union[float, None] = None
#     regularMarketDayLow: Union[float, None] = None
#     regularMarketDayHigh: Union[float, None] = None
#     volume: Union[int, None] = None
#     regularMarketVolume: Union[int, None] = None
#     averageVolume: Union[int, None] = None
#     averageVolume10days: Union[int, None] = None
#     averageDailyVolume10Day: Union[int, None] = None
#     bid: Union[float, None] = None
#     ask: Union[float, None] = None
#     # common
#     maxAge: Union[int, None] = None,
#     priceHint: Union[int, None] = None,
#     previousClose: Union[float, None] = None,
#     regularMarketPreviousClose: Union[float, None] = None,
#     fiftyTwoWeekLow: Union[float, None] = None,
#     fiftyTwoWeekHigh: Union[float, None] = None,
#     fiftyDayAverage: Union[float, None] = None,
#     twoHundredDayAverage: Union[float, None] = None,
#     currency: Union[str, None] = None,
#     exchange: Union[str, None] = None,
#     quoteType: Union[str, None] = None,
#     symbol: Union[str, None] = None,
#     underlyingSymbol: Union[str, None] = None,
#     shortName: Union[str, None] = None,
#     longName: Union[str, None] = None,
#     firstTradeDateEpochUtc: Union[int, None] = None,
#     timeZoneFullName: Union[str, None] = None,
#     timeZoneShortName: Union[str, None] = None,
#     uuid: Union[str, None] = None,
#     messageBoardId: Union[str, None] = None,
#     gmtOffSetMilliseconds: Union[int, None] = None,
#     trailingPegRatio: Union[float, None] = None
