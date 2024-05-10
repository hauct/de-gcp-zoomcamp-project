import requests as re
from config import category_endpoint_url
from API_helper.util.util import _build_url

def category_id(**kwarg):
    """ 
    category_id int : The id for a category.
    """
    # Define API Parameter
    endpoint = category_endpoint_url.category
    endpointpara = category_endpoint_url.para_category
    # Contruct the url request    
    url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
    try:
        result = re.get(url_requst)
        return result
    except Exception as error:
        print(f"An error occured '{error}'. Please check the parameter pass.")
        return None