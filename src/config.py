from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "development"
    #DATABASE_URL: str = "postgresql://postgres:@127.0.0.1:5432/app"
    DATABASE_URL: str = "postgresql://postgres:postgres@127.0.0.1:5432/app1"
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str
    auth0_client_id: str
    auth0_client_secret: str
    #auth0_api_audience_frontend: str
    

    class Config:
        env_file = ".env"


settings = Settings()
