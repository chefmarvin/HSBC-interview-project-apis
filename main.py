from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from constants import DEFAULT_HISTORY_PERIOD, ORIGINS
from typing import Dict, Any, List
from fastapi.middleware.cors import CORSMiddleware
import logging
from model import IYFinanceGenericData, IYFinanceHistoryData, IGenAIReport
from finance_data_source.yfinance import YahooFinanceQuery
from service.analysis import get_llama_analysis

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
    """
    Retrieves the data for the default set of symbols.

    Returns:
        Dict[str, IYFinanceGenericData]: A dictionary where the key is the symbol and the value is an IYFinanceGenericData object representing the data for the given symbol.

    Raises:
        HTTPException: If there is an error in fetching the data, an HTTPException is raised with a 500 status code.
    """
    try:
        yf_ins = YahooFinanceQuery()
        yf_ins_data = yf_ins.getSymbolsData()
        return yf_ins_data
    except Exception as e:
        logger.error(f"Error when get data for default symbols: {e}")
        raise HTTPException(status_code=500, detail="Error when get data.")

@app.get("/search/by-symbol/{symbol}/", response_model=Dict[str, IYFinanceGenericData])
async def search_by_symbol(symbol: str):
    """
    Retrieves the data for a given symbol from Yahoo Finance.

    Args:
        symbol (str): The symbol for which the data is to be retrieved.

    Returns:
        Dict[str, IYFinanceGenericData]: A dictionary where the key is the symbol and the value is an IYFinanceGenericData object representing the data for the given symbol.

    Raises:
        HTTPException: If there is an error in fetching the data, an HTTPException is raised with a 500 status code.
    """
    try:
        yf_ins = YahooFinanceQuery()
        yf_ins_data = yf_ins.getSymbolsData([symbol])
        return yf_ins_data
    except Exception as e:
        logger.error(f"Error when get data for symbol {symbol}: {e}.")
        raise HTTPException(status_code=500, detail="Error when get data.")

@app.get("/history/by-symbol/{symbol}/", response_model=List[IYFinanceHistoryData])
async def history_by_symbol(symbol: str, period: str = DEFAULT_HISTORY_PERIOD):
    """
    Retrieves the historical data for a given symbol from Yahoo Finance.

    Args:
        symbol (str): The symbol for which the historical data is to be retrieved.
        period (str, optional): The period for which the historical data is to be retrieved. Defaults to DEFAULT_HISTORY_PERIOD.

    Returns:
        List[IYFinanceHistoryData]: A list of IYFinanceHistoryData objects, each representing the historical data for the given symbol for a specific date.

    Raises:
        HTTPException: If there is an error in fetching the data, an HTTPException is raised with a 500 status code.
    """
    try:
        yf_ins = YahooFinanceQuery()
        yf_ins_data = yf_ins.getHistoryBySymbol(symbol, period)
        return yf_ins_data
    except Exception as e:
        logger.error(f"Error when get history data for symbol {symbol}: {e}.")
        raise HTTPException(status_code=500, detail="Error when get history data.")

@app.get("/analysis/by-genAI/{symbol}/", response_model=IGenAIReport)
async def openai_analysis(symbol: str):
    try:
        report = get_llama_analysis(symbol)
        return { "report": report.choices[0].message.content }
    except Exception as e:
        logger.error(f"Error when get analysis data for symbol {symbol}: {e}.")
        raise HTTPException(status_code=500, detail="Error when get analysis data.")
