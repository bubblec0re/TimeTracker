from os.path import exists
from dotenv import dotenv_values
from .db_init import populate_db


envs = dotenv_values("app/.env", verbose=True)

try:
    db_url: str = envs["db_url"]  # type: ignore
except KeyError:
    db_url: str = "sqlite:///./timetracker.db"
    populate_db(db_url)

if db_url.startswith('sqlite:///') and not exists(db_url[10:]):
    populate_db(db_url)

jwt_secret_key: str = envs["jwt_secret_key"]  # type: ignore
jwt_secret_refresh_key: str = envs["jwt_secret_refresh_key"]  # type: ignore
algorithm: str = envs["algorithm"]  # type: ignore
access_token_expire_minutes = int(envs["access_token_expire_minutes"])  # type: ignore
refresh_token_expire_minutes = int(envs["refresh_token_expire_minutes"])  # type: ignore
