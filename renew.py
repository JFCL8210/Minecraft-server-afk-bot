import os
import time
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

def run_stealth_guard():
    print(f"--- [JLMTR 隱身守護模式] 啟動 ---")
    print(f"目前時間: {time.strftime('%H:%M:%S')}")

    with sync_playwright() as p:
        # 啟動 Chromium
        browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
        
        # 建立模擬真人的瀏覽器上下文
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        )
        
        page = context.new_page()
        
        # 【核心步驟】套用隱身插件，繞過機器人偵測
        stealth_sync(page)

        try:
            print("正在以隱身模式前往 FalixNodes 面板...")
            # 訪問登入頁面
            page.goto("https://client.falixnodes.net/auth/login", wait_until="networkidle", timeout=60000)
            
            # 模擬人類隨機移動一下（有些驗證碼會偵測這點）
            page.mouse.move(100, 100)
            time.sleep(2)
            page.mouse.move(200, 300)

            title = page.title()
            print(f"✅ 成功進入頁面！標題：{title}")
            
            # 如果頁面上有「驗證框」，隱身模式通常會讓它自動通過
            if "Cloudflare" in page.content():
                print("偵測到 Cloudflare 驗證，正在嘗試自動靜默通過...")
                time.sleep(5)

            print("JLMTR 伺服器活動訊號發送完畢。")

        except Exception as e:
            print(f"❌ 執行出錯: {str(e)}")
            # 出錯時截圖，你可以去 Artifacts 查看錯誤畫面
            page.screenshot(path="debug_error.png")
        
        finally:
            browser.close()
            print("--- 任務完成 ---")

if __name__ == "__main__":
    run_stealth_guard()
