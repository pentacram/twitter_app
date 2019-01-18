from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseindexview, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('add/post/', views.add_post_view, name="add-post"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('timeline/slug/', views.timeline_view, name="timeline"),
]
