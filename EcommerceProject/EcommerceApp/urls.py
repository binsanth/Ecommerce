from . import views
from django.urls import path
app_name='EcommerceApp'
urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='home'),
    path('<slug:c_slug>/<slug:p_slug>/',views.product_details,name='ProDetail'),
]
