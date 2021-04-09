# Chapter06-4-3
# 파이썬 심화
# Asyncio
# 비동기 I/O Coroutine 작업

# aiohttp 사용 가능(Asyncio 지원)
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 시작 시간
start = timeit.default_timer()
urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com/', 'https://gmarket.co.kr/']


async def fetch(url, executor):
    # 쓰레드 이름 주목!
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)
    # urlopen은 동기 함수여서 스레드 생성해서 처리해줌
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name :', threading.current_thread().getName(), 'Done', url)
    # 반환
    return res.read()[0:5]


async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # asyncio.ensure_future :
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합
    rst = await asyncio.gather(*futures)  # 알아서 리스트 언팩킹해서 씀

    print()
    print('Result : ', rst)

if __name__ == '__main__':
    # 루프 생성 : 중앙 관리자
    loop = asyncio.get_event_loop()
    # 루프 대기 : 모든 제너레이터 함수가 끝날 때까지
    loop.run_until_complete(main())
    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Time : ', duration)
