from app.core.config import get_settings

settings=get_settings()
print("APP NAME: ",settings.app_name)
print("Groq API Key: ",settings.groq_api_key)