from sqlalchemy import create_engine
from .settings import db_url

if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from models.models import Base
    from datetime import datetime, timedelta

    # create DB
    engine = create_engine(db_url)
    Base.metadata.create_all(bind=engine)
    session = Session(bind=engine)

    from app.models import Worktype_ORM, Workrecord_ORM

    demoWorkType1 = Worktype_ORM(id=1, name="Demo work type 1")
    demoWorkType2 = Worktype_ORM(id=2, name="Demo work type 2")
    session.add(demoWorkType1)
    session.add(demoWorkType2)
    session.commit()

    now = datetime.now()
    past = now - timedelta(seconds=30)
    demoWorkRecord1 = Workrecord_ORM(
        id=1, name="Demo work record 1", type_id=1, start=past, end=now
    )
    demoWorkRecord2 = Workrecord_ORM(
        id=2, name="Demo work record 2", type_id=2, start=past, end=now
    )
    demoWorkRecord3 = Workrecord_ORM(
        id=3, name="Demo work record 3", type_id=2, start=past, end=now
    )

    session.add(demoWorkRecord1)
    session.add(demoWorkRecord2)
    session.add(demoWorkRecord3)
    session.commit()

    print(f"created and populated the DB at {db_url}")
