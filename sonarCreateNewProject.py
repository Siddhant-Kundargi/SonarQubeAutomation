import requests as r

user_token = "squ_728be71f02926b246121dcbadf3cf8c2cca56755"
URL = "http://localhost:9000/api/projects/create"

project_name = "AssetSummaryService"
branch_name = "someRandomBranch"
data = {
    "project": project_name + branch_name + "-key",
    "name": project_name,
    "mainBranch": branch_name
}

headers = { "Authorization": f"Bearer {user_token}"}
req = r.post(URL, data=data, headers=headers)
print(req.content)

class SonarQube:

    """
    Simple ORM to work with SonarQube server
    """
    def __init__(self, sonarqube_url: str, user_token: str):
        self.sonarqube_url  = sonarqube_url
        self.token          = user_token
    
    def create_project(self, project_name: str, branch_name: str) -> dict:
        project_key = project_name + branch_name + '-key'

        data_to_post = {
            "project": project_key,
            "name": project_name,
            "mainBranch": branch_name
        }
        
        headers = { 
            "Authorization": f"Bearer {user_token}"
        }
        
        response = r.post(URL, data=data_to_post, headers=headers)

        project_properties = response.json['project']

        return project_properties