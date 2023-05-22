#1

class InvalidUrlError(Exception):
    def __init__(self,url):
        self.url = url
def fetch_data_from_url(url):
        if url != "https://www.youtube.com/watch?v=Gs_uBw0CJNk":
            raise InvalidUrlError("Invalid URL:" + url)
        elif "/" not in url:
            raise InvalidUrlError("Something was typed uncorrectly (")
        else:
            print("URL was typed correctly")

try:
    fetch_data_from_url("https://www.youtube.com/watch?v=Gs_uBw0CJNK")
except InvalidUrlError as e:
    print("Error:" , e)

#2

