from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('adminsecure2/', admin.site.urls),
    path('', include("store.urls", namespace='store')),
    path('carts/', include('carts.urls', namespace='carts')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('orders/', include('orders.urls', namespace='orders'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)