import requests

def get_chats():
    url = "http://192.168.8.253/api/v1/chats"
    headers = {
        "Authorization": "Bearer ragflow-UwMmM5YWU1MGFkZTExZjBiMzUyMDI0Mm"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 确保请求成功
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {str(e)}")
        return None

def create_chat_session(chat_id, session_name):
    """
    创建新的对话会话
    对应curl命令:
    curl --request POST \
         --url http://192.168.8.253/api/v1/chats/{chat_id}/sessions \
         --header 'Content-Type: application/json' \
         --header 'Authorization: Bearer ragflow-UwMmM5YWU1MGFkZTExZjBiMzUyMDI0Mm' \
         --data '{"name": "新的对话"}'
    """
    url = f"http://192.168.8.253/api/v1/chats/{chat_id}/sessions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer ragflow-UwMmM5YWU1MGFkZTExZjBiMzUyMDI0Mm"
    }
    payload = {
        "name": session_name
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # 确保请求成功
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"创建会话失败: {str(e)}")
        return None

def ask_question(chat_id, session_id, question):
    """
    发送问题并获取中文回答
    对应curl命令:
    curl --request POST \
         --url http://47.103.197.173:6068/api/v1/chats/{chat_id}/completions \
         --header 'Content-Type: application/json' \
         --header 'Authorization: Bearer ragflow-UwMmM5YWU1MGFkZTExZjBiMzUyMDI0Mm' \
         --data '{"question": "问题内容", "stream": false, "session_id": "会话ID"}'
    """
    url = f"http://47.103.197.173:6068/api/v1/chats/{chat_id}/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer ragflow-UwMmM5YWU1MGFkZTExZjBiMzUyMDI0Mm"
    }
    payload = {
        "question": question,
        "stream": False,
        "session_id": session_id,
        "language": "zh-CN"  # 新增语言参数
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"提问失败: {str(e)}")
        return None

if __name__ == "__main__":
    # chats = get_chats()
    # if chats:
    #     print(chats)

    # chats = create_chat_session('7057f5150acb11f09e3a0242ac170006', "新的对话")
    # print(chats)

    chats = ask_question('7057f5150acb11f09e3a0242ac170006', 'ec5f11150ae211f085240242ac170006', "彭朗是谁")
    print(chats)