
import requests as re
from config import category_endpoint_url
from API_helper.util.util import _build_url

class category:

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

    def chlid_category(**kwarg):
        """
        category_id    int  : The id for a category.
        realtime_start str  : The start of the real-time period. YYYY-MM-DD formatted string
        realtime_end   str  : The end of the real-time period. YYYY-MM-DD formatted string
        """
        # Define API Parameter
        endpoint = category_endpoint_url.child_category
        endpointpara = category_endpoint_url.para_child_category
        # Contruct the url request    
        url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
        try:
            result = re.get(url_requst)
            return result
        except Exception as error:
            print(f"An error occured '{error}'. Please check the parameter pass.")
            return None

    def related_category(**kwarg):
        """
        category_id    int  : The id for a category.
        realtime_start str  : The start of the real-time period. YYYY-MM-DD formatted string'
        realtime_end   str  : The end of the real-time period. YYYY-MM-DD formatted string'
        """
        # Define API Parameter
        endpoint = category_endpoint_url.related_category
        endpointpara = category_endpoint_url.para_related_category
        # Contruct the url request    
        url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
        try:
            result = re.get(url_requst)
            return result
        except Exception as error:
            print(f"An error occured '{error}'. Please check the parameter pass.")
            return None

    def series_category(**kwarg):
        """
        category_id         int  : The id for a category.
        realtime_start      str  : The start of the real-time period. YYYY-MM-DD formatted string'
        realtime_end        str  : The end of the real-time period. YYYY-MM-DD formatted string'
        limit               int  : The maximum number of results to return
        offset              int  : offset postion of result
        order_by            str  : Order results by values of the specified attribute.
                                   'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 
                                   'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 
                                   'observation_end', 'popularity', 'group_popularity'.
        sort_order          str  : Sort results is ascending or descending One of the following strings: 'asc', 'desc'.
        filter_variable     str  : The attribute to filter results by.'frequency', 'units', 'seasonal_adjustment'.
        filter_value        str  : The value of the filter_variable attribute to filter results by.
        tag_names           str  : A semicolon delimited list of tag names that series match all of. 
                                   Example value: 'income;bea'. Filter results to series having both tags 'income' and 'bea'.
        exclude_tag_names   str  : A semicolon delimited list of tag names that series match none of.
                                   Example value: 'discontinued;annual'. Filter results to series having neither tag 'discontinued' nor tag 'annual'.
        """
        # Define API Parameter
        endpoint = category_endpoint_url.series_category
        endpointpara = category_endpoint_url.para_series_category
        # Contruct the url request    
        url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
        try:
            result = re.get(url_requst)
            return result
        except Exception as error:
            print(f"An error occured '{error}'. Please check the parameter pass.")
            return None

    def tag_category(**kwarg):
        """
        category_id         int  : The id for a category.
        realtime_start      str  : The start of the real-time period. YYYY-MM-DD formatted string'
        realtime_end        str  : The end of the real-time period. YYYY-MM-DD formatted string'
        limit               int  : The maximum number of results to return
        offset              int  : offset postion of result
        order_by            str  : Order results by values of the specified attribute.
                                   'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 
                                   'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 
                                   'observation_end', 'popularity', 'group_popularity'.
        sort_order          str  : Sort results is ascending or descending One of the following strings: 'asc', 'desc'.
        tag_group_id        str  : One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'.
                                   req = Frequency
                                   gen = General or Concept
                                   geo = Geography
                                   geot = Geography Type
                                   rls = Release
                                   seas = Seasonal Adjustment
                                   src = Source
        tag_names           str  : A semicolon delimited list of tag names that series match all of. 
                                   Example value: 'income;bea'. Filter results to series having both tags 'income' and 'bea'.
        exclude_tag_names   str  : A semicolon delimited list of tag names that series match none of.
                                   Example value: 'discontinued;annual'. Filter results to series having neither tag 'discontinued' nor tag 'annual'.
        search_text         str  : The words to find matching tags with.
        """
        # Define API Parameter
        endpoint = category_endpoint_url.tags_category
        endpointpara = category_endpoint_url.para_tags_category
        # Contruct the url request    
        url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
        try:
            result = re.get(url_requst)
            return result
        except Exception as error:
            print(f"An error occured '{error}'. Please check the parameter pass.")
            return None

    def relatetag_category(**kwarg):
        """
        category_id         int  : The id for a category.
        realtime_start      str  : The start of the real-time period. YYYY-MM-DD formatted string'
        realtime_end        str  : The end of the real-time period. YYYY-MM-DD formatted string'
        limit               int  : The maximum number of results to return
        offset              int  : offset postion of result
        order_by            str  : Order results by values of the specified attribute.
                                   'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 
                                   'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 
                                   'observation_end', 'popularity', 'group_popularity'.
        sort_order          str  : Sort results is ascending or descending One of the following strings: 'asc', 'desc'.
        tag_group_id        str  : One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'.
                                   req = Frequency
                                   gen = General or Concept
                                   geo = Geography
                                   geot = Geography Type
                                   rls = Release
                                   seas = Seasonal Adjustment
                                   src = Source
        tag_names           str  : A semicolon delimited list of tag names that series match all of. 
                                   Example value: 'income;bea'. Filter results to series having both tags 'income' and 'bea'.
        exclude_tag_names   str  : A semicolon delimited list of tag names that series match none of.
                                   Example value: 'discontinued;annual'. Filter results to series having neither tag 'discontinued' nor tag 'annual'.
        search_text         str  : The words to find matching tags with.

        """
        # Define API Parameter
        endpoint = category_endpoint_url.realted_tag
        endpointpara = category_endpoint_url.para_realted_tag
        # Contruct the url request    
        url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
        try:
            result = re.get(url_requst)
            return result
        except Exception as error:
            print(f"An error occured '{error}'. Please check the parameter pass.")
            return None