import requests
from bs4 import BeautifulSoup
from concurrent.futures import as_completed
import re
from concurrent.futures import ThreadPoolExecutor as Pool

response = requests.get("http://www.beautyleg.com/sample.php?no=1538")
print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
alist = soup.find_all('img')
images = []
for a in alist:
    src = a.get('src')
    if re.match('http', src):
        images.append(src)
    else:
        fullString = "http://www.beautyleg.com/" + src
        images.append(fullString)


def write_file(url):
    print(url)
    fileName = "./img/" + url.split("/")[-1]
    content = requests.get(url, timeout=5)
    with open(fileName, "wb") as write:
        write.write(content.content)
    return fileName


with Pool(max_workers=20, thread_name_prefix="download-") as executor:
    future_tasks = [executor.submit(write_file, pathUrl) for pathUrl in images]

    for f in future_tasks:
        if f.running():
            print('%s is running' % str(f))

    for f in as_completed(future_tasks):
        try:
            ret = f.done()
            if ret:
                f_ret = f.result()
                print('Thead %s,  result is %s' % (str(f), f_ret))
        except Exception as e:
            f.cancel()
            print(str(e))
