import os
import time
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

def run_guard():
    print(f"--- [JLMTR 終極守護] 啟動 ---")
    
    with sync_playwright() as p:
        # 啟動瀏覽器，關閉沙盒模式以加快速度
        browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-gpu'])
        context = browser.new_context(viewport={'width': 1280, 'height': 720})
        page = context.new_page()
        
        # 套用隱身插件
        stealth_sync(page)

        try:
            print("正在嘗試繞過驗證碼並進入 Falix 面板...")
            # 1. 訪問頁面，等待時間縮短為 45 秒防止整體超時
            page.goto("https://client.falixnodes.net/auth/login", wait_until="networkidle", timeout=45000)
            
            # 2. 模擬真人等待
            time.sleep(5)
            
            # 3. 截圖保存（這是最關鍵的，如果 Error 了，你可以去 Actions 的檔案區看這張圖）
            page.screenshot(path="status_check.png")
            print(f"✅ 頁面已加載，標題：{page.title()}")
            print("活動訊號已發送。")

        except Exception as e:
            print(f"❌ 發生錯誤: {str(e)}")
            # 出錯也要截圖
            page.screenshot(path="error_view.png")
        
        finally:
            browser.close()
            print("--- 任務結束 ---")

if __name__ == "__main__":
    run_guard()
