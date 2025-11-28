import requests
import llm_api_key as api_key

def embed(text: str):
    """
    使用 Ollama 的 DeepSeek embedding 模型
    """
    url = "https://api.siliconflow.cn/v1/embeddings"
    payload = {
        "model": "BAAI/bge-large-zh-v1.5",
        "input": f"{text}"
    }
    headers = {
        "Authorization": f"Bearer {api_key.my_api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    res = response.json()
    print(res)
    return res['data'][0]['embedding']

if __name__ == "__main__":
    vec_words = embed("你好")




