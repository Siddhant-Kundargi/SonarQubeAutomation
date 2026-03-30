import requests as r

user_token = "squ_728be71f02926b246121dcbadf3cf8c2cca56755"
URL = "http://localhost:9000/api/projects/search"

project_name = "AssetSummary"
branch_name = "someRandomBranch"
data = {
    'q': "project_name"
}

headers = { "Authorization": f"Bearer {user_token}"}
req = r.get(URL, data=data, headers=headers)

response = [(i['name'],i['key']) for i in req.json()['components']]
