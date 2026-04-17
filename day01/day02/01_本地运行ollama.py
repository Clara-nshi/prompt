import ollama

client = ollama.Client(host="http://127.0.0.1:11434")


def call_ollama(prompt):
    """
    使用ollama进行对话
    :param prompt: 你的问题/提示词
    :return: AI的回复内容
    """
    res = client.chat(
        model="deepseek-r1:1.5b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return res.message.content


if __name__ == '__main__':
    # 1. 生成不同思路：3个
    question = """一个商店卖铅笔，每支2元。如果小明有20元，他最多能买多少支铅笔？"""

    step1_prompt = f"""
                    你是一个数学老师。请用3种不同的方法来推理这个问题，只需给出推理思路，不需要解答。思路需要简洁明了，并且合理有效。
                    输出格式必须为：["思路1","思路2","思路3"] ,不要有多余内容!!!
                    问题如下：
                    {question}
                    """

    solution_list = call_ollama(step1_prompt)
    print(f'step1_result->{solution_list}')

    # 2.循环遍历每个思路
    step2_result_list = []
    for solution in eval(solution_list):
        # 将每个思路拼接成一个prompt，分别调用大模型得到结果
        step2_prompt = f"""
                        你是一个数学老师。请用如下的思路来解决这个问题。只输出答案即可。
                        思路：
                        {solution}
                        问题：
                        {question}"""
        step2_result = call_ollama(step2_prompt)
        step2_result_list.append(step2_result)
    print(f'step2_result_list->{step2_result_list}')

    # 3. 每个思路的结果进行投票
    step3_prompt = f"""
                    你是一个公正的投票专家，能够根据用户输入的list格式的多个答案进行投票，哪个答案出现的次数最多
                    你就返回哪个答案，需要注意，返回的答案只需要有计算结果就行，不要有过程。
                    用户输入的多个答案：
                    {step2_result_list}
                    """

    step3_result = call_ollama(step3_prompt)

    print(f'step3_result->{step3_result}')
