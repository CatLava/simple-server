import requests
import threading
import concurrent.futures
import time


thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        return requests.Session()

    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep ='', end='', flush=True)

# This gets passed a list
def download_all_sites(sites):
    # thread executor will determine when function is called for each thread
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executer:
        # Map function will call out when to execute
        executor.map(download_site, sites)


if __name__ == '__main__':

    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * 80

    print("Commence Download")
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print(f"Downloaded {len(sites)} sites in {duration} seconds")