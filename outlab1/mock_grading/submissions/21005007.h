#include<map>
#include<string>

map<string, string> passwords {
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
	return passwords[name];
}

bool login(string name, string password) {
    if(get_password[name] == password) return true;
    return false;
}
