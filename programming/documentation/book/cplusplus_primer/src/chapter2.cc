#include <iostream>

int main(int argc, char *argv[]) {
    // C-style type conversion is not recommended
    const int A_POSITIVE_NUMBER = 1.2;
    const int A_NEGATIVE_NUMBER = -1.2;

    std::cout << A_POSITIVE_NUMBER << " " << A_NEGATIVE_NUMBER << std::endl;

    return 0;
}
