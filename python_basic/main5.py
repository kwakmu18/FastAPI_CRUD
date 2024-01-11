# 비동기. async와 await. 코루틴.
# 동기 : 순차, I/O 발생 시 완료까지 대기
# 비동기 : I/O가 완료되면 그것의 결과를 받아 작업 진행. 웹 API에는 비동기 코드 사용

from fastapi import FastAPI

async def get_burgers(cnt:int): # 비동기 함수를 선언하려면 async 키워드 추가
    return cnt

app = FastAPI()

@app.get("/burgers")
async def read_burgers():
    burgers = await get_burgers(2) # await 키워드를 사용하여 해당 함수가 종료될 때까지 대기, 그 동안 다른 작업 수행
    return burgers

# await 키워드는 async(비동기)로 선언된 함수 내부에서만 사용 가능