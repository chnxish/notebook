#include <iostream>

#define PRINT_NAME(x) \
    std::cout << "Name: " << x << std::endl;

int main(int argc, char *argv[]) {
    char USERNAME1[] = "abcdefghijklmn"
                       "opqrstuvwxyz";

    std::cout << "Hello, Xish. I'm name is "
        << USERNAME1 << std::endl;

    char USERNAME2[] = "abcdefghijklmn\
                        opqrstuvwxyz";

    PRINT_NAME(USERNAME1);
    PRINT_NAME(USERNAME2);

    return 0;
}
