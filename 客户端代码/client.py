import json
import requests


def json_out():
    question: str = input("输入问题: ")
    url_path: str = "http://服务器ip:5505/gpt/" + question
    url = requests.get(url_path)
    data = json.loads(url.text)
    #print(data)
    print(data['content'])

if __name__ == '__main__':
    json_out()