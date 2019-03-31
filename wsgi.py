import sys
sys.path.insert(0,"/var/www/webroot/ROOT/")
print(environ)
from myapp import app as application
