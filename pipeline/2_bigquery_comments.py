#to be run only after posts table has been created
#inserts values into comments table (already created by terraform)
from google.cloud import bigquery

# Set up BigQuery client with explicit project ID
bq_client = bigquery.Client(project='stackai-394819')

# Set up query to insert data into the table
query = """
    INSERT INTO StackAI.comments_cleaned (post_id, text, creation_date, score)
    SELECT
        c.post_id,
        COALESCE(c.text, 'N/A') AS text,
        COALESCE(FORMAT_DATE('%Y-%m-%d', DATE(c.creation_date)), 'N/A') AS creation_date,
        COALESCE(c.score, 0) AS score
    FROM
        `bigquery-public-data.stackoverflow.comments` c
    JOIN
        `stackai-394819.StackAI.posts_cleaned` p
    ON 
        c.post_id = p.question_id
"""

# Run query to insert data into the table
job_config = bigquery.QueryJobConfig()
job_config.use_legacy_sql = False

job = bq_client.query(query, job_config=job_config)
job.result()
