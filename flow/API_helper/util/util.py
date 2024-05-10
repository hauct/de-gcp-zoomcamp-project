from urllib.parse import urlencode
from config import endpoint_url, category_endpoint_url
from dotenv import load_dotenv
import os

basedir=os.getcwd()[:-5]
print(basedir)
load_dotenv(os.path.join(basedir, '../.env'))

def _build_endurl(parameter,endpointpara):
    para_all = {}
    for name,value in parameter['kwarg'].items():
        if name in endpointpara:
            para_all[name] = value
    
    para_all['api_key'] = os.getenv("Fred_API")
    para_all['file_type'] = 'json'
    endurl = urlencode(para_all)

    return endurl

def _build_url(endpoint=None,endpointpara=None,map=None,**kwarg):
    if map:
        main_url = endpoint_url.main_url_geo
    else:
        main_url = endpoint_url.main_url
    end_url = _build_endurl(parameter=kwarg,endpointpara=endpointpara)

    return main_url + endpoint + end_url

data = _build_url(endpoint=category_endpoint_url.category, endpointpara=category_endpoint_url.para_category)
print(data)
