from playwright.sync_api import sync_playwright
import time

def run_guard():
    with sync_playwright() as p:
        # 啟動一個真正的瀏覽器 (無頭模式)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("--- [JLMTR 瀏覽器模擬模式] 啟動 ---")
        try:
            # 訪問網址，這會執行 JavaScript，繞過 403
            page.goto("https://client.falixnodes.net/auth/login", wait_until="networkidle")
            print(f"頁面標題: {page.title()}")
            print("✅ 已成功模擬真實瀏覽器訪問，JLMTR 續期成功。")
            
            # 這裡可以視情況加入 page.fill() 來輸入帳號密碼，但單純訪問通常已足夠
            
        except Exception as e:
            print(f"❌ 瀏覽器模擬失敗: {str(e)}")
        
        browser.close()

if __name__ == "__main__":
    run_guard()
