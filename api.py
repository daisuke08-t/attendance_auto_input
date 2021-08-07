from main import Main
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()
main = Main()

@app.get('/')
async def api_main():
    main.main()
    return {"text": "Success!!"}