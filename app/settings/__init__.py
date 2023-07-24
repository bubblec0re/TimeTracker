from dotenv import dotenv_values, find_dotenv

envs = dotenv_values("app\\settings\\.env")

try:
    db_url: str = envs["db_url"]  # type: ignore
except KeyError:
    db_url: str = "sqlite:///./timetracker.db"

jwt_secret_key: str = envs["jwt_secret_key"]  # type: ignore
jwt_secret_refresh_key: str = envs["jwt_secret_refresh_key"]  # type: ignore
