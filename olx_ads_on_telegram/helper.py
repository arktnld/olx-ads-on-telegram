# Build info msg to send to telegram
def build_msg(list):
    price, link = list
    msg = f'*{price}* \n\n[link]({link})'
    # print(msg)
    return msg

# Filter urls by pattern
def filter_found_urls(urls, keys):
    for key in keys:
        urls = [url for url in urls if key not in url]
    return urls

