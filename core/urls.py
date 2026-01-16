# core/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # 👈 匯入 Django 內建的登入視圖


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_movies, name='search_movies'),
    path('add/<int:tmdb_id>/', views.add_movie, name='add_movie'),   
    # 👇 這一行就是解決 dashboard 錯誤的關鍵！
    path('dashboard/', views.dashboard, name='dashboard'),
    path('remove/<int:movie_id>/', views.remove_movie, name='remove_movie'),
    path('edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),    
    # 註冊頁面 (我看你的截圖裡有 signup.html，所以這裡先預留著，如果沒有這個功能可以先忽略)
    # path('signup/', views.signup, name='signup'), 
    # 👇 新增這三行 (登入、登出、註冊)
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('movie/<int:tmdb_id>/', views.movie_detail, name='movie_detail'),
    path('dashboard/analysis/', views.movie_analysis, name='movie_analysis'),
    path('api/generate-review/', views.generate_ai_review, name='generate_ai_review'),
]


# from django.urls import path, include
# from . import views

# urlpatterns = [
#     # 首頁
#     path('', views.home, name='home'),
#     path('', views.my_dashboard, name='dashboard'),
#     # 搜尋頁面 (關鍵修改：views.search_movies 要加 s)
#     path('search/', views.search_movies, name='search_movies'),
#     path('search/', views.search_movie, name='search_movie'),
#     # 加入片單
#     path('add/', views.add_movie, name='add_movie'),
#     path('add/',views.add_to_list,name='add_to_list'),
#     # path('add/', views.add_movie, name='add_movie'),
#     path('edit/<int:pk>/', views.edit_list, name='edit_list'),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('signup/', views.signup, name='signup'),
#     path('delete/<int:pk>/', views.delete_from_list, name='delete_from_list'),
#     path('user/<str:username>/', views.public_profile, name='public_profile'),
# ]