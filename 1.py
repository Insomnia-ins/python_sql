import sqlite3

connect = sqlite3.connect('people.db')
cursor = connect.cursor()

def query_users():
    cursor.execute("SELECT * FROM users;")
    all_results = cursor.fetchall()

    request_query = []
    request_query.append(int(all_results[-1][0])+1)
    request_query.append(input("Name: "))
    request_query.append(input("Age: "))
    request_query.append(input("Gender: "))
    
    request_query_ready = tuple(request_query)
    
    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", request_query_ready)
    connect.commit()
    

    
    

query_users()