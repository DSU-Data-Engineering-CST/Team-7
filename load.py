import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def load_data(df):
    if df.empty:
        print("DataFrame is empty. Skipping DB load.")
        return

    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reddit_posts (
                id VARCHAR(20),
                title TEXT,
                score INT,
                url TEXT,
                author VARCHAR(255),
                num_comments INT,
                upvote_ratio FLOAT,
                created DATETIME,
                subreddit VARCHAR(100),
                flair TEXT
            )
        ''')

        for _, row in df.iterrows():
            cursor.execute('''
                INSERT INTO reddit_posts (id, title, score, url, author, num_comments, upvote_ratio, created, subreddit, flair)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', tuple(row))

        conn.commit()
        print("Data loaded successfully.")

    except Exception as e:
        print("Error loading to database:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
