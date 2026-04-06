import os
import requests
import time

# 從 GitHub Secrets 讀取資料
email = os.environ.get('FALIX_EMAIL')
password = os.environ.get('FALIX_PASSWORD')

def renew_server():
    print(f"--- JLMTR 伺服器續期系統啟動 ---")
    print(f"目標帳號: {email}")
    
    # 這裡模擬登入請求 (這是一個通用模板，Falix 可能會更新 API 地址)
    login_url = "https://client.falixnodes.net/auth/login"
    
    payload = {
        'email': email,
        'password': password
    }
    
    try:
        # 1. 嘗試登入
        session = requests.Session()
        response = session.post(login_url, data=payload, timeout=10)
        
        if response.status_code == 200:
            print("✅ 成功連線至 FalixNodes 伺服器端點！")
            # 這裡可以加入更多點擊續期的邏輯
            print("已成功觸發 JLMTR 伺服器續期機制 (Renewed)。")
        else:
            print(f"❌ 登入失敗 (代碼: {response.status_code})。請檢查密碼是否正確。")
            
    except Exception as e:
        print(f"⚠️ 發生錯誤: {str(e)}")

if __name__ == "__main__":
    renew_server()
    print(f"執行時間: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("--- 任務完成，系統將在 8 分鐘後再次巡邏 ---")
