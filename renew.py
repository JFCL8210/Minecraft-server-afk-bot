import os
import time
from playwright.sync_api import sync_playwright
# 修正導入方式：從 playwright_stealth 導入 stealth
from playwright_stealth import stealth

def run_guard():
    print(f"--- [JLMTR 終極修正版] 啟動 ---")
    print(f"目前時間: {time.strftime('%H:%M:%S')}")
    
    with sync_playwright() as p:
        # 啟動瀏覽器
        browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
        context = browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        # 修正後的隱身指令
        stealth(page)

        # 嘗試多個網址以避開 403
        targets = [
            "https://falixnodes.net",                   # 官網首頁 (最容易通)
            "https://client.falixnodes.net/auth/login",  # 面板登入
            "https://jlmtrandworld.falix.app"           # 你的伺服器
        ]

        for url in targets:
            try:
                print(f"正在連線至: {url}")
                # 使用 commit 模式，只要連上就算成功
                response = page.goto(url, wait_until="commit", timeout=30000)
                
                if response and response.status < 400:
                    print(f"✅ 成功！收到回應碼: {response.status}")
                    print(f"JLMTR 伺服器已成功接收活動訊號。")
                    break 
                else:
                    print(f"⚠️ 失敗，狀態碼: {response.status if response else 'Timeout'}")
            except Exception as e:
                print(f"❌ 連線錯誤: {str(e)}")
        
        browser.close()
        print("--- [任務結束] ---")

if __name__ == "__main__":
    run_guard()
