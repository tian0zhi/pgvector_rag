import psycopg2
from embedding_client import embed
from psycopg2.extras import Json

conn = psycopg2.connect(
    dbname="vector_db_test",
    user="postgres",
    password="password",
    host="localhost",
)
conn.autocommit = True


def insert_document(text: str, metadata: dict = None):
    vector = embed(text)

    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO documents (content, embedding, metadata)
            VALUES (%s, %s, %s)
        """, (text, vector, Json(metadata)))

    print("Inserted:", text[:40], "...")


if __name__ == "__main__":
    insert_document("太阳能逆变器用于将直流转交流...", {"type": "energy"})
