from django.urls import path,include
from coffeeapp import views
from . import views
from .views import SearchResultsView



urlpatterns = [
    path('', views.FirstPage, name='first'),
    path('<int:id>',views.coffee_detail,name='coffeedetail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('search/',SearchResultsView.as_view(),name='search_results'),

    path('add_to_cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart_items',views.cart_items,name='cart_items'),
    path('remove_from_cart/<int:coffee_id>',views.remove_from_cart,name='remove_from_cart'),
    path('add_address',views.add_address,name='add_address')
    

    


]

