from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.MainView.as_view(), name='base'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('ReadAboutView/', views.ReadAboutView.as_view(), name='ReadAboutView'),



   path('login/', views.loginpage, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('index', views.PostView.as_view(), name='index'),
    path('Customer_registration/', views.Customer_registration.as_view(), name='Customer_registration'),
    path('ServiceList/', views.ServiceList.as_view(), name='ServiceList'),
    path('OrderList/', views.OrderLists.as_view(), name='OrderLists'),
    path('OrderList/<int:pk>', views.OrderDeteil.as_view(), name='OrderView'),
    path('OrderUpdate/<int:pk>', views.OrderUpedate.as_view(), name='OrderUpdate'),
    path('OrderDelete/<int:pk>', views.OrderDelete.as_view(), name='OrderDelete'),
    path('DeleteCustomerOrder/<int:pk>', views.DeleteCustomerOrder.as_view(), name='DeleteCustomerOrder'),

  
  #class basede view  theat create the order



    path('create_order/', views.CreateOrder.as_view(), name='create_order'),
# fuction based create order
   
    path('customerorder/',views.customerorder,name='customerorder'),





]