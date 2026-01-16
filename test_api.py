import requests
import json

# === 這裡填入你剛剛拿到的 API Key ===
API_KEY = 'd9421c1104e8d7b3958ef76e67c0cdf7' 
# ==================================

def test_search(query):
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': API_KEY,
        'query': query,
        'language': 'zh-TW'  # 設定繁體中文
    }
    
    print(f"正在搜尋: {query} ...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        
        if results:
            print(f"成功！找到了 {len(results)} 筆結果。")
            first_movie = results[0]
            print("--- 第一筆結果 ---")
            print(f"電影名稱: {first_movie.get('title')}")
            print(f"上映日期: {first_movie.get('release_date')}")
            print(f"大綱: {first_movie.get('overview')[:50]}...") # 只顯示前50字
            print(f"海報路徑: {first_movie.get('poster_path')}")
        else:
            print("連線成功，但沒有找到相關電影。")
    else:
        print(f"錯誤！狀態碼: {response.status_code}")
        print("請檢查 API Key 是否正確。")

if __name__ == "__main__":
    test_search("哈利波特") # 測試搜尋哈利波特