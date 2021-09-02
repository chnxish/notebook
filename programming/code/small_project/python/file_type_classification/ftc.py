import os

"""File Type Classification

Args：
    file_type, like XXXX, .XXXX, XX.XX
    file_name
    file_relative_path
"""
class Ftc:

    FILE_TYPES = [
        '.XXXX',  # The file name string starts wirh a period, like .gitconfig
        'XX.XX',  # Regular file name, like hello.cc
        'XXXX',   # The file name string does not contain a period, like LICENSE
    ]

    def __init__(self, file_name, realtive_path_name):
        self.file_name = file_name

        index_of_period = self.file_name.find('.')
        if index_of_period == 0:
            self.file_type = self.FILE_TYPES[0]
        elif index_of_period > 0:
            self.file_type = self.FILE_TYPES[1]
        else:
            self.file_type = self.FILE_TYPES[2]

        self.file_realtive_path = os.path.join(realtive_path_name, self.file_name)

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self.file_realtive_path)

    def __str__(self):
        return str(self.file_realtive_path)

    def member_function_names(self):
        return ['file_type', 'file_name', 'file_realtive_path']

    def to_list(self):
        return [self.file_type, self.file_name, self.file_realtive_path]
      

if __name__ == '__main__':
    ftc = Ftc('hello.cc', 'cpp')
    print(ftc)
    print(ftc.member_function_names())
    print(ftc.to_list())
