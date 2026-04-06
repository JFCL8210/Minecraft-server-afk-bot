import os
import time
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

def run_guard():
    print(f"--- [JLMTR 終極繞道模式] 啟動 ---")
    
    with sync_playwright() as p:
        # 啟動瀏覽器
        browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
        context = browser.new_context(viewport={'width': 1280, 'height': 720})
        page = context.new_page()
        stealth_sync(page)

        # 我們測試三個不同的網址，增加成功率
        targets = [
            "https://jlmtrandworld.falix.app",          # 你的伺服器位址
            "https://falixnodes.net",                   # 官網首頁 (防禦最鬆)
            "https://client.falixnodes.net/auth/login"  # 原始面板
        ]

        for url in targets:
            try:
                print(f"正在嘗試連線至: {url}")
                # 只要伺服器有回應 (commit)，就算成功敲門
                response = page.goto(url, wait_until="commit", timeout=30000)
                
                if response and response.status <= 399:
                    print(f"✅ 成功！收到代碼 {response.status}。")
                    print(f"JLMTR 伺服器活動訊號已送達。")
                    break # 成功一個就停止，避免被鎖 IP
                else:
                    print(f"⚠️ 失敗，代碼: {response.status if response else '無回應'}")
            except Exception as e:
                print(f"❌ 連線 {url} 發生錯誤。")
        
        browser.close()
        print("--- 任務結束 ---")

if __name__ == "__main__":
    run_guard()
