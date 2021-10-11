
from django.contrib import admin
from django.urls import path
from bookstoreApp import views

urlpatterns = [
    #staff
    path('admin/', admin.site.urls),
    path('employee/', views.EmployeeView.as_view()),
    path('workarea/', views.WorkAreaView.as_view()),
    
    #Business
    path('sale/', views.SaleView.as_view()),
    path('reservation/', views.SaleView.as_view()),
    
    #products
    path('magazine/', views.MagazineView.as_view()),
    path('book/', views.MagazineView.as_view()),
]
