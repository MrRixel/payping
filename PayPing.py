import requests
import re
from lxml import html

class payping:
    def __init__(self, username):
        check = requests.get("https://www.payping.ir/{}".format(username))
        if check.status_code == 200: self.username = username
        else: raise Exception("Username is wrong!")

    def PaymentRequest(self, amount, name, desc):
        get = requests.get("https://www.payping.ir/{}".format(self.username),
        headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        })
        lxml = html.fromstring(get.content)
        for cookie in get.cookies: __RequestVerificationToken = cookie.value
        RequestVerificationToken = lxml.xpath('//*[@id="formDiv"]/form/input[1]')[0].value
        data = '__RequestVerificationToken={}&UserName={}&IsPreDefiened=False&Amount={}&PayerName={}&Description={}'.format(RequestVerificationToken, self.username, amount, name, desc)
        post = requests.post("https://www.payping.ir/{}".format(self.username), data=data,
        headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Referer': 'https://www.payping.ir/{}'.format(self.username),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '__RequestVerificationToken={}'.format(__RequestVerificationToken)
        })
        return post.url

    def PaymentVerify(self, url):
        get = requests.get(url)
        return ("این درخواست پرداخت شده است" in get.text)
