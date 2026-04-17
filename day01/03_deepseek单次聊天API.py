# Please install OpenAI SDK first: `pip3 install openai`
import os
# 导入 openai 库
from openai import OpenAI

# --------------------------
# 把你刚才申请到的 DeepSeek API Key 填进去！
# --------------------------
# 创建客户端
client = OpenAI(
    # base_url 要指向 DeepSeek 的 API 地址，因为 DeepSeek 兼容 OpenAI 格式
    api_key="自己的API_KEY",
    base_url="https://api.deepseek.com")


def chat_with_deepseek(prompt, system_prompt=None, temperature=0.7):
    """
    使用 DeepSeek API进行对话
    :param prompt: 你的问题/提示词
    :param system_prompt: 系统提示词，用来设定AI的角色和行为（可选）
    :return: AI的回复内容
    """

    # 构造消息列表
    messages = []

    # 如果有系统提示词，先加上（告诉 AI 它是什么角色）
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    # 加上用户的问题
    messages.append({"role": "user", "content": prompt})

    try:
        # 调用 API
        # 添加系统提示词
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=temperature,
            timeout=30
        )
        # 提取 AI 的回复内容
        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    print("===== DeepSeek API 测试 =====\n")
    print("【示例1】基础问答：")
    print(chat_with_deepseek("解释一下什么是面向对象"))