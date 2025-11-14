import requests
import json

# Kimi API configuration
API_KEY = "sk-xCUgjubcKVXVJf2OGX69tzNauMlxMTGviwPzVkNrWtKF6Ntt"
API_URL = "https://api.moonshot.cn/v1/chat/completions"

def test_kimi_api():
    """ทดสอบการเชื่อมต่อ Kimi API"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # ข้อความทดสอบ
    data = {
        "model": "moonshot-v1-8k",
        "messages": [
            {
                "role": "user",
                "content": "สวัสดี ทดสอบ API"
            }
        ],
        "temperature": 0.7
    }

    try:
        print("กำลังทดสอบ Kimi API...")
        print(f"API URL: {API_URL}")
        print("-" * 50)

        response = requests.post(API_URL, headers=headers, json=data, timeout=30)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("\n✓ API ใช้งานได้!")
            print("\nการตอบกลับ:")
            print(json.dumps(result, indent=2, ensure_ascii=False))

            if 'choices' in result and len(result['choices']) > 0:
                message = result['choices'][0]['message']['content']
                print(f"\nข้อความตอบกลับ: {message}")

            return True
        else:
            print(f"\n✗ API ใช้งานไม่ได้!")
            print(f"Error: {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"\n✗ เกิดข้อผิดพลาดในการเชื่อมต่อ!")
        print(f"Error: {str(e)}")
        return False
    except Exception as e:
        print(f"\n✗ เกิดข้อผิดพลาด!")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_kimi_api()
