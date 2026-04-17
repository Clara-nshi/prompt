# 导入requests包
import requests
import json

# 把刚申请到的API填到这里
API_KEY = "自己的API_KEY"

# 免费版的接口域名，不要改这个！
BASE_URL = "https://mv76x9vmk7.re.qweatherapi.com"


# 获取天气信息
def get_weather(city):
    """
    获取实时天气
    :param location: 地点，可以是城市ID（比如北京是101010100），也可以是经纬度（比如116.41,39.92）
    :return: 实时天气结果
    """
    # 拼接完整的接口URL
    url = f"{BASE_URL}/v7/weather/now"

    # 构造请求参数
    params = {
        "location": city,  # 要查的地点
        "key": API_KEY  # API KEY身份凭证
    }

    try:
        # 3. 发送GET请求（和之前介绍的GET方法一致）
        response = requests.get(url, params=params, timeout=10)

        # 查看返回是数据是什么样的，主要获取now中的数据
        # return responseResult.get('now')
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
        return responseResult.get('now')
    except Exception as e:
        # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
        print('请求异常')
        print(e)
        return None


# 获取 7 天天气预报
def get_weather_forecast(city):
    """
    获取 7 天天气预报
    """
    url = f"{BASE_URL}/v7/weather/7d"
    params = {
        "location": city,
        "key": API_KEY
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        # 查看返回是数据是什么样的，主要获取daily中的数据
        # return responseResult.get('daily')
        # result = response.json()
        # print("完整的API返回数据是：")
        # print(result)
        # # 为了方便阅读，也可以使用更美观的格式来打印
        # print(json.dumps(result, indent=4, ensure_ascii=False))

        if response.status_code == 200:
            responseResult = response.json()
            print(responseResult)
        else:
            print('请求异常')
            print(response.status_code)
            print(response.text)
            print(response.content)
            print(response.json())
            return None
        return responseResult.get('daily')
    except Exception as e:
        print('请求异常')
        print(e)
        return None


# 测试代码
if __name__ == '__main__':
    # 你要查的城市，这里用北京的城市ID
    cityID = "101010100"
    print(f"正在获取{cityID}的实时天气...")

    # 1. 查询实时天气
    now = get_weather(cityID)
    if now:
        print(f"{cityID}的实时天气是：{now.get('text')}")
        print(f"当前温度是：{now.get('temp')}")
        print(f"体感温度是：{now.get('feelsLike')}")
        print(f"风向是：{now.get('windDir')}")
        print(f"风速是：{now.get('windSpeed')}")
        print(f"相对湿度是：{now.get('humidity')}")

    # 查询7天预报
    forecast = get_weather_forecast(cityID)
    if forecast:
        print(f"正在获取{cityID}的7天天气预报...")
        for day in forecast:
            print(
                f"{day.get('fxDate')} {day.get('textDay')} 最高气温：{day.get('tempMax')} 最低气温：{day.get('tempMin')}")
