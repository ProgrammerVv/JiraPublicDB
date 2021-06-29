from jira import JIRA


def jira_auth(server_url, login, key_or_password):  # Auth
    jira_options = {'server': server_url}
    jira = JIRA(options=jira_options, basic_auth=(login, key_or_password))
    return jira
