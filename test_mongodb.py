from backend.database.mongodb import client

try:
    client.admin.command("ping")
    print("✅ Connected to MongoDB Atlas!")

except Exception as e:
    print("❌ Connection Failed")
    print(e)