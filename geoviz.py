#
#
#
print 'loading geoviz.py'

class Map(object):
    url = None
    endpoint = None
    data = None
    style = None

def publish(data, style, endpoint):
    map = Map()
    map.url = endpoint + '/stuff/goes/here'

print 'geoviz.py loaded'

