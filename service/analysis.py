from openai import OpenAI
import json
from finance_data_source.yfinance import YahooFinanceQuery
from constants import LLAMA_API_KEY, LLAMA_MODEL_ID

client = OpenAI(api_key = LLAMA_API_KEY, base_url = "https://api.llama-api.com")

def get_llama_analysis(symbol: str):
    yf_ins = YahooFinanceQuery()
    yf_ins_data = yf_ins.getSymbolsData([symbol])
    type = yf_ins_data[symbol]['info']['quoteType'] if 'quoteType' in yf_ins_data[symbol]['info'] else None
    type_str = "stock" if type == 'EQUITY' else "mutual fund"
    data_str = json.dumps(yf_ins_data[symbol]['info'], indent=2)
    prompt_str = f"I have some information about the {type_str} which symbol is {symbol}. and also its basic data {data_str}, give me a brief analysis including investment suggestions."
    response = client.chat.completions.create(
        model=LLAMA_MODEL_ID,
        stream=False,
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": prompt_str}
        ]
    )
    print(response.model_dump_json(indent=2))
    print(response.choices[0].message.content)
    return response