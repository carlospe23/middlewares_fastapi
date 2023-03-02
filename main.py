from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(CORSMiddleware(allow_origins=['*'], allow_methods=['*']))


@app.middleware('http')
async def verify_user_agent(request: Request, call_next):
    if request.headers['User-Agent'].find('Mobile') == -1:
        response = await call_next(request)
        return response
    else:
        return JSONResponse(content ={
            'message': 'error :(('
        }, status_code=401)


@app.get('/')
def main():
    return 'hola mundo'