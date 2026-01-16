from django import forms
from .models import UserMovie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserMovieForm(forms.ModelForm):
    class Meta:
        model = UserMovie
        # 我們只允許使用者修改這三個欄位，其他像 user 或 movie 不該被改動
        fields = ['status', 'rating', 'review']
        
        # 這裡設定標籤名稱，讓網頁顯示中文
        labels = {
            'status': '觀看狀態',
            'rating': '評分 (1-10)',
            'review': '心得評論',
        }
        
        # 這裡用 widgets 來幫表單加上 Bootstrap 的樣式類別
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': '這部電影帶給你什麼感覺...?'}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email') # 這裡可以順便加上 email 欄位，如果需要的話
        
        # 這裡設定我們想要的中文標籤
        labels = {
            'username': '設定帳號',
            'email': '電子信箱 (選填)',
        }
        
        # 加上 Bootstrap 樣式
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入帳號'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    # 因為密碼欄位不是 Model 欄位，要特別在這邊處理中文和樣式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = "請輸入 150 個字元以內的字母、數字或 @/./+/-/_。"
        
        self.fields['password1'].label = "設定密碼"
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].help_text = "密碼長度至少 8 碼，且不能太過常見。"
        
        self.fields['password2'].label = "確認密碼"
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': '請再次輸入密碼'})