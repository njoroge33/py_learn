import os
import re
from dotenv import load_dotenv

import mechanize
import requests
import bs4
from bs4 import BeautifulSoup
from tidylib import tidy_document

load_dotenv()


def slugify(name):
    slug = '_'.join(name.split(' ')).lower()
    regex = re.compile('[^a-zA-Z0-9_]')
    return regex.sub('', slug)


def add_file(dir_name, f_name, url=None, cont=[]):
    print('creating file: {}'.format(f_name))
    with open(f'{dir_name}/{f_name}.py', 'w') as f:
        print(f'adding quiz description to file: {f_name}')
        for l in cont:
            f.write(f"# {l.strip()} \n")
        if url:
            f.write(f"# for more info on this quiz, go to this url: {url}")


def create_folder(name):
    print(f'\n\ncreating folder: {name}')
    path = name
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
    #     print(f)

    br.select_form(nr=1)
    br.form['name'] = os.getenv('USERNAME')
    br.form['pass'] = os.getenv('PASSWORD')

    # Login
    br.submit()
    return br

def get_quiz_content(page):
    try:
        soup = BeautifulSoup(page, 'html.parser')
        q_desc_html = soup.find(class_='story')
        x_c = [tidy_document(str(x)) for x in q_desc_html.find_all('p')]

        x_s = BeautifulSoup(x_c[0][0], 'html.parser')
        q_desc = x_s.find('p').text.strip()
        return [x for x in q_desc.split('.') if x]
    except Exception as err:
        q_c = [x for x in q_desc_html.descendants][:2]
        if isinstance(q_c[1], bs4.element.Tag):
            q_c[1] = q_c[1].text
        else:
            q_c[1] = ''
        return q_c


def main():
    quiz_p = 'http://www.programmr.com/exercises?lang=python'
    q_c = requests.get(quiz_p)
    soup = BeautifulSoup(q_c.text, 'html.parser')
    li_w_c = soup.find_all(class_ = 'exercise')
    li_w_c.reverse()

    br = login()
    for idx, li in enumerate(li_w_c):
        try:
            n = slugify(li.find(class_ = 'top_node').text.strip())
            dir_name = f'{idx+1:02d}_{n}'
            ul_c = li.find('ul')
            files = ul_c.find_all('li')
            path = create_folder(dir_name)
            for file in files:
                try:
                    a = file.find('a')
                    f_name = slugify(a.text.strip())
                    url = f'http://www.programmr.com{a.get("href")}'
                    cont = br.open(url).read()
                    q_cont = get_quiz_content(cont)
                    add_file(path, f_name, url, cont=q_cont)
                except Exception as err:
                    print(err)
        except Exception as err:
            print(err)


if __name__ == '__main__':
    main()
