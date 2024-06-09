from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from constants import DEFAULT_HISTORY_PERIOD, ORIGINS
from typing import Dict, Any, List
from fastapi.middleware.cors import CORSMiddleware
from model import IYFinanceGenericData, IYFinanceHistoryData
from finance_data_source.yfinance import YahooFinanceQuery
import logging

class CustomJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return super().render(self.remove_none(content))

    @staticmethod
    def remove_none(data):
        if isinstance(data, list):
            return [CustomJSONResponse.remove_none(i) for i in data if i is not None]
        elif isinstance(data, dict):
            return {k: CustomJSONResponse.remove_none(v) for k, v in data.items() if v is not None}
        else:
            return data

# create a logger
logger = logging.getLogger(__name__)

app = FastAPI(default_response_class=CustomJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes

@app.get("/")
async def root():
    return {"message": "HSBC interview coding project"}

@app.get("/default-symbols-list/", response_model=Dict[str, IYFinanceGenericData])
async def default_symbols_list():
    try:
        yf_ins = YahooFinanceQuery()
        yf_ins_data = yf_ins.getSymbolsData()
        return yf_ins_data
    except Exception as e:
        logger.error(f"Error when get data for default symbols: {e}")
        raise HTTPException(status_code=500, detail="Error when get data.")

@app.get("/search/by-symbol/{symbol}/", response_model=Dict[str, IYFinanceGenericData])
async def search_by_symbol(symbol: str):
    try:
        yf_ins = YahooFinanceQuery()
        yf_ins_data = yf_ins.getSymbolsData([symbol])
        return yf_ins_data
    except Exception as e:
        logger.error(f"Error when get data for symbol {symbol}: {e}.")
        raise HTTPException(status_code=500, detail="Error when get data.")

@app.get("/history/by-symbol/{symbol}/", response_model=List[IYFinanceHistoryData])
async def history_by_symbol(symbol: str, period: str = DEFAULT_HISTORY_PERIOD):
    try:
        yf_ins = YahooFinanceQuery()
        yf_ins_data = yf_ins.getHistoryBySymbol(symbol, period)
        return yf_ins_data
    except Exception as e:
        logger.error(f"Error when get history data for symbol {symbol}: {e}.")
        raise HTTPException(status_code=500, detail="Error when get history data.")