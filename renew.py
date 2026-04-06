from playwright.sync_api import sync_playwright
import os
import time

def run_jlmtr_guard():
    print(f"--- [JLMTR 守護模式：效能優化版] 啟動 ---")
    
    with sync_playwright() as p:
        # 增加啟動參數，讓瀏覽器跑得更快、佔用更少記憶體
        browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()

        try:
            print("正在連接至 FalixNodes...")
            # 只要拿到 DOM 內容就停止等待 (commit)，不用等圖片跑完，節省時間
            page.goto("https://client.falixnodes.net/auth/login", timeout=45000, wait_until="commit")
            
            # 給它 3 秒鐘讓基本的 JavaScript 觸發
            time.sleep(3)
            
            title = page.title()
            print(f"✅ 連接成功！目前頁面：{title}")
            
        except Exception as e:
            print(f"⚠️ 依然超時或錯誤，但可能已觸發活動訊號: {str(e)}")
        
        finally:
            browser.close()
            print("--- 任務結束 ---")

if __name__ == "__main__":
    run_jlmtr_guard()
