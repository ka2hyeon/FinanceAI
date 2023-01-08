import os 

def get_mariadb_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 1315 if host == "localhost" else 1315
    #user = input("[DB] Enter user name:")
    #password = input("[DB] Enter password:")
    user = "ka2hyeon"
    password = "1541666"
    
    db_name = "Asset"
    return f"mariadb+mariadbconnector://{user}:{password}@{host}:{port}/"\
            f"{db_name}"

def get_postgres_uri():
    pass


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 1316 if host == "localhost" else 1316
    return f"http://{host}:{port}"