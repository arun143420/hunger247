from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^food/', include('food.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^ordermanage/', include('ordermanage.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)