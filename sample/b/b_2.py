import rootdir
rootdir.root_dependency(__file__)

from a.a_1 import print_a_1

if __name__ == "__main__":
    print(rootdir.root_dir(__file__))
    print_a_1()