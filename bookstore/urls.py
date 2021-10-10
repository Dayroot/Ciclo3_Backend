
from django.contrib import admin
from django.urls import path
from bookstoreApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', views.EmployeeView.as_view()),
    path('workarea/', views.WorkAreaView.as_view()),
    path('magazine/', views.MagazineView.as_view()),
    
]
