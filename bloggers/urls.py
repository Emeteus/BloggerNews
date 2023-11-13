from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import home, blogger_details, add_blogger


urlpatterns = [
    path('', views.home, name='home'),
    path('blogger_profiles/', views.blogger_profiles, name='blogger_profiles'),
    path('blogger_details/<int:blogger_id>/', views.blogger_details, name='blogger_details'),
    path('news/', views.news, name='news'),
    path('blogger/<int:blogger_id>/', blogger_details, name='blogger_detail'),
    path('add/', add_blogger, name='add_blogger'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
