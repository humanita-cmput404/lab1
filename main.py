import requests

repo_code = requests.get('https://raw.githubusercontent.com/humanita-cmput404/lab1/main/main.py').text
print(repo_code)