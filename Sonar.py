import requests
import urllib.parse
import subprocess

class SonarQube:

    """
    Simple ORM to work with SonarQube server
    """
    def __init__(self, sonarqube_url: str, user_token: str, sonar_scanner_path: str):
        self.sonarqube_url  = sonarqube_url
        self.token          = user_token
        self.headers        = { 
            "Authorization": f"Bearer {self.token}"
        }
        self.sonar_scanner_path = sonar_scanner_path

    def get_project(self, search_string: str):

        url_suffix = "/api/projects/search"
        url_to_send = urllib.parse.urljoin(self.sonarqube_url, url_suffix)
        
        data = {
            'q': "project_name"
        }

        response = requests.get(url_to_send, data=data, headers=self.headers)

        projects = [(i['name'],i['key']) for i in response.json()['components']]

        return projects


    def create_project(self, project_name: str, branch_name: str) -> dict:
        project_key = project_name + branch_name + '-key'

        if self.get_project(project_key):
            return {"key": project_key}

        url_suffix = "/api/projects/create"
        url_to_send = urllib.parse.urljoin(self.sonarqube_url, url_suffix)

        data_to_post = {
            "project": project_key,
            "name": project_name,
            "mainBranch": branch_name
        }
        
        response = requests.post(url_to_send, data=data_to_post, headers=self.headers)

        project_properties = response.json()['project']
        return project_properties
        
    def scan_project(self, project_key: str, sources: str, debug: bool = False, **kwargs):

        scan_command = [
            self.sonar_scanner_path,
            f"-Dsonar.host.url={self.sonarqube_url}", 
            f"-Dsonar.token={self.token}", 
            f"-Dsonar.projectKey={project_key}", 
            f"-Dsonar.sources={sources}"
        ]

        for key, value in kwargs.items():
            scan_command.append(f"-Dsonar.{key}={value}")

        scan_command_output = subprocess.Popen(scan_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        _, err = scan_command_output.communicate()

        if err:
            if debug:
                return False, err
            return bool, err
        
        return True

    def check_if_project_exists(self, project_key: str):
        url_suffix = "/api/projects/search"
        url_to_send = urllib.parse.urljoin(self.sonarqube_url, url_suffix)
        
        data = {
            'projects': f"{project_key}"
        }

        response = requests.get(url_to_send, data=data, headers=self.headers)

        return len(response.json()['components'])
                
    def delete_project(self, project_name: str = '', branch_name: str = '', project_key: str = ''):

        if project_key:
            if not self.check_if_project_exists(project_key):
                return False, "project key not exist"
        elif project_name and branch_name:
            project_key = self.get_project(project_name + branch_name + "-key")
            if not project_key:
                return False, "project data not valid"
            else:
                project_key = project_key[0][1]
        else:
            return False, "insufficient data"

        url_suffix = "/api/projects/delete"
        url_to_send = urllib.parse.urljoin(self.sonarqube_url, url_suffix)

        data_to_post = {
            "project": project_key,
        }
        
        requests.post(url_to_send, data=data_to_post, headers=self.headers)

        return not self.check_if_project_exists(project_key), f"final {project_key}" 