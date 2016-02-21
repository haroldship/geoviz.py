#
#
#
print 'loading geoviz.py'

class Map(object):
    def __init__(self, data, style, endpoint=None, url=None):
        self.data = data
        self.style = style
        self.endpoint = endpoint
        self.url = url
        if self.url and not self.endpoint:
            self.endpoint = self.url

    def publish(self):
        self.url = self.endpoint + '/path/to/something'
        return self.url

    def update(self):
        if not self.url:
            raise RuntimeError('cannot update without url') 
        pass

    def show(self):
        return '<iframe src="http://www.yahoo.com">'

print 'geoviz.py loaded'

