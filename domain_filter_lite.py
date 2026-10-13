# Lite Corporate Domain Filter
# Full FastAPI Live Scraper + AI Scoring + n8n Workflow JSON: https://kritikos12.gumroad.com/l/qjimps/LAUNCH29

FREE_PROVIDERS = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com", "aol.com", "protonmail.com"}

def is_corporate_email(email: str) -> dict:
    domain = email.strip().split("@")[-1].lower()
    return {"email": email, "domain": domain, "is_corporate": domain not in FREE_PROVIDERS}

if __name__ == "__main__":
    print(is_corporate_email("cto@enterprise.io"))