
import requests as re
from config import map_endpoint_url
from API_helper.util.util import _build_url

class map:    
    def file(**kwarg): 
            '''
            ['shape']
            '''
            # Define API Parameter
            endpoint = map_endpoint_url.file
            endpointpara = map_endpoint_url.para_file
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,map=True,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def series_meta(**kwarg): 
            '''
            ['file_type','series_id']
            '''
            # Define API Parameter
            endpoint = map_endpoint_url.series
            endpointpara = map_endpoint_url.para_series
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,map=True,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def series_regional(**kwarg): 
            '''
           ['file_type','series_id','date','start_date']
            '''
            # Define API Parameter
            endpoint = map_endpoint_url.series_regional
            endpointpara = map_endpoint_url.para_series_regional
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,map=True,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def regional(**kwarg): 
            '''
           ['file_type','series_group','region_type','date','start_date','season','units','transformation','frequency','aggregation_method']
            '''
            # Define API Parameter
            endpoint = map_endpoint_url.regional
            endpointpara = map_endpoint_url.para_regional
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,map=True,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None