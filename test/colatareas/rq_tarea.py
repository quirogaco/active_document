import requests

print("0")
def count_words_at_url(url):
    """Just an example function that's called async."""

    print("url:", url)
    resp = requests.get(url)
    print("11111111111111111")

    return len(resp.text.split())
