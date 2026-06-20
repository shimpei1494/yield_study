from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


class DBSession:
    def close(self):
        print("close db session")


def get_db():
    db = DBSession()

    try:
        yield db
    finally:
        db.close()


@app.get("/items")
def list_items(db: Annotated[DBSession, Depends(get_db)]):
    return {"message": "use db here"}
