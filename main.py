from fastapi import FastAPI
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from model import IYFinanceMarketIndexesInfo, IYFinanceMutualFundInfo
from finance_data_source.yfinance import YahooFinanceQuery

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
    "https://wonderful-bay-0ec57fa0f.5.azurestaticapps.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "HSBC interview coding project"}

@app.get("/market-indexes-list/", response_model=Dict[str, IYFinanceMarketIndexesInfo])
async def market_indexes_list():
    yf_ins = YahooFinanceQuery()
    yf_ins_data = yf_ins.getMarketIndexesData()
    return yf_ins_data

@app.get("/default-mutual-funds-list/", response_model=Dict[str, IYFinanceMutualFundInfo])
async def default_mutual_funds_list():
    yf_ins = YahooFinanceQuery()
    yf_ins_data = yf_ins.getMutualFundsInfoBySymbols()
    return yf_ins_data

@app.get("/search/mutual-fund/by-symbol/{symbol}/", response_model=Dict[str, IYFinanceMutualFundInfo])
async def search_mutual_fund_by_symbol(symbol: str):
    yf_ins = YahooFinanceQuery()
    yf_ins_data = yf_ins.getMutualFundsInfoBySymbols([symbol])
    return yf_ins_data
