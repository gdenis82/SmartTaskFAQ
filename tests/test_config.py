
def test_config():
    from app.core.config import settings
    assert settings.PROJECT_NAME == "SmartTask FAQ"
