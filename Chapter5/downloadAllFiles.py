import os
from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

download_directory = '/Users/anurag.sh/workspace/SQLDump/temp'
base_url = 'https://www.python.org/'


def get_absolute_url(base_url, src):
    if src.startswith('http://www.'):
        url = 'http://{}'.format(src[11:])
    elif src.startswith('http://'):
        url = src
    elif src.startswith('www.'):
        url = src[4:]
        url = 'http://{}'.format(src)
    else:
        url = '{}/{}'.format(base_url, src)
    if base_url not in url:
        return None
    return url


def is_file_inside_base_directory(child_path, parent_path):
    # Smooth out relative path names, note: if you are concerned about symbolic links,
    # you should use os.path.realpath too
    parent_path = os.path.abspath(parent_path)
    child_path = os.path.abspath(child_path)

    # Compare the common path of the parent and child path with the common path of just the parent path.
    # Using the commonpath method on just the parent path will regularise
    # the path name in the same way as the comparison that deals with both paths,
    # removing any trailing path separator
    return os.path.commonpath([parent_path]) == os.path.commonpath([parent_path, child_path])


def get_download_path(base_url, absolute_url):
    path = absolute_url.replace('www.', '')
    path = path.replace(base_url, '')
    path = download_directory + path
    file_path = os.path.dirname(path)

    print("File path -> ", file_path)
    if is_file_inside_base_directory(file_path, download_directory):
        print("Invalid path, trying to harm our laptop")
        exit(1)

    if not os.path.exists(file_path):
        print("Creating file path -> ", file_path)
        os.makedirs(file_path)

    return path


def main():
    html = urlopen(base_url)
    bs = BeautifulSoup(html, 'html.parser')
    download_list = bs.find_all(src=True)

    for download in download_list:
        print(download['src'], type(download['src']))
        file_url = get_absolute_url(base_url, download['src'])
        if file_url is not None:
            print(file_url)
            try:
                urlretrieve(file_url, get_download_path(base_url, file_url))
            except HTTPError as ex:
                print('Could not download {}, got error'.format(file_url, ex))
        else:
            print("Ignoring file -> ", download['src'])


if __name__ == '__main__':
    main()
