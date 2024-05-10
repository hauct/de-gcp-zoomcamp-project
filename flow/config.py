from dotenv import load_dotenv
import os

basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env'))

class endpoint_url:
    main_url                        = 'https://api.stlouisfed.org/fred'
    main_url_geo                    = 'https://api.stlouisfed.org/geofred'

class category_endpoint_url:
    category                        = '/category?'
    child_category                  = '/category/children?'
    related_category                = '/category/related?'
    series_category                 = '/category/series?'
    tags_category                   = '/category/tags?'
    realted_tag                     = '/category/related_tags?'
    para_category                   = ['file_type','category_id']
    para_child_category             = ['file_type','category_id','realtime_start','realtime_end']
    para_related_category           = ['file_type','category_id','realtime_start','realtime_end']
    para_series_category            = ['file_type','category_id','realtime_start','realtime_end','limit','offset','order_by','sort_order','filter_variable','filter_value','tag_names','exclude_tag_names']
    para_tags_category              = ['file_type','category_id','realtime_start','realtime_end','tag_names','tag_group_id','search_text','limit','offset','order_by','sort_order']
    para_realted_tag                = ['file_type','category_id','realtime_start','realtime_end','tag_names','exclude_tag_names','tag_group_id','search_text','limit','offset','order_by','sort_order']