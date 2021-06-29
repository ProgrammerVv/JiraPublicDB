import authDatabase


def db_request(client):  # function for requests to database

    print(client.execute('SHOW DATABASES;'))
    #print(client.execute('USE DATABASE Jira;'))



def insert_data_to_database(client,data):  # Insert data to database
    client.insert_dataframe(
    'INSERT INTO jira.issues (*) VALUES', data
        )

    print('______________________________________')
    print('Data was insert into database success!')
    print('______________________________________')