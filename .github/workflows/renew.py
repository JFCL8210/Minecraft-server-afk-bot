import os

def test():
    email = os.environ.get('FALIX_EMAIL')
    if email:
        print(f"成功讀取到帳號: {email}")
    else:
        print("錯誤：找不到 FALIX_EMAIL，請檢查 Secrets 設定！")

if __name__ == "__main__":
    test()
