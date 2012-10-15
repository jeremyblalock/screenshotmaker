
from django.conf.urls.defaults import *

#company_resource = resources.CompanyResource()

urlpatterns = patterns('app',
    #url(r'', include(company_resource.urls)),
    url(r'^$', 'views.index')
)

