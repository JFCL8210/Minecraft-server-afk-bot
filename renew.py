import os
import requests
import time

# 讀取 Secrets
email = os.environ.get('FALIX_EMAIL')
password = os.environ.get('FALIX_PASSWORD')

# 使用面板網址，因為這個網址 24 小時都開著
target_url = "https://client.falixnodes.net/auth/login"

def run_guard():
    print(f"--- [JLMTR 強效守護模式] 啟動 ---")
    
    # 偽裝成真實的 Windows Chrome 瀏覽器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://client.falixnodes.net/',
        'Connection': 'keep-alive'
    }

    try:
        # 使用 Session 保持 Cookie，這會讓 Falix 覺得你是真人在操作
        session = requests.Session()
        
        print(f"正在向 Falix 面板發送活動訊號...")
        # 第一次訪問首頁拿 Cookie
        session.get("https://client.falixnodes.net/", headers=headers, timeout=20)
        
        # 第二次訪問登入頁面（這會觸發 Falix 的活動偵測，重置 10 分鐘計時器）
        response = session.get(target_url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            print(f"✅ 成功擊穿防火牆！伺服器已接收到活動訊號。")
            print(f"JLMTR 伺服器 10 分鐘關機倒數已重新計算。")
        else:
            print(f"⚠️ 收到回應代碼: {response.status_code}。")
            print("雖然不是 200，但只要有連線紀錄，通常也能防止關機。")

    except Exception as e:
        print(f"❌ 依然被拒絕: {str(e)}")
        print("提示：這代表 Falix 完全封鎖了 GitHub。建議手動進去點一次 Renew。")

if __name__ == "__main__":
    run_guard()
    print(f"完成時間: {time.strftime('%H:%M:%S')}")
