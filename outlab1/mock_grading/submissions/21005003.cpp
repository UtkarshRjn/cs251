#include "21005003.h"
#include<iostream>
using namespace std;

int main(){
    string name, password;
	while(1);
    cin >> name;
    cin >> password;

    if(login(name, password)) cout << "Success!\n";
    cout << "Fail!\n";
}
