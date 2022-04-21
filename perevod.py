import requests

IAM_TOKEN = 't1.9euelZqVz5mRj46Xkc2Uy56UmY-Vne3rnpWanIvOiZXNnpfJlJ7PkJabyZbl8_djOnts-e8hXx4A_d3z9yNpeGz57yFfHgD9.5A5hme4465e4KmRiNYRNx4uDzN7NJXBAuGktgWBSOoD1C9Vdsa-GguNMemziB6DqkODxnRmm3q4BCNgbwSImCg'
folder_id = 'b1gd129pp9ha0vnvf5g7'
target_language = 'ru'
texts = ["Hello", "World"]

body = {
    "targetLanguageCode": target_language,
    "texts": texts,
    "folderId": folder_id,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {0}".format(IAM_TOKEN)
}

response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
    json = body,
    headers = headers
)

print(response.text)
if __name__ == "__main__":
    print()

