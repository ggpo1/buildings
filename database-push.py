import psycopg2
import json

def get_query_by_building(building: dict):
    return "insert into buildings (id, lat, lng) values (%i, %f, %f)" % (building["id"], building["lat"], building["lng"])

def push_nodes(nodes: list, conn, cursor):
    i = 0
    stop = 999999

    for node in nodes:
        if i >= stop: break
        cursor.execute(get_query_by_building(node))
        i = i + 1

    conn.commit()

def main():
    try:
        connection = psycopg2.connect(dbname='<db-name>', user='<db-user>', 
                                password='<db-user-password>', host='<db-host>')
        cursor = connection.cursor()

        input_data_file = open("./buildings.json", "r")
        file_json = input_data_file.read()
        input_data_file.close()

        push_nodes(json.loads(file_json), connection, cursor)

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into buildings:", error)

    finally:
        cursor.close()
        connection.close()

main()
