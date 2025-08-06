from openai import OpenAI

client = OpenAI(
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key='sk-ed9855eafd804709aee7bb68627688b5'
)

resp = client.chat.completions.create(
    model='qwen-Plus-Latest',
    messages=[
        # {"role": 'user', "content": "qwen3的大模型有什么特点？<think>\n"}
        {"role": 'user', "content": "什么是深度学习？"}
    ],
    extra_body={
        "chat_template_kwargs": {'enable_thinking': False}
    }
)

print(resp.choices[0].message)