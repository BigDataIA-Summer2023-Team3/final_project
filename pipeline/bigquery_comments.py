#to be run only after posts table has been created
#inserts values into comments table (already created by terraform)
from google.cloud import bigquery

def insert_data_into_comments_table(bq_client):
    query = """
        INSERT INTO StackAI.comments_cleaned (post_id, text, creation_date, score)
        SELECT
            c.post_id,
            c.text,
            c.creation_date,
            c.score
        FROM
            `bigquery-public-data.stackoverflow.comments` c
        JOIN
            `stackai-394819.StackAI.posts_cleaned` p
        ON 
            c.post_id = p.question_id
    """
    job_config = bigquery.QueryJobConfig()
    job_config.use_legacy_sql = False
    
    job = bq_client.query(query, job_config=job_config)
    job.result()

if __name__ == "__main__":
    bq_client = bigquery.Client(project='stackai-394819')
    insert_data_into_comments_table(bq_client)
