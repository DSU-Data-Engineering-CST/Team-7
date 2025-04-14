import praw
import os
from dotenv import load_dotenv
import time
from datetime import datetime

# Load env vars
load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    check_for_async=False
)

def stream_reddit(subreddit_names, post_limit=10):
    extracted_data = []

    for subreddit_name in subreddit_names:
        print(f"Fetching posts from subreddit: {subreddit_name}")
        try:
            subreddit = reddit.subreddit(subreddit_name)
            count = 0
            seen_ids = set()

            while count < post_limit:
                for submission in subreddit.new(limit=10):
                    if submission.id in seen_ids:
                        continue

                    seen_ids.add(submission.id)
                    post = {
                        "id": submission.id,
                        "title": submission.title,
                        "score": submission.score,
                        "url": submission.url,
                        "author": submission.author.name if submission.author else 'Unknown',
                        "num_comments": submission.num_comments,
                        "upvote_ratio": submission.upvote_ratio,
                        "created": datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                        "subreddit": subreddit_name,
                        "flair": submission.link_flair_text
                    }

                    extracted_data.append(post)
                    print(f"Fetched post: {post['title']}")
                    count += 1

                    if count >= post_limit:
                        break

                time.sleep(5)  # avoid rate limit

        except Exception as e:
            print(f"Error fetching from subreddit {subreddit_name}: {e}")
            time.sleep(5)

    return extracted_data

# For direct testing
if __name__ == "__main__":
    subreddits = ["StockMarket", "investing"]
    data = stream_reddit(subreddits, post_limit=5)
    for d in data:
        print(d)
