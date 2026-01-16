import requests

# 建議將來這行要放在環境變數，現在練習先直接填
TMDB_API_KEY = 'd9421c1104e8d7b3958ef76e67c0cdf7'

def search_movie_from_api(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': TMDB_API_KEY,
        'query': query,
        'language': 'zh-TW'
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get('results', [])
            # 簡單處理一下資料，確保沒有空的
            formatted_results = []
            for item in results:
                # 略過沒有圖片或標題的殘缺資料
                if not item.get('poster_path') or not item.get('title'):
                    continue
                    
                formatted_results.append({
                    'tmdb_id': item['id'],
                    'title': item['title'],
                    'release_date': item.get('release_date', '未知'),
                    # 組合完整圖片網址
                    'poster_url': f"https://image.tmdb.org/t/p/w500{item['poster_path']}",
                    'overview': item.get('overview', '')
                })
            return formatted_results
    except Exception as e:
        print(f"API Error: {e}")
    
    return []


def get_trending_movies():
    """取得本週熱門電影"""
    url = "https://api.themoviedb.org/3/trending/movie/week"
    params = {
        'api_key': TMDB_API_KEY, # 記得確認你的變數名稱跟上面一樣
        'language': 'zh-TW'
        
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get('results', [])
            formatted_results = []
            
            for item in results:
                # 只抓取資料完整的電影
                if not item.get('poster_path') or not item.get('title'):
                    continue
                    
                formatted_results.append({
                    'tmdb_id': item['id'],
                    'title': item['title'],
                    'release_date': item.get('release_date', '未知'),
                    'poster_url': f"https://image.tmdb.org/t/p/w500{item['poster_path']}",
                    'overview': item.get('overview', '')
                })
            return formatted_results
    except Exception as e:
        print(f"API Error: {e}")
        
    return []