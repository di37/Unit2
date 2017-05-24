def get_page(link):
    try:
        import urllib.request
        page = urllib.request.urlopen(link).read().decode('utf-8')
        return page
    except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

##url, endpos = get_next_target(page)
##
##print (url)
#Now to print all links:
##def union(p,q):
##    for e in q:
##        if e not in p:
##            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


print(get_all_links(get_page('https://xkcd.com/353/')))
