from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from CMS import views

urlpatterns = [
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('home/',views.index,name='Home'), 
    path('about/',views.about,name='About'),
    path('status/',views.status,name='Status'),
    path('',views.index,name='Home'),
    path('dash/', include('dash.urls')),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

