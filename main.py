from src.server import create_server
import uvicorn

if __name__ == "__main__":
    uvicorn.run(create_server(), host="0.0.0.0", port=8000)