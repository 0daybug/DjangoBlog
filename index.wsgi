import sae
from CloudBlog import wsgi

application = sae.create_wsgi_app(wsgi.application)
