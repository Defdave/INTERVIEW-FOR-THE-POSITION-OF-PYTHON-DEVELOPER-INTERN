from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_polling_unit_results/', views.add_polling_unit_results, name='add_polling_unit_results'),
    path('polling-unit-results/', views.polling_unit_results, name='polling_unit_results'),
    path('lga-results/', views.lga_results, name='lga_results'),
]
