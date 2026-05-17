import time
import pandas as pd
from sqlalchemy import create_engine


DB_USER = "user"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "my_database"

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def connect_with_retry(max_attempts=10, delay=10):
    for attempt in range(1, max_attempts + 1):
        try:
            engine = create_engine(DATABASE_URL)
            with engine.connect() as connection:
                print("Connected to MySQL successfully.")
            return engine
        except Exception as error:
            print(f"Attempt {attempt} failed: {error}")

            if attempt < max_attempts:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise Exception("Could not connect to MySQL after several attempts.")


def main():
    engine = connect_with_retry()

    query = "SELECT * FROM titanic;"
    df = pd.read_sql(query, engine)

    print(df)
    print(f"\nRows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")


if __name__ == "__main__":
    main()