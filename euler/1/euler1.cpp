#include <iostream>

using namespace std;

void euler1(){
	int result = 0;

	for (int i; i < 1000;i++){
		if (i % 3 == 0 || i % 5 == 0){
			result += i;
		}
	}

	std::cout << result << endl;
}

int main()
{

    euler1();
    return 0;
}
