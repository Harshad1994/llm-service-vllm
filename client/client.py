import requests

BASE_URL = "http://localhost:8004"
TOKEN_URL = f"{BASE_URL}/llm2/token"
GENERATE_URL = f"{BASE_URL}/llm2/generate"

def get_access_token():
    username ="llm"
    password = "PASSWORD"
    token_data = {
        "username": username,
        "password": password,
    }
    token_response = requests.get(TOKEN_URL, data=token_data)
    if token_response.status_code == 200:
        token_data = token_response.json()
        access_token = token_data.get("access_token")
        return access_token
    else:
        return None

def generate_completion(generate_config,access_token):
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    llm_response = requests.post(GENERATE_URL, json=generate_config, headers=headers)
    return llm_response

def generate(generate_config):

    # Get the access token
    access_token = get_access_token()

    if access_token:
        # Make the generate request with the obtained access token
        llm_response = generate_completion(generate_config,access_token)

        # Check if the access token is expired and retry the generate request with a new token
        if llm_response.status_code == 401:
            print("Access token expired. Retrying with a new token.")
            new_access_token = get_access_token()
            if new_access_token:
                llm_response = generate_completion(generate_config,new_access_token)
                print("Generate Response status code:", llm_response.status_code)
                print("Generate Response content:", llm_response.json())
            else:
                print("Failed to obtain a new access token.")
                return None
        else:
            print("Generate Response status code:", llm_response.status_code)
            print("Generate Response content:", llm_response.json())
    else:
        print("Failed to obtain access token.")
        return None

    return llm_response.json()

if __name__ == "__main__":

    prompt = "What is capital of India?"

    generate_config = {
        "prompt": prompt,
        "stream": False,
        "temperature":0,
        "max_tokens":50
        # Add other fields as needed for the SamplingParams
    }

    generate(generate_config)

