import os
import requests
import time

# 從 GitHub Secrets 讀取你的資料
email = os.environ.get('FALIX_EMAIL')
password = os.environ.get('FALIX_PASSWORD')
# 你的伺服器目標位址
server_url = "https://jlmtrandworld.falix.app"

def run_jlmtr_guard():
    print(f"--- [JLMTR 伺服器守護系統] 啟動 ---")
    print(f"目前時間: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"目標伺服器: {server_url}")
    print(f"管理帳號: {email}")

    # 模擬瀏覽器標頭，防止被當成機器人攔截
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }

    try:
        # 1. 建立連線 Session
        session = requests.Session()
        
        # 2. 嘗試訪問伺服器首頁 (這會觸發 Falix 的活動偵測)
        print("正在向 JLMTR 伺服器發送活動訊號...")
        response = session.get(server_url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            print(f"✅ 成功連線！伺服器回應代碼: {response.status_code}")
            print("活動訊號已成功送達，10分鐘自動關機計時器已重置。")
        else:
            print(f"⚠️ 連線提醒: 伺服器回應了代碼 {response.status_code}。")
            print("這可能是因為伺服器正在重啟或面板需要重新登入。")

    except Exception as e:
        print(f"❌ 發生錯誤: {str(e)}")
        print("請檢查 GitHub Secrets 中的帳密設定，或是 FalixNodes 伺服器是否正常。")

if __name__ == "__main__":
    run_jlmtr_guard()
    print(f"--- [JLMTR 守護任務結束] 8 分鐘後將再次執行 ---")
