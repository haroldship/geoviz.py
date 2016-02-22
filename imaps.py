#
#
#

class Map(object):
    def __init__(self, data, endpoint, apikey=None, apikey_password=None, mapid=None):
        self.data = data
        self.endpoint = endpoint
        if endpoint[-1] != '/':
            endpoint += '/'
        self.apikey = apikey
        self.apikey_password = apikey_password
        self.mapid = mapid
        self.url = self.endpoint + '/maps/' + self.mapid

    def publish(self):
        return self.url

    def update(self, style):
        if not self.url:
            raise ValueError('cannot update without url') 
        self.style = style




