#include "21005004.h"
#include<iostream>
using namespace std;

int main(){
    string name, password;
    cin >> name;
    cin >> password;

    if(login(name, password)) cout << "Success!\n";
    cout << "Fail!\n";
}
