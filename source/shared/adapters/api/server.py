import uvicorn
from fastapi import FastAPI, Request


app = FastAPI()


@app.get('/health')
def health():
    return {
        'status': 'ok'
    }


def server():
    uvicorn.run("source.shared.adapters.api.server:app", host="0.0.0.0", port=5000, log_level="info")


if __name__ == "__main__":
    main()