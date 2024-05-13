from dotenv import load_dotenv
import os

basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env.config'))

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
    
class clean_df:
    series_col      = ['id', 'realtime_start', 'realtime_end', 'title', 'observation_start','observation_end', 'frequency', 'frequency_short', 'units','units_short', 'seasonal_adjustment', 'seasonal_adjustment_short','last_updated', 'popularity', 'group_popularity']
    series_str_col  = ['id', 'title', 'observation_start','observation_end', 'frequency', 'frequency_short', 'units','units_short', 'seasonal_adjustment', 'seasonal_adjustment_short','last_updated']
    series_int_col  = ['popularity','group_popularity']
    series_date_col = ['realtime_start','realtime_end','last_updated']

class query_bq:
    query_getseriesPara = f'''
    SELECT distinct id FROM `{os.getenv("Gcp_Project_id")}.dbt_prod.stg_category`
where parent_name  in ('Interest Rates','International Data','Money, Banking, & Finance','National Income & Product Accounts','Prices','National Accounts','Current Employment Statistics (Establishment Survey)','	Productivity & Costs','U.S. Trade & International Transactions','U.S. Regional Data') 
order by id
    '''
    
    query_getMapPara =f'''
    SELECT 
    [region_type]
      ,[series_group]
      ,[season]
      ,[units]
      ,[frequency]
      ,min_date
 FROM `{os.getenv("Gcp_Project_id")}.dbt_prod.series_group`
where Active = 1
order by series_group
    '''