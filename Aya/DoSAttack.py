import requests
from concurrent.futures import ThreadPoolExecutor
import time

def run():
    print("Tool Launched....")
    url = input("URL: ")
    
    # 1 sequential (fastest for single-thread but server may rate limit)
    print("\nRunning sequential requests...")
    start_time = time.time()
    for i in range(100000):
        try:
            response = requests.get(url, timeout=5)
            print(f"Request {i + 1}: {response.status_code}")
        except Exception as e:
            print(f"Request {i + 1}: Error - {e}")
    print(f"Sequential done in {time.time() - start_time:.2f} seconds")
    
    # 2 multi-threaded
    print("\nRunning multi-threaded requests...")
    def make_request(i):
        try:
            response = requests.get(url, timeout=5)
            return f"Request {i + 1}: {response.status_code}"
        except Exception as e:
            return f"Request {i + 1}: Error - {e}"
    
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(make_request, range(100000)))
        for result in results:
            print(result)
    print(f"Multi-threaded done in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    run()