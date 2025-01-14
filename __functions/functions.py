import requests
from bs4 import BeautifulSoup
import urllib3
import sys
import time
import random
from urllib.parse import urlparse
import json, re
from __constants.constants import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def random_col():
    listt = ['green', 'yellow', 'white']
    return random.choice(listt)

def learnviral(page):
    links_ls = []
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
    }

    r = requests.get(LEARNVIR + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    first = soup.find_all('div', class_ = 'content-box')
    soup1 = BeautifulSoup(str(first[1]), 'html.parser')
    title_all = soup1.find_all('h3', class_ = 'entry-title')
    links = soup1.find_all('div', class_ = 'link-holder')

    for index, lk in enumerate(links):
        title = title_all[index].text
        links_ls.append(title + '|||' + lk.a['href'])
    return links_ls

def real_disc(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(REALDISC + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    # udd = soup.find_all('div', attrs = {'style': 'margin-top:-274px;z-index:9;position: absolute; left: 0; margin-left: 15px; color: #fff; background: rgba(0,0,0,0.5); padding: 2px 4px; font-weight: 700;'})
    # content = soup.find_all('div', class_ = 'white-block-content', attrs = {'style': ';background-color: #333333;height: 160px;   overflow: hidden;'})
    content = soup.find_all("a", href=re.compile("offer"))
    # print(len(content))
    # exit()

    for index, i in enumerate(content):
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()

        if i.has_attr('href'):
            url2 = i['href']

            r2 = requests.get(url=f"https://www.real.discount{url2}", headers=head, verify=False)
            soup1 = BeautifulSoup(r2.content, 'html.parser')
            title1 = soup1.find('title').text.replace('[100% Off] ', '')
            title = title1.replace('  Free  Course Coupon', '')
            links_ls.append(title + '|||' + soup1.findAll("a", href=re.compile("udemy.com"))[0]['href'])
    return links_ls

    for index, i in enumerate(content):
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()
        # print(udd[index].text)
        if udd[index].text.replace('\n', '') == 'Udemy':
            url2 = i.a['href']

            r2 = requests.get(url=url2, headers=head, verify=False)
            soup1 = BeautifulSoup(r2.content, 'html.parser')
            title = soup1.find('title').text.replace(' Udemy Coupon - Real Discount', '')
            links_ls.append(title + '|||' + soup1.find('div', class_ = 'col-sm-6 col-xs-6 letshover').a['href'])
    return links_ls

def udemy_freebies(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(UDEMYFREEBIES + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('div', 'theme-block')
    for index, items in enumerate(all):
        title = items.img['title']
        url2 = items.a['href']
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()

        r2 = requests.get(url2, headers=head, verify=False)
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        try:
            url3 = soup1.find('a', class_ = 'button-icon')['href']
            link = requests.get(url3, verify=False).url
            links_ls.append(title + '|||' + link)
        except:
            pass
    return links_ls

def udemy_coupons_me(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(UDEMYCOUPONS + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('div', 'td_module_1 td_module_wrap td-animation-stack')
    if page == 1:
        all = all[2:]
    for index, items in enumerate(all):
        title = items.a['title']
        url2 = items.a['href']
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()
        r2 = requests.get(url2, headers=head, verify=False)
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        try:
            ll = soup1.find('span', class_ = 'td_text_highlight_marker_green td_text_highlight_marker').a['href']
            links_ls.append(title + '|||' + ll)
        except:
            ll = ''
    return links_ls

def discudemy(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(DISCUD + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('section', 'card')
    for index, items in enumerate(all):
        try:
            title = items.a.text
            url2 = items.a['href']
        except:
            title = ''
            url2 = ''
        if url2 != '':
            r2 = requests.get(url2, headers=head, verify=False)
            soup1 = BeautifulSoup(r2.content, 'html.parser')
            next = soup1.find('div', 'ui center aligned basic segment')
            try:
                url3 = next.a['href']
                r3 = requests.get(url3, headers=head, verify=False)
                sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
                sys.stdout.flush()
                soup3 = BeautifulSoup(r3.content, 'html.parser')
                links_ls.append(title + '|||' + soup3.find('div', 'ui segment').a['href'])
            except:
                title = ''
                url2 = ''
    return links_ls

########### NEW WEBSITES #############
def tricksinfo(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(TRICKSINF + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('a', class_ = 're_track_btn')
    for index, items in enumerate(all):
        title = items['aria-label']
        url2 = items['href']
        r2 = requests.get(url2, headers=head, verify=False)
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        link = soup1.find('div', 'wp-block-button').a['href']
        links_ls.append(title + '|||' + link)
    return links_ls

def onlinecourses(page):
    links_ls = []

    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(ONLINECOURSES+ str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('a', attrs={"rel": "bookmark", "title": True})
    for index, items in enumerate(all):
        try:
            title = items.text
            url2 = items['href']
            r2 = requests.get(url2, headers=head, verify=False)
            sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
            sys.stdout.flush()
            soup1 = BeautifulSoup(r2.content, 'html.parser')
            link = soup1.find('div', 'link-holder').a['href']
            links_ls.append(title + '|||' + link)
        except:
            title = ''
            url2 = ''
    return links_ls

def coursevania(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    course_vania = "https://coursevania.com/courses/"
    r =  requests.get(course_vania, headers=head)
    soup = BeautifulSoup(r.content, 'html.parser')
    # value = soup.xpath('/html/head/script[23]')
    # pattern = re.compile(r"var stm_lms_nonces = '(.*?)';$", re.MULTILINE | re.DOTALL)
    # script = soup.find("script", text=pattern)
    s = soup.findAll('script')
    # pattern = re.compile(r'var stm_lms_nonces = ({.*})', re.MULTILINE | re.DOTALL)
    for i in range(len(s)):
        try:
            data = json.loads(re.search(r"var stm_lms_nonces = ({.*})", s[i].string).group(1))
        except:
            pass
    # print(data["load_content"])


    r = requests.get(COURSEVANIA+data['load_content'], headers=head, verify=False)
    js = r.json()
    soup = BeautifulSoup(js['content'], 'html.parser')
    #all = soup.find_all('a', class_ = 'heading_font')
    all = soup.find_all('a', attrs={"class": "heading_font", "title": True})
    for index, items in enumerate(all):
        title = items['title']
        url2 = items['href']
        r2 = requests.get(url2, headers=head, verify=False)
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        try:
            link = soup1.find('div', 'stm-lms-buy-buttons').a['href']
            if (link is not None) and (title is not None): 
                links_ls.append(title + '|||' + link)
        except:
            pass
        #    title = ''
        #    url2 = ''
    return links_ls

def freewebcart(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(WEBCART + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('h2', class_ = 're_track_btn')
    for index, items in enumerate(all):
        title = items.text
        url2 = items.a['href']
        r2 = requests.get(url2, headers=head, verify=False)
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        try:
            link = soup1.find('a', class_ = 're_track_btn btn_offer_block')['href']
            links_ls.append(title + '|||' + link)
        except:
            pass
    return links_ls

def couponscorpion(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(COUPONSCORPION + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('h3.a')
    for index, items in enumerate(all):
        title = items.text
        url2 = items.a['href']
        r2 = requests.get(url2, headers=head, verify=False)
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        link = soup1.find('a', class_ = 'btn btn-default btn-lg')['href']
        links_ls.append(title + '|||' + link)
    return links_ls

def course_mania(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Referer': 'https://coursemania.xyz/',
        'Origin': 'https://coursemania.xyz',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(COURSEMANIA, headers=head, verify=False)
    js = r.json()
    for items in js:
        title = items['courseName']
        link = items['url']
        links_ls.append(title + '|||' + link)
    return links_ls

def helpcovid(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(HELPCOV, headers=head, verify=False)
    js = r.json()
    for items in js['courses']:
        title = items['title']
        link = items['url']
        links_ls.append(title + '|||' + link)
    return links_ls

def jojocoupons(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(JOJOCP + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('h2', class_ = 'font130 mt0 mb10 mobfont110 lineheight20')
    for index, items in enumerate(all):
        title = items.text
        url2 = items.a['href']
        r2 = requests.get(url2, headers=head, verify=False)
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        link = soup1.find('div', class_ = 'rh-post-wrapper')
        for tag in soup1.find_all('a'):
            try:
                if urlparse(tag['href']).netloc == 'www.udemy.com' or urlparse(tag['href']).netloc == 'udemy.com':
                    # print(tag['href'])
                    links_ls.append(title + '|||' + tag['href'])
                    break
            except:
                r = ''
    return links_ls

def onlinetutorials(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(ONLINETUT + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('h3', class_ = 'entry-title')
    for index, items in enumerate(all):
        title = items.text
        url2 = items.a['href']
        r2 = requests.get(url2, headers=head, verify=False)
        sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
        sys.stdout.flush()
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        link = soup1.find('div', class_ = 'link-holder').a['href']
        links_ls.append(title + '|||' + link)
    return links_ls

# print(onlinetutorials(1))
