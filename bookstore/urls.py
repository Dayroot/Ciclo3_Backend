
from django.contrib import admin
from django.urls import path
from bookstoreApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    #staff
    path('admin/', admin.site.urls),
    path('employee/', views.EmployeeView.as_view()),
    path('workarea/', views.WorkAreaView.as_view()),
    path('staff-login/', views.StaffTokenObtainPairView.as_view()),
    
    #Business
    path('shoppingCart/', views.ShoppingCartView.as_view()),
    path('shoppingCart_Product/', views.ShoppingCart_ProductView.as_view()),
    path('invoice/', views.InvoiceView.as_view()),
    path('invoice_product/', views.Invoice_ProductView.as_view()),
  
    #Products
    path('magazine/', views.MagazineView.as_view()),
    path('book/', views.BookView.as_view()),
    
    #Customer
    path('customer-management/', views.CustomerManagementView.as_view()),
    path('customer-registration/', views.CustomerRegistrationView.as_view()),
    path('customer-detail/<int:pk>', views.CustomerDetailView.as_view()),
    path('customer-login/', views.CustomerTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    
    #Analysis
    path('sales-year/', views.SalesPerYearView.as_view()),
    path('sales-month/', views.SalesPerMonthView.as_view()),
]
