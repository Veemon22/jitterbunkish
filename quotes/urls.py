from django.urls import path
from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('form/', views.FormView.as_view(), name='form'),
    path('forms/', views.create_quote, name='create_quote'),
    path('filterquote/', views.quote_view, name='quote_view'),
    path('filtersource/', views.source_view, name='source_view'),
]