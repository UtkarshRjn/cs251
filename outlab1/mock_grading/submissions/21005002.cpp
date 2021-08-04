#include "21005002.h"
#include<iostream>
#include<vector>

using namespace std;

int *a = NULL;

int main(){
    string name, password;

	cout << *a << endl;

    cin >> name;
    cin >> password;


    if(login(name, password)) cout << "Success!\n";
    cout << "Fail!\n";
}
