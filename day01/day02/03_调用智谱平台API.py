from zhipuai import ZhipuAI

client = ZhipuAI(api_key="自己的API_KEY")
response = client.chat.completions.create(
    model="glm-5.1",
    messages=[
        {
            "role": "system",
            "content": "你是一个有用的AI助手。"
        },
        {
            "role": "user",
            "content": "你好，请介绍一下自己。"
        }
    ]
)
print(response.choices[0].message.content)