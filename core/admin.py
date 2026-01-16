# core/admin.py
from django.contrib import admin
# 👇 注意這裡：我們改成匯入 UserMovie (不是 UserMovieList 了)
from .models import Movie, UserMovie

@admin.register(UserMovie)
class UserMovieAdmin(admin.ModelAdmin):
    # 👇 修改這裡：把 'movie' 改成 'title'
    # 並加上我們新做的 status 和 rating
    list_display = ('user', 'title', 'status', 'rating', 'added_at')
    
    # 右側篩選器 (選填，方便你管理)
    list_filter = ('status', 'added_at')
    
    # 搜尋功能 (選填)
    search_fields = ('title', 'user__username')