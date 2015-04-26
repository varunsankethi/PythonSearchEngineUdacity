def get_page():
    import urllib.request
    url = 'http://www.google.com/'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    return text

def get_all_links():
    page = get_page()
    start_link = page.find ('<a href =')
    start_quote = page.find ('"', start_link)
    end_quote = page.find('"' , start_quote+1)
    #url = page[start_quote+1:end_quote]
    #print (url)

    

if __name__ == '__main__':
    get_all_links()

    
                       
