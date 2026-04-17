# 导包
from openai import OpenAI

# 创建客户端对象
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key="ollama",  # 如果要调用本地ollama模型,此处apikey不能省略,但是内容可以任意填写,建议写ollama见名知意
    base_url="http://127.0.0.1:11434/v1",
)


def get_translate_result(question):
    # TODO 提前定义系统提示词
    SYSTEM_PROMPT = '''
    你是一个翻译专家,请将用户输入的英文翻译成中文
    '''
    # 直接聊天
    res = client.chat.completions.create(
        model="deepseek-r1:1.5b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        stream=False,
        temperature=0.6
    )
    return res.choices[0].message.content


if __name__ == '__main__':
    question = input("请输入要翻译的英文:")
    data = get_translate_result(question)
    print(data)
