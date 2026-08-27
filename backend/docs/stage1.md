# Lesson 1: Setup

Loyihani yaratib olish va dastlabki bosqich sozlashlari

1. papka yaratish ✅
`mkdir <dirname>`

2. ichiga kirish ✅
`cd <dirname>`

3. .venv init qilish ✅
`python -m venv .venv`

4. .venvni ishga tushirish ✅
`source .venv/bin/activate`

5. kerakli kutubxonalarni o'rnatish ✅
`pip install fastapi uvicorn[standard]`

6. freeze orqali kutubxonalarni ro'yxatini saqlash ✅
`pip freeze > requirements.txt`

7. main.py ni sozlash ✅
main.py
```python
from src.app import app

if __name__ == '__name__':
    import uvicorn
    uvicorn.run(app, port=8000)
```

8. src/app.py ni sozlash ✅
src/app.py
```python
from fastapi import FastAPI

app = FastAPI(
    title='My API',
    description='Sample FastAPI project to learn backend',
    version='1.0.0'
)

@app.get('/')
async def hello():
    return 'Hello World!'

```

9. test.http orqali API ni ishlashini tekshirib ko'rish ✅
test/api/test.http
```http
GET http://localhost:8000/
```
