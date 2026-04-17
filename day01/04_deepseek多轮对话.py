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


# 多轮对话示例：创建一个AI助手
def multi_turn_chat():
    # 初始化消息列表，这个列表会保存所有的对话历史
    messages = [
        {"role": "system", "content": "你是一个 乐于助人 的AI助手， 名字叫小深"}
    ]
    print("AI助手[小深]已启动！输入'quit'退出对话\n")
    while True:
        # 获取用户输入
        user_input = input("用户：")
        if user_input.lower() == 'quit':
            print("对话结束")
            break
        # 把用户的消息加入历史
        messages.append({"role": "user", "content": user_input})

        try:
            # 调用 API
            # 添加系统提示词
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=0.7
            )
            # 提取 AI 的回复内容
            reply = response.choices[0].message.content
            print(f"小深: {reply}\n")
            # 把AI的回复加入历史
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(e)


if __name__ == '__main__':
    multi_turn_chat()