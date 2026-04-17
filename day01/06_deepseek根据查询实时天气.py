# 导入requests包
import requests
from openai import OpenAI

# ==================== 配置区 ====================
# 和风天气 API Key
WEATHER_API_KEY = "bcd606132d064a84b10b63b4739b5fdb"

# DeepSeek API Key
DEEPSEEK_API_KEY = "自己的API_KEY"

# 初始化 DeepSeek
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

# 和风天气接口
BASE_URL = "https://mv76x9vmk7.re.qweatherapi.com"


# ==================== 获取实时天气 ====================
def get_weather(city_id):
    url = f"{BASE_URL}/v7/weather/now"
    params = {
        "location": city_id,
        "key": WEATHER_API_KEY
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            res = response.json()
            # 和风天气成功码是 code: 200
            if res.get("code") != "200":
                print("API错误：", res)
                return None
            return res.get('now')
        return None
    except Exception as e:
        print("请求异常：", e)
        return None


# ==================== AI 总结天气 ====================
def summarize_weather(weather):
    # 构造天气信息文本
    weather_text = f"""
当前天气情况：
天气状况：{weather.get('text')}
温度：{weather.get('temp')}℃
体感温度：{weather.get('feelsLike')}℃
风向：{weather.get('windDir')}
风速：{weather.get('windSpeed')}
湿度：{weather.get('humidity')}%
    """

    # 让 AI 总结天气
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个贴心的天气播报助手，用简洁友好的语气总结天气"},
            {"role": "user", "content": f"请根据以下天气信息，用自然口语总结今天天气：\n\n{weather_text}"}
        ]
    )
    return response.choices[0].message.content


# ==================== 主程序 ====================
if __name__ == '__main__':
    print("🔍 正在获取北京天气...\n")

    # 北京城市ID：101010100
    weather = get_weather("101010100")

    if weather:
        print("🤖 AI 正在总结天气...\n")
        summary = summarize_weather(weather)
        print("=" * 60)
        print("☀️ 今日天气播报：\n")
        print(summary)
        print("=" * 60)
    else:
        print("未获取到天气信息")
