import psycopg2

def init_pgvector():
    conn = psycopg2.connect(
        dbname="vector_db_test",
        user="postgres",
        password="password",
        host="localhost",
        port=5432
    )
    conn.autocommit = True

    cur = conn.cursor()

    # 1. Enable pgvector
    cur.execute("""
        CREATE EXTENSION IF NOT EXISTS vector;
    """)

    # 2. Create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id bigserial PRIMARY KEY,
            content text NOT NULL,
            embedding vector(1024),
            metadata jsonb
        );
    """)

    # 3. Create HNSW index
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_documents_embedding
        ON documents
        USING hnsw (embedding vector_cosine_ops)
        WITH (m = 16, ef_construction = 64);
    """)

    print("PostgreSQL + pgvector 初始化完成！")

    cur.close()
    conn.close()


if __name__ == "__main__":
    init_pgvector()
