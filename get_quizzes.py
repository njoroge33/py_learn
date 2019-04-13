import os
import re
from http import cookiejar
from dotenv import load_dotenv

import mechanize
import requests
from bs4 import BeautifulSoup
from tidylib import tidy_document

load_dotenv()


def slugify(name):
    slug = '_'.join(name.split(' ')).lower()
    regex = re.compile('[^a-zA-Z0-9_]')
    return regex.sub('', slug)


def add_file(dir_name, f_name, cont=[]):
    print('creating file: {}'.format(f_name))
    with open('{}/{}.py'.format(dir_name, f_name), 'w') as f:
        print('adding quiz description to file: {}'.format(f_name))
        for l in cont:
            f.write("# {} \n".format(l.strip()))


def create_folder(name):
    print('\n\ncreating folder: {}'.format(name))
    path = '{}'.format(name)
    os.mkdir(path)
    add_file(path, '__init__')
    return path


def login():
    br = mechanize.Browser()

    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]

    br.open('http://www.programmr.com/user/sign-in?op=login')

    # # View available forms
    # for f in br.forms():
    #     print('-----------------------------------')
    #     print(f)

    br.select_form(nr=1)

    # User credentials
    br.form['name'] = os.getenv('USERNAME')
    br.form['pass'] = os.getenv('PASSWORD')

    # Login
    br.submit()
    return br

def get_quiz_content(page):
    soup = BeautifulSoup(page, 'html.parser')
    q_desc_html = soup.find(class_='story')
    x = [tidy_document(str(x)) for x in q_desc_html.find_all('p')]

    x_s = BeautifulSoup(x[0][0], 'html.parser')
    q_desc = x_s.find('p').text.strip()
    return [x for x in q_desc.split('.') if x]


def main():
    quiz_p = 'http://www.programmr.com/exercises?lang=python'
    q_c = requests.get(quiz_p)
    soup = BeautifulSoup(q_c.text, 'html.parser')
    li_w_c = soup.find_all(class_ = 'exercise')
    br = login()
    for li in li_w_c:
        try:
            dir_name = slugify(li.find(class_ = 'top_node').text.strip())
            ul_c = li.find('ul')
            files = ul_c.find_all('li')
            path = create_folder(dir_name)
            for file in files:
                a = file.find('a')
                f_name = slugify(a.text.strip())
                url = 'http://www.programmr.com/{}'.format(a.get('href'))
                cont = br.open(url).read()
                q_cont = get_quiz_content(cont)
                add_file(path, f_name, cont=q_cont)
        except Exception as err:
            print(err)


if __name__ == '__main__':
    main()
