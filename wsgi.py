def application(environ, start_response):
    import sys
    path = '/var/www/webroot/ROOT'
    if path not in sys.path:
        sys.path.append(path)

    #from pyinfo import pyinfo
    #output = pyinfo()
    output = environ
    start_response('200 OK', [('Content-type', 'text/html')])
    return str(output)
    #yield output.encode('utf-8')

#import sys
#sys.path.insert(0,"/var/www/webroot/ROOT/")
#print(environ)
#from myapp import app as application
