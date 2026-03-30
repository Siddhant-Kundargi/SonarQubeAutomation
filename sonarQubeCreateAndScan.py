import requests as r
import subprocess.Popen

user_token = "squ_728be71f02926b246121dcbadf3cf8c2cca56755"
URL = "http://localhost:9000/api/projects/create"

SONAR_CLI_PATH = "C:\\Users\\Siddhant.Kundargi\\Downloads\\sonar-scanner-cli-6.2.1.4610-windows-x64\\sonar-scanner-6.2.1.4610-windows-x64\\bin\\sonar-scanner.bat"

project_name = "test_proj"
branch_name = "someRandomBranch"
data = {
    "project": project_name + branch_name + "-key",
    "name": project_name,
    "mainBranch": branch_name
}

headers = { "Authorization": f"Bearer {user_token}"}
res = r.post(URL, data=data, headers=headers)

response_data = res.json

key = response_data['project']['key']

sonar_scanner_output = subprocess.Popen([SONAR_CLI_PATH, f'-Dsonar.projectKey={key}', f'-Dsonar.sources={}'], )