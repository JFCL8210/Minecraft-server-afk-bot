import os
import requests
import time

# 從 GitHub Secrets 讀取資料
email = os.environ.get('FALIX_EMAIL')
password = os.environ.get('FALIX_PASSWORD')
server_url = "https://jlmtrandworld.falix.app"

def run_guard():
    print(f"--- JLMTR 守護系統啟動 ---")
    print(f"目標伺服器: {server_url}")
    
    # 模擬瀏覽器訪問，重置 Falix 的 10 分鐘關機計時器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        session = requests.Session()
        # 訪問伺服器網址
        response = session.get(server_url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            print(f"✅ 成功連線！活動訊號已送達。")
            print(f"JLMTR 伺服器目前狀態正常，已重置關機倒數。")
        else:
            print(f"⚠️ 伺服器回應代碼: {response.status_code}，請檢查伺服器是否開機。")
            
    except Exception as e:
        print(f"❌ 發生錯誤: {str(e)}")

if __name__ == "__main__":
    run_guard()
    print(f"執行時間: {time.strftime('%H:%M:%S')}，下次 9 分鐘後巡邏。")
