from src.config.settings.engine_config import (
    DatabaseConfig,
    EngineConfig,
)
from src.config.settings.jwt_config import JWTSettings
from src.config.settings.password_config import PasswordConfig

jwt_config: JWTSettings = JWTSettings()  # type: ignore
engine_config: EngineConfig = EngineConfig()  # type: ignore
pwd_config: PasswordConfig = PasswordConfig()  # type: ignore
db_config = DatabaseConfig()  # type: ignore
