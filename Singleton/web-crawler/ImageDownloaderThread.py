import httplib2
import os
import threading
import urllib
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup
from Singleton import Singleton

class ImageDownloaderThread(threading.Thread):
    """A thread for downloading images in parallel."""

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print 'Starting thread ', self.name
        self.download_images(self.name)
        print 'Finished thread ', self.name

    def download_images(self, thread_name):
        singleton = Singleton()
        # While we have pages where we have not download images
        while singleton.to_visit:
            url = singleton.to_visit.pop()
            http = httplib2.Http()
            print thread_name, 'Starting downloading images from', url
            try:
                status, response = http.request(url)
            except Exception as e:
                print(e)
                continue
            bs = BeautifulSoup(response)
            # Find all <img> tags
            images = BeautifulSoup.findAll(bs, 'img')
            for image in images:
                # Get image source url which can be absolute or relative
                src = image.get('src')
                # Construct a full url. If the image url is relative,
                # it will be prepended with webpage domain.
                # If the image url is absolute, it will remain as is
                src = urljoin(url, src)
                # Get a base name, for example 'image.png' to name file locally
                basename = os.path.basename(src)
                if src not in singleton.downloaded:
                    singleton.downloaded.add(src)
                    print 'Downloading', src
                    # Download image to local filesystem
                    urllib.urlretrieve(src, os.path.join('images', basename))
            print thread_name, 'finished downloading images from', url