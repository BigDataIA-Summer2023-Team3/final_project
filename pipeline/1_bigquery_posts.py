from google.cloud import bigquery

# Set up BigQuery client with explicit project ID
bq_client = bigquery.Client(project='project id')

# Set up query to get the top 3 most repeated tags
top_tags_query = """
    SELECT tags, COUNT(*) as count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    GROUP BY tags
    ORDER BY count DESC
    LIMIT 3
"""

# Run query to get the top 3 most repeated tags
top_tags_job = bq_client.query(top_tags_query)
top_tags_result = top_tags_job.result()
top_tags = [row[0] for row in top_tags_result]

# Set up query to insert data into the table
query = f"""
    INSERT INTO StackAI.posts_cleaned (question_id, question_title, question_body, question_tags, question_score, question_view_count, answer_count, comment_count, question_creation_date, accepted_answer, accepted_answer_creation_date, accepted_answer_owner_display_name, owner_reputation, owner_badge, accepted_answer_score, accepted_answer_view_count)
    WITH posts_answers AS (
        SELECT
            p1.id AS question_id,
            COALESCE(p1.title, 'N/A') AS question_title,
            COALESCE(p1.body, 'N/A') AS question_body,
            COALESCE(p1.tags, 'N/A') AS question_tags,
            COALESCE(p1.score, 0) AS question_score,
            COALESCE(SAFE_CAST(p1.view_count AS INT64), 0) AS question_view_count,
            COALESCE(p1.answer_count, 0) AS answer_count,
            COALESCE(p1.comment_count, 0) AS comment_count,
            COALESCE(FORMAT_DATE('%Y-%m-%d', DATE(p1.creation_date)), 'N/A') AS question_creation_date,
            COALESCE(p2.body, 'N/A') AS accepted_answer,
            COALESCE(FORMAT_DATE('%Y-%m-%d', DATE(p2.creation_date)), 'N/A') AS accepted_answer_creation_date,
            COALESCE(u.display_name, 'N/A') AS accepted_answer_owner_display_name,
            COALESCE(u.reputation, 0) AS owner_reputation,
            COALESCE(b.name, 'N/A') AS owner_badge,
            COALESCE(p2.score, 0) AS accepted_answer_score,
            COALESCE(SAFE_CAST(p2.view_count AS INT64), 0) AS accepted_answer_view_count
        FROM
            `bigquery-public-data.stackoverflow.posts_questions` p1
        LEFT JOIN
            `bigquery-public-data.stackoverflow.posts_answers` p2
        ON
            p1.accepted_answer_id = p2.id
        LEFT JOIN
            `bigquery-public-data.stackoverflow.users` u
        ON
            p2.owner_user_id = u.id
        LEFT JOIN
            `bigquery-public-data.stackoverflow.badges` b
        ON
            p2.id = b.id
        WHERE
            p1.tags IN ('{top_tags[0]}', '{top_tags[1]}', '{top_tags[2]}')
    )
    SELECT *
    FROM posts_answers limit 500
"""

# Run query to insert data into the table
job_config = bigquery.QueryJobConfig()
job_config.use_legacy_sql = False

job = bq_client.query(query, job_config=job_config)
job.result()
