from .external import ExternalService
import os 

def get_mutual_funds(scheme_type: str):
    fund_api = ExternalService(url=f"https://{os.getenv('FUND_API_URL')}")
    headers = {
        "x-rapidapi-host": os.getenv("FUND_API_URL"),
        "x-rapidapi-key": os.getenv("FUND_API_KEY"),
    }
    endpoint = '/latest'
    if scheme_type:
        endpoint = f'/latest?scheme_type={scheme_type}'
    fund_data = fund_api.call_api(endpoint, headers=headers)
    return fund_data
