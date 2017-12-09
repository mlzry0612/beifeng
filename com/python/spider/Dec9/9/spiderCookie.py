import urllib.parse as url_pa
import urllib.request as url_re
import urllib
import http.cookiejar

cookie_test = http.cookiejar.MozillaCookieJar(filename='cookie.txt')

handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_test)

opener = urllib.request.build_opener(handler)

#全局用的
urllib.request.install_opener(opener=opener)


urllib.request.urlopen('http://www.ibeifeng.com')
cookie_test.save(ignore_discard=True, ignore_expires=True)


filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
opener.open()