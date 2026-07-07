import uvicorn

from yorha.api.app import app
from yorha.config import settings


def main():
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
    )


if __name__ == "__main__":
    main()