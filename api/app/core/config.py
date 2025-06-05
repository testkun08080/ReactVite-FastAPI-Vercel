from pydantic import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Default Project Name"
    project_description: str = "Default Project Description"
    version: str = "0.1.0"
    root_path: str = "/api"

    class Config:
        env_file = "api/.env"
