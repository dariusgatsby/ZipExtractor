import zipfile

def extractor(folder, extract_location):
    with zipfile.ZipFile(folder, 'r') as zip_ref:
        zip_ref.extractall(extract_location)

if __name__ == '__main__':
    extractor('Archive.zip', '/Users/macadmin/PycharmProjects/ZipExtractor')
