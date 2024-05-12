
from API_helper.url_client.category import category

class url_module(object):
    '''
    Helper create for calling Fred API
    https://fred.stlouisfed.org/docs/api/fred/#API
    '''
    def __init__(self):
        ## Initiate clients
        self.category = category()
        self.map = map()