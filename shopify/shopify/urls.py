
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from shop.admin import shop_site
from django.conf.urls.static import static

urlpatterns = [
    path('',include('musicapp.urls')),
    path('shopadmin/',shop_site.urls),
    path('admin/', admin.site.urls),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.index_title='Musicality'
admin.site.site_header='Musicality admin'
admin.site.site_title='Musicality'