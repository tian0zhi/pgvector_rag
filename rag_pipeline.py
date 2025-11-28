import requests
from search import search_similar
import llm_api_key as api_key


def rag_answer(query: str, top_k: int = 5):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    docs = search_similar(query, top_k)

    context = "\n\n".join([d["content"] for d in docs])

    prompt = f"""
你是一个知识检索助手。根据以下检索到的内容回答用户问题。
如果检索内容不足，请合并常识合理补充。

===检索内容===
{context}

===问题===
{query}

请给出清晰、有条理的回答。
"""
    print(prompt)
    payload = {
    "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    "messages": [
        {
            "role": "user",
            "content": f"{prompt}"
        }
    ]
    }
    headers = {
        "Authorization": f"Bearer {api_key.my_api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    res = response.json()["choices"][0]["message"]["content"]

    return res


if __name__ == "__main__":
    print(rag_answer("逆变器的作用是什么？"))
