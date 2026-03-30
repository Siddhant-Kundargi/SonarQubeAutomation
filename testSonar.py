from Sonar import SonarQube

USER_TOKEN = "squ_728be71f02926b246121dcbadf3cf8c2cca56755"
URL = "http://localhost:9000/"
SONAR_SCANNER_PATH = r"c:\Users\Siddhant.Kundargi\Downloads\sonar-scanner-cli-6.2.1.4610-windows-x64\sonar-scanner-6.2.1.4610-windows-x64\bin\sonar-scanner.bat"

sq = SonarQube(URL, USER_TOKEN, SONAR_SCANNER_PATH)

project_key = sq.create_project("AssetSummaryService", "notmain")['key']

print(project_key)

scanning_result = sq.scan_project(project_key, r'C:\Users\Siddhant.Kundargi\code.repo\POC.repo\SonarQubePOC\ProjectRepos\AssetSummaryService')

print(scanning_result)

deletion_success = sq.delete_project(project_key=project_key)

print(deletion_success)