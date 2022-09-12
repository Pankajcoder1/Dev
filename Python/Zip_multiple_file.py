from zipfile import ZipFile

def make_zip():
    zip_file = ZipFile('Sample.zip', 'w')
    add_to_zip(zip_file, 'Cf.cpp')
    add_to_zip(zip_file, 'hello.sh')
    add_to_zip(zip_file, 'LeetCode.cpp')
    zip_file.close()

def add_to_zip(zip_object, file_name):
    zip_object.write(file_name)


if __name__ == '__main__':
    make_zip()