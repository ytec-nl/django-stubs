from django.apps import AppConfig as AppConfig
from typing import Any

class GISConfig(AppConfig):
    name: str = ...
    verbose_name: Any = ...
    def ready(self) -> None: ...
