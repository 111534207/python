# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    TYPE_CHOICES = (
        ('movie', '電影'),
        ('tv', '影集'),
    )

    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    media_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='movie')

    def __str__(self):
        return f"{self.title} ({self.media_type})"

class UserMovie(models.Model):
    # 👇 1. 定義狀態選項
    STATUS_CHOICES = [
        ('watchlist', '待看清單'),
        ('watching', '觀看中'),
        ('watched', '已看完'),
        ('dropped', '棄劇'),
    ]

    # 👇 2. 基本欄位 (維持原本設計，直接存資料，比較簡單)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.CharField(max_length=20, blank=True, null=True)
    media_type = models.CharField(max_length=10, default='movie')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="加入時間")
    
    # 👇 3. 新增功能欄位 (狀態、評分、心得)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='watchlist', # 預設加入時都是 "待看"
        verbose_name="狀態"
    )
    
    rating = models.IntegerField(
        null=True, 
        blank=True, 
        choices=[(i, f'{i} 星') for i in range(1, 6)], # 1~5星
        verbose_name="評分"
    )
    
    review = models.TextField(blank=True, null=True, verbose_name="觀影心得")

    # 👇 4. Meta 設定 (這會幫你依照加入時間，新的排前面)
    class Meta:
        ordering = ['-added_at']

    def __str__(self):
        # get_status_display() 可以自動把 'watchlist' 轉成 '待看清單'
        return f"{self.user.username} - {self.title} ({self.get_status_display()})"