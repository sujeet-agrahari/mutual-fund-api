from .external import ExternalService

def get_mutual_funds(scheme_type: str):
    fund_api = ExternalService('https://latest-mutual-fund-nav.p.rapidapi.com')
    headers = {
        'x-rapidapi-host': 'latest-mutual-fund-nav.p.rapidapi.com',
        'x-rapidapi-key': '63c198c46cmshe4e0e927edb0cb0p17bd85jsn46dcf86675f2'
    }
    endpoint = '/latest'
    if scheme_type:
        endpoint = f'/latest?scheme_type={scheme_type}'
    fund_data = fund_api.call_api(endpoint, headers=headers)
    return fund_data
