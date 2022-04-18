import argparse
import requests
from datetime import datetime, timedelta
import json
from typing import List


class SearchResult:
    pass

class SearchResults:
    pass

class GovScraper:
 
    def __init__(self, api_key:str, keywords:List, numDays:int) -> None:
        self.api_key = api_key
        self.keywords = keywords
        self.numDays = numDays

    def search(self) -> SearchResults:
        today = datetime.today()
        today_form = today.strftime('%m/%d/%Y')
        past = (today - timedelta(days=self.numDays)).strftime('%m/%d/%Y')
        print(today_form, past)
        BASE_URI = "https://api.sam.gov/prod/opportunities/v2/search"
        query_params = {
            "limit": 1000,
            "api_key": self.api_key,
            "postedFrom": past,
            "postedTo": today_form,
            "deptname": "general",
            "ptype": "a",
            
        }       
         
        # search_api = "https://api.sam.gov/prod/opportunities/v2/search?limit=1000&api_key="+ self.api_key + "&postedFrom=01/01/2018&postedTo=05/10/2018&ptype=a&deptname=general"
        # print(search_api)    
        # response = requests.get(search_api).json()
        response = requests.get(BASE_URI, params=query_params)
        print(response.text)
        print(type(response))
        
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', help='the API key used for searching', type=str)
    parser.add_argument('--keywords', nargs='*', help='the keywords to search for')
    parser.add_argument('--numDays', help='The number of days in the past to search', type=int)
    args = parser.parse_args()
   
    scraper = GovScraper(args.api_key, args.keywords, args.numDays)
    scraper.search()