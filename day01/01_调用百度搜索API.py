# 导入requests包
import requests
import json

# 测试请求
# print(requests.__version__)

# 923-新闻列表查询 - 代码参考（根据实际业务情况修改）

# 基本参数配置
apiKey = '自己的API_KEY'  # 在个人中心->我的数据,接口名称上方查看


# 封装接口请求方法
def get_news(channel='top', count=10):
    """
    调用聚合数据新闻头条API的函数
    :param channel: 新闻频道，可选值：
                    "top"（头条，默认）、"guonei"（国内）、
                    "guoji"（国际）、"keji"（科技）、"tiyu"（体育）
    :param count: 要返回多少条结果，默认10条
    :return: 新闻列表
    """
    # 1. API的请求地址（聚合数据提供的接口）
    apiUrl = 'https://v.juhe.cn/toutiao/index'  # 接口请求URL

    # 2. 构造请求参数
    requestParams = {
        'key': apiKey,      # 聚合数据API Key
        'type': channel,    # 新闻频道
        'page_size': count  # 返回条数
    }
    try:
        # 3. 发送GET请求（和之前介绍的GET方法一致）
        response = requests.get(apiUrl, params=requestParams, timeout=10)

        # result = response.json()
        # print("完整的API返回数据是：")
        # print(result)
        # # 为了方便阅读，也可以使用更美观的格式来打印
        # print(json.dumps(result, indent=4, ensure_ascii=False))

        # 4. 检查请求是否成功，如果失败就抛出错误
        # 解析响应结果
        if response.status_code == 200:
            responseResult = response.json()
            # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
            print(responseResult)
        else:
            # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
            print('请求异常')
            print(response.status_code)
            print(response.text)
            print(response.content)
            print(response.json())
            return None
        return responseResult.get('result').get('data')
    except Exception as e:
        # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
        print('请求异常')
        print(e)
        return None


if __name__ == '__main__':
    print(f"正在获取科技新闻...\n")
    newsList = get_news(channel='yule', count=10)
    for news in newsList:
        print(f"标题：{news.get('title')}")
        print(f"来源：{news.get('author_name')}")
        print(f"时间：{news.get('date')}")
        print(f"类别：{news.get('category')}")
        print('-' * 50)
