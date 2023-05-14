import openai
import json
import os

# path = os.path.expanduser('/Users/kansantoshiyuki/Library/CloudStorage/GoogleDrive-toshi.kanyama@gmail.com/マイドライブ/Private/APIKeys/APIKey.json')
path = os.path.expanduser('~/Library/CloudStorage/GoogleDrive-toshi.kanyama@gmail.com/マイドライブ/Private/APIKeys/APIKey.json')
f = open(path, 'r')
datajson = json.loads(f.read())
f.close()
key = datajson['APIKey']
openai.api_key = key


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "語頭には「ふむ。」、すべての語尾に「じゃ」か「のじゃ。」をつけて質問に短く答えてください"},
        {"role": "user", "content": "APIってなに？"},
    ]   
)
print(f"ChatGPT: {response['choices'][0]['message']['content']}")
print(response['usage'])
