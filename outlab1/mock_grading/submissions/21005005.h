#include<map>
#include<string>
#include<iostream>
#include<utility>

using namespace std;

pair<string, string> passwords[] = {
    {"Tinsmorem","Iltil"},
    {"Ulyglet","Snurgrurg"},
    {"Lafibnom","Diamdioc"},
    {"Thenbovir","Oudrarrouz"},
    {"Gallnip","Haulmi"},
    {"Froolvess","Holdiz"},
    {"Smameknuc","Hinnyual"},
    {"Smedekmet","Traolbubrorg"},
    {"Cebbnec","Khishohi"},
    {"Klolyddwac","Maennius"},
    {"Blivylnas","Jolmuulmohr"},
    {"Glyhamdas","Drustiel"},
    {"Hillnar","Nanruddiarth"},
    {"Phieddlu","Zussial"},
    {"Fnamdyn","Laszo"},
    {"Fladnivith","Nathentoih"},
    {"Phelnyll","Phorughoelle"},
    {"Snallbam","Skilzeda"},
    {"Fensmyl","Vrakniarth"},
    {"Pibkecim","Jerpuldo"}
};

//Returns the password for a particular person
string get_password(string name){
	int i = 0;
	while(1){
		if(passwords[i].first == name) return passwords[i].second;
		i++;
	}
	return "";
}

bool login(string name, string password) {
    if(get_password(name) == password) return true;
    return false;
}
