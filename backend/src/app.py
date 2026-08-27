from fastapi import FastAPI

app = FastAPI(
    title='MyLMS API',
    description='Sample FastAPI project to learn backend',
    version='1.0.0'
)

@app.get('/')
async def hello():
    return 'Hello World!'
