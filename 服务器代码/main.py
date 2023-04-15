import json
import requests
import openai

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return dict(content=hello)

@app.route('/gpt/<path:paths>') # <path:paths>是一个变量，转换器类型是path类型
def get_path(paths):# 参数是必须传递的
    
  
    openai.api_key = "sk-AmH"  # 填写api_key
    question: str = paths  
    completion = openai.ChatCompletion.create(  
    model="gpt-3.5-turbo",  
    stream=True,  
    messages=[{"role": "user", "content": question}]  
    )  
      
    collected_events = [] # 响应接收区  
    stream_result = '' # 保存流式输出的总结果  
    
    for event in completion:  
        collected_events.append(event) # 保存事件响应  
        data_dict = event.to_dict() # 转换响应为字典  
        data_openai_object = data_dict['choices'][0] # 获取choices的值  
        data_json = data_openai_object.to_dict() # 转换openai_object为字典  
        data_openai_object = data_json['delta'] # 获取delta的值  
        finish_reason = data_json['finish_reason'] # 获取finish的值,用于判断是否传输结束  
        data_json = data_openai_object.to_dict() # 转换openai_object为字典  
        segmental_result = data_json.get('content', "null") # 获取content的值，如果没有就返回null  
      
        if(segmental_result != "null"): # 判断“分段结果”内是否有内容，有就输出  
            # print(segmental_result, end="") # 输出“分段结果“的内容
            stream_result += segmental_result  # 合并分段结果到总结果

    return dict(content=stream_result)



if __name__ == '__main__':
    app.run(host='::',port = 5505)