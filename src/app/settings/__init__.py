import os
from app.settings.dev import DevSettings
from app.settings.prod import ProdSettings

settings_module = os.environ.get("SETTINGS", "prod")

settings_classes = {
    "dev": DevSettings,
    "prod": ProdSettings,
}

if settings_module not in settings_classes:
    expected = ", ".join(settings_classes)
    raise ValueError(
        f"Wrong SETTINGS env value! Expected {expected}, got {settings_module}."
    )

settings = settings_classes[settings_module]()
