# 导入requests包
import requests
import json
from openai import OpenAI

# ==================== 配置区 ====================
# 聚合新闻 API Key
apiKey = '自己的API_KEY'

# DeepSeek API Key
DEEPSEEK_API_KEY = "sk-a9288b987af8466bb42b691a7eafa988"

# 初始化 DeepSeek
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

# ==================== 获取新闻 ====================
def get_news(channel='keji', count=10):
    apiUrl = 'https://v.juhe.cn/toutiao/index'
    params = {
        'key': apiKey,
        'type': channel,
        'page_size': count
    }
    try:
        response = requests.get(apiUrl, params=params, timeout=10)
        if response.status_code == 200:
            res = response.json()
            if res.get("error_code") != 0:
                print("API错误：", res.get("reason"))
                return None
            return res.get('result', {}).get('data', [])
        return None
    except Exception as e:
        print("请求异常：", e)
        return None

# ==================== AI 总结新闻 ====================
def summarize_news(news_list):
    # 把新闻拼成文本
    news_text = "今日科技新闻如下：\n\n"
    for i, news in enumerate(news_list, 1):
        news_text += f"{i}. {news.get('title')}\n"
        news_text += f"   时间：{news.get('date')}  来源：{news.get('author_name')}\n\n"

    # 让 AI 总结
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个科技新闻播报助手，帮用户简洁、清晰总结今天的科技新闻"},
            {"role": "user", "content": f"请根据以下新闻，用通顺自然的语言总结今天重要科技新闻：\n\n{news_text}"}
        ]
    )
    return response.choices[0].message.content

# ==================== 主程序 ====================
if __name__ == '__main__':
    print("🔍 正在获取今日科技新闻...\n")
    news_list = get_news(channel='keji', count=8)

    if news_list:
        print("🤖 AI 正在总结...\n")
        summary = summarize_news(news_list)
        print("=" * 60)
        print("📢 今日科技新闻总结：\n")
        print(summary)
        print("=" * 60)
    else:
        print("未获取到新闻")
