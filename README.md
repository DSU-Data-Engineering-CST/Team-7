# Reddit Post Analysis

This project implements an ETL (Extract, Transform, Load) pipeline that streams posts from specific subreddits using the Reddit API, transforms the data, and loads it into a MySQL database.

## 🔧 Features

- Streams posts from subreddits like `StockMarket` and `investing`
- Extracts relevant fields such as title, author, score, and creation time
- Transforms data into a structured format
- Loads data into a MySQL database for storage and analysis

---

## 📁 Project Structure

```
reddit_etl/
├── extract.py         # Extracts data from Reddit using PRAW
├── transform.py       # Cleans and structures data
├── load.py            # Loads data into MySQL
├── main.py            # Orchestrates the ETL process
├── .env               # Environment variables (NOT tracked in Git)
├── requirements.txt   # Python dependencies
└── README.md          # Project overview and setup
```

---

## 🔐 Reddit API Setup

1. Visit [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click **Create App**:
   - **Name**: `reddit_etl`
   - **Type**: `script`
   - **Redirect URI**: `http://localhost`
3. Copy the **client ID** and **client secret**.

Create a `.env` file in the root directory:

```
MYSQL_HOST=localhost
MYSQL_USER=airflow
MYSQL_PASSWORD=airflow_password
MYSQL_DATABASE=airflow
```

> 🔒 Do NOT commit your `.env` to version control

---

## 🧱 MySQL Setup

Run the following SQL commands to prepare your database:

```sql
CREATE DATABASE reddit_etl;

USE reddit_etl;

CREATE TABLE posts (
    id VARCHAR(10) PRIMARY KEY,
    title TEXT,
    score INT,
    url TEXT,
    author VARCHAR(255),
    num_comments INT,
    upvote_ratio FLOAT,
    created DATETIME,
    subreddit VARCHAR(100),
    flair VARCHAR(100)
);
```

Update your DB credentials in `load.py` accordingly.

---

##  Python Dependencies

Install all dependencies with:

```bash
pip install -r requirements.txt
```

### `requirements.txt` contents:

```
praw
python-dotenv
mysql-connector-python
pandas
```

---

## 🚀 Running the ETL Pipeline

Run the pipeline using:

```bash
python main.py
```

---

## 📌 Default Subreddits

The pipeline fetches data from:
- `StockMarket`
- `investing`

Modify `main.py` to change these.

---

## 🙌 Contributions

#Team 7 DSU-Data-Engineering-CST

