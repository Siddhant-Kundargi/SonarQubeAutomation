import requests as r
import dotenv
from os import environ, path

# ENV_FILE = path.join(path.dirname(__file__), '.env')
# dotenv.load_dotenv(path.dirname)

user_token = "squ_728be71f02926b246121dcbadf3cf8c2cca56755"
URL = "http://localhost:9000/api/projects/bulk_delete"

# project_name = "test_proj"
# branch_name = "someRandomBranch"
data = {
    "q": "Asset"
}

headers = { "Authorization": f"Bearer {user_token}"}
req = r.post(URL, data=data, headers=headers)
print(req.content)