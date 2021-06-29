import authJira as aj
import params as p
import jirarequests as jr
import authDatabase as db
import dbrequests as dbr


def main():
    conection = aj.jira_auth(p.params_for_jira_connect[0], p.params_for_jira_connect[1], p.params_for_jira_connect[2])  # get auth for jira requests
    total_of_jira_issues = jr.issue_total(conection, p.jql)  # Get issue total
    print('Count issues from jira:  ', total_of_jira_issues)  # Count of issues
    list_with_issues_jira = jr.issue_finder(conection, p.jql, total_of_jira_issues)  # foo add all tasks from jira by jql
    data = jr.convert_to_dataframe(list_with_issues_jira)  # Convert list from jira request to Dataframe
    print(data)
    db_connect = db.db_connect(p.params_for_db_connect)  # Connect to db and get the client
    dbr.db_request(db_connect)
    #print(jr.convert_dataframe_to_tuple(data)) convert dataframe to tuple
    dbr.insert_data_to_database(db_connect, data)  # Insert data to database



main()


#fix progress bars (not now)