from models import Reading, db

try:
    db.create_tables([Reading])
except Exception as e:
    print(f"[FAIL] Setup failed.\nError: {str(e)}")
    exit(1)
