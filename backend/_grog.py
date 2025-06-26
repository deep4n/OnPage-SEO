import requests

def get_grog_response(prompt, _grog_api_key):
    """
    Mengirimkan prompt ke Grog API dan mendapatkan respons.
    
    Args:
        prompt (str): Prompt yang akan dikirimkan ke Grog API.
        api_key (str): API key Grog API.
        
    Returns:
        dict: Respons dari Grog API.
    """
    url = "https://api.grog.com/generate"
    headers = {
        "Authorization": f"Bearer {_grog_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "model": "llama3",  # Menentukan model yang digunakan
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}
