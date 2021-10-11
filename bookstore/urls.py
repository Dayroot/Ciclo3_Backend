
from django.contrib import admin
from django.urls import path
from bookstoreApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    #staff
    path('admin/', admin.site.urls),
    path('employee/', views.EmployeeView.as_view()),
    path('workarea/', views.WorkAreaView.as_view()),
    
    #Business
    path('sale/', views.SaleView.as_view()),
    path('reservation/', views.ReservationView.as_view()),
    
    #Products
    path('magazine/', views.MagazineView.as_view()),
    path('book/', views.MagazineView.as_view()),
    
    #Customer
    path('customer-registration/', views.CustomerRegistrationView.as_view()),
    path('customer-detail/<int:pk>', views.CustomerDetailView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    
]
