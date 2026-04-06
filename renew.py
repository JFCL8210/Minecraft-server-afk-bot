import os
import requests
import time

# 從 Secrets 讀取資料
email = os.environ.get('FALIX_EMAIL')
target_url = "https://client.falixnodes.net/auth/login"

def run_ultimate_guard():
    print(f"--- [JLMTR 深度偽裝模式] 啟動 ---")
    
    # 極致偽裝標頭：模仿最新版 Chrome 的所有行為
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        session = requests.Session()
        
        # 1. 先隨機訪問一個子頁面，騙過 Cloudflare 的初步檢查
        print("正在繞過邊緣防火牆...")
        session.get("https://client.falixnodes.net/", headers=headers, timeout=20)
        
        time.sleep(2) # 模擬人類思考停頓 2 秒
        
        # 2. 正式訪問登入頁面觸發續期
        response = session.get(target_url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            print(f"✅ 成功突破 403 封鎖！狀態代碼: 200")
            print(f"JLMTR 伺服器已成功接收到活動心跳。")
        elif response.status_code == 403:
            print(f"❌ 依然顯示 403。這代表 Falix 的 Cloudflare 擋得非常死。")
            print("建議：嘗試把 main.yml 的執行頻率降低（例如每 15 分鐘一次）。")
        else:
            print(f"⚠️ 收到代碼 {response.status_code}，請檢查網頁是否正常。")

    except Exception as e:
        print(f"❌ 連線異常: {str(e)}")

if __name__ == "__main__":
    run_ultimate_guard()
    print(f"結束時間: {time.strftime('%H:%M:%S')}")
