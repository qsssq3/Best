from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index' ),
    path('ilsan/', views.ilsan, name='ilsan'),
    path('busan/', views.busan, name='busan'),
    path('FAQ/', views.faq, name='FAQ'),
    path('schedule/', views.schedule, name='schedule'),
    path('setec_site/', views.setec_site, name='setec_site'),
    path('setec/', views.setec, name='setec'),
    path('suwon/', views.suwon, name='suwon'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('bexcosite/', views.bexcosite, name='bexcosite'),
    path('kintexsite/', views.kintexsite, name='kintexsite'),
    path('note/', views.note, name='note'),
    path('price/', views.price, name='price'),
    path('suwonsite/', views.suwonsite, name='suwonsite'),
    path('team/', views.team, name='team'),
]