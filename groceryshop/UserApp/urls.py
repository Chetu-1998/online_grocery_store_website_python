from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login',views.login),
    path('Signup',views.Signup),
    path('ShowGroceries/<id>',views.ShowGroceries),
    path('ViewDetails/<id>',views.ViewDetails),
    path('Signout',views.Signout),
    path('addToCart',views.addToCart),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('MakePayment',views.MakePayment),
    path('removeItem',views.removeItem),
    path('demo',views.demo),
    path('About',views.About),
    path('Contact',views.Contact),
    path('Termsandcondition',views.Termsandcondition),
    path('News',views.News),
    
    
]
