import sqlite3
import json
from tqdm import tqdm

def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)

    return conn

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT data FROM events WHERE type_name = 'user' AND timestamp > 1611538386.96759")
    rows = cur.fetchall()
    
    return rows

def unixtime2standardtime(unix_time):
    unix_timestamp = float(unix_time)
    local_timezone = tzlocal.get_localzone()
    local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
    return (local_time.strftime("%B %d %Y"))

if __name__ == '__main__':
    conn = create_connection('/app/database/cpp.db')
    data_rows = select_all_tasks(conn)

    with open('user_ask.txt', 'w') as f:
        for i in tqdm(range(len(data_rows))):
            if not json.loads(data_rows[i][0])['parse_data']['intent']['name']:
                f.write(json.loads(data_rows[i][0])['text'] + ',None' + '\n')
            else:
                if json.loads(data_rows[i][0])['parse_data']['entities']:
                    f.write(json.loads(data_rows[i][0])['text'] + '\t||\t' 
                                + json.loads(data_rows[i][0])['parse_data']['intent']['name'] + '\t||\t' + 
                                   json.loads(data_rows[i][0])['parse_data']['entities'][0]['value'] + '\n')
                else:
                    f.write(json.loads(data_rows[i][0])['text'] + '\t||\t' 
                                + json.loads(data_rows[i][0])['parse_data']['intent']['name'] + '\n')
    
    print('Done')