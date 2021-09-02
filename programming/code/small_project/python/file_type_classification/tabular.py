# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data/26937531#26937531

from prettytable import PrettyTable

# Printing Lists as Tabular Data
def tabular(mylist):
    first_element = mylist[0]

    if hasattr(first_element, 'member_function_names') and hasattr(first_element, 'to_list'):
        mfn = first_element.member_function_names()
        t = PrettyTable(mfn)
        for x in mylist:
            t.add_row(x.to_list())
        print(t)
    else:
        print('Error: The list data does not support the tabular function')

if __name__ == '__main__':
    from ftc import Ftc

    f1 = Ftc('hello.cc', '')
    f2 = Ftc('.gitconfig', '')
    f3 = Ftc('LICENSE', '')

    l = list()
    l.append(f1)
    l.append(f2)
    l.append(f3)

    tabular(l)
