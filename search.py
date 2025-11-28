import psycopg2
from embedding_client import embed


conn = psycopg2.connect(
    dbname="vector_db_test",
    user="postgres",
    password="password",
    host="localhost",
)



def search_similar(query: str, top_k: int = 5):
    qvec = embed(query)

    with conn.cursor() as cur:
        cur.execute("""
            SELECT content, 1 - (embedding <=> %s::vector) AS similarity
            FROM documents
            ORDER BY embedding <-> %s::vector
            LIMIT %s;
        """, (qvec, qvec, top_k))

        results = cur.fetchall()

    return [{"content": r[0], "similarity": float(r[1])} for r in results]

if __name__ == "__main__":
    print(search_similar("逆变器的作用？"))
