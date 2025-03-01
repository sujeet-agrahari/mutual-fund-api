from mutual_fund_brokerage_api.app import app
import uvicorn

from dotenv import load_dotenv
load_dotenv()  

def main():
    uvicorn.run("mutual_fund_brokerage_api.app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
