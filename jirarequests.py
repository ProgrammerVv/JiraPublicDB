import jira
from jira import JIRA
import consoleinterface as console
import math
import numpy as np
import pandas as pd


def get_project(jira_auth_info):  # get project-names
    connection_params = jira_auth_info
    projects = connection_params.projects()
    return projects


def issue_total(jira_auth_info, jql):  # Get total issues from jira
    total_issues_from_jql = jira_auth_info.search_issues(jql).total  # get total
    #math.ceil(total_issues_from_jql)  # total round
    return total_issues_from_jql


def issue_finder(jira_auth_info, jql, total):  # Get issues from jira and append all to list
    """
    :param jira_auth_info:
    :return:
    """
    all_issues = []
    #total = 100 FOR TESTS
    i = 0
    while 1000 * i < total:
        all_issues.append(jira_auth_info.search_issues(jql, maxResults=1000, startAt=1000 * i,
                                                       fields=[
                                                           'project',  # Project'
                                                           'issuetype',  # Issue type
                                                           'reporter',  # Reporter
                                                           'assignee',  # Assignee
                                                           'summary',  # Summary
                                                           'priority',  # Priority
                                                           'status',  # Status
                                                           'labels',  # Labels
                                                           'customfield_10301',  # Cost
                                                           'customfield_12600',  # Project manager


                                                       ]))  # Issues from JQL
        #console.loading_indicator(all_issues)  # one loop loading interface
        #console.loading_indicator_int(total)  # fix it in consoleinterface file
        i += 1
        print('Loop count (one loop = 1000 issues)', i)

    return all_issues


def get_issue(jira_auth_info, key):  # get issue information (custom fields)
    issue = jira_auth_info.issue(key)
    issue_fields = [
        issue.fields.summary,
        issue.fields.project.key,
        issue.fields.issuetype.name,
        issue.fields.reporter.displayName,
        issue.fields.description,
    ]
    return issue_fields


def convert_to_dataframe(issues_from_jql):  # Convert all DataFrame

    rows = []
    for page in issues_from_jql:
        for issue in page:
            elem = issue.raw['fields']

            val = {}

            # SYSTEM FIELDS
            val['id'] = issue.id
            val['key'] = issue.key
            val['project key'] = issue.fields.project.key
            val['issue type'] = issue.fields.issuetype.name
            val['summary'] = issue.fields.summary
            try:
                val['assignee'] = issue.fields.assignee.displayName
            except:
                val['assignee'] = 'Unassigned'

            try:
                val['reporter'] = issue.fields.reporter.displayName
            except:
                val['reporter'] = 'No reporter'

            val['priority'] = issue.fields.priority.name
            val['status'] = issue.fields.status.name

            # # CASTOM FIELDS

            # try:
            #     val['projectManager'] = issue.fields['customfield_12600']['displayName'] # return 0 beacuse inactive - check it
            # except TypeError:
            #     val['projectManager'] = ' '
            #
            # try:
            #     val['cost'] = issue.fields.customfield_10301
            # except TypeError:
            #     val['cost'] = 0


            rows.append(val)

    dataframe_issues = pd.DataFrame(rows)
    return dataframe_issues


def convert_dataframe_to_tuple(dataFrame):

    convert_dataframe_to_tuple = [tuple(x) for x in dataFrame()]

    return convert_dataframe_to_tuple