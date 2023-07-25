from dotenv import dotenv_values, find_dotenv

envs = dotenv_values("app\\settings\\.env")

try:
    db_url: str = envs["db_url"]  # type: ignore
except KeyError:
    db_url: str = "sqlite:///./timetracker.db"

jwt_secret_key: str = envs["jwt_secret_key"]  # type: ignore
jwt_secret_refresh_key: str = envs["jwt_secret_refresh_key"]  # type: ignore
algorithm: str = envs["algorithm"]  # type: ignore
access_token_expire_minutes = int(envs["access_token_expire_minutes"])  # type: ignore
refresh_token_expire_minutes = int(envs["refresh_token_expire_minutes"])  # type: ignore
