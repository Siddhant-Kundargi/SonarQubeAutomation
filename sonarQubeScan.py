# from Sonar import SonarQube
# # from sonarCreateNewProject import URL, user_token

# import subprocess
# from os import system

user_token = "squ_728be71f02926b246121dcbadf3cf8c2cca56755"
URL = "http://localhost:9000/"

sonar_scanner_path = r"c:\Users\Siddhant.Kundargi\Downloads\sonar-scanner-cli-6.2.1.4610-windows-x64\sonar-scanner-6.2.1.4610-windows-x64\bin\sonar-scanner.bat"

# params = [
#     sonar_scanner_path,
#     "-Dsonar.host.url=http://localhost:9000", 
#     "-Dsonar.token=squ_728be71f02926b246121dcbadf3cf8c2cca56755", 
#     "-Dsonar.projectKey=AssetSummaryServicenotmain-key", 
#     "-Dsonar.sources=C:\\Users\\Siddhant.Kundargi\\code.repo\\POC.repo\\SonarQubePOC\\ProjectRepos\\AssetSummaryService"
# ]


# out = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# print(out.stdout.read(), out.stderr.read())
from Sonar import SonarQube

sq = SonarQube(URL, user_token, sonar_scanner_path)

project_scan_result = sq.scan_project(project_key="AssetSummaryServicenotmain-key", sources="C:\\Users\\Siddhant.Kundargi\\code.repo\\POC.repo\\SonarQubePOC\\ProjectRepos\\AssetSummaryService")

if type(project_scan_result) == tuple:
    print(project_scan_result[1])
else:
    print("success")