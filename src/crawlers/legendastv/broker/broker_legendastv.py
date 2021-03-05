COOKIES = ''


def get_first_response(url, host, session):

    global COOKIES

    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,gl;q=0.5",
        'Connection': "keep-alive",
        'Cookie': COOKIES,
        'Cache-Control': "no-cache",
        'Host': host,
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0"
    }

    first_response = session.get(url, headers=headers)

    cookie = [{'name': c.name, 'value': c.value} for c in session.cookies]

    for coo in cookie:
        COOKIES += coo['name']+'='+coo['value']+';'

    return first_response


def do_login(url_login, host, url_home_page, user, password, session):
    
    headers = {
        'Host': host,
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding': "gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'Origin': url_home_page,
        'Connection': "close",
        'Referer': url_home_page,
        'Upgrade-Insecure-Requests': "1",
        'Cookie': COOKIES,
    }

    querystring = {
        '_method':'POST',
        'data[User][username]':user,
        'data[User][password]':password,
        'data[lembrar]':'on',
    }

    res = session.post(url_login, headers=headers, data=querystring)

    return res


def search_term(url_do_search, host, url_home_page, term, session):
    
    headers = {
        'Host': host,
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding': "gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'Origin': url_home_page,
        'Connection': "close",
        'X-Requested-With': "XMLHttpRequest",
        'Referer': url_home_page,
        'Upgrade-Insecure-Requests': "1",
        'Cookie': COOKIES,
    }

    res = session.get(url_do_search+term+'/1', headers=headers)

    return res


def get_next_pages(url_next, host, term, session, page_number):

    headers = {
        'Host': host,
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
        'X-Requested-With': "XMLHttpRequest",
        'Referer': url_next+term,
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        'Cookie': COOKIES,
        'Connection': "close",
    }

    return session.get(url_next+term+"/1/-/"+str(page_number)+"/-", headers=headers)
