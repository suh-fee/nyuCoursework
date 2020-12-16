//
//  rec02.cpp
//  Labs 2-?
//
//  Created by Safiullah Hasani on 9/14/18.
//  Copyright © 2018 Safiullah Hasani. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;



struct Hydrocarbon{
    vector<string> name;
    int carbons;
    int hydrogens;
};

// prototypes
void reader(vector<Hydrocarbon>& vect, ifstream& myfile);
void file_opener(ifstream& myfile);
void insertion_sort(vector<Hydrocarbon>&);


int main() {
    ifstream myfile;
    vector<Hydrocarbon> hydro;
    
    file_opener(myfile);
    reader(hydro, myfile);
    insertion_sort(hydro);
    for(const Hydrocarbon& i : hydro){
        cout << "C" << i.carbons << "H" << i.hydrogens << ' ';
        for(const string& j :  i.name){
            cout << j << ' ';
        }
        cout << endl;
    }
    
    return 0;
}


void file_opener(ifstream& myfile){
    string input = "";
    cout << "What file do you wish to open?" << endl;
    cin >> input;
    myfile.open(input);
    while (!myfile){
        cout << "File not opened!" << endl;
        cout << "What file do you wish to open?" << endl;
        cin >> input;
        myfile.open(input);
    }
}

void insertion_sort(vector<Hydrocarbon>& vect){
    for(int i = 1; i < vect.size(); i++){
        for(int j = i; j > -1; j--){
            int first = vect[j].carbons;
            int second = vect[j-1].carbons;
            if (first == second){
                first = vect[j].hydrogens;
                second = vect[j-1].hydrogens;
                if (first < second){
                    Hydrocarbon temp = vect[j-1];
                    vect[j-1] = vect[j];
                    vect[j] = temp;
                }
            }
            else{
                if (first < second){
                    Hydrocarbon temp = vect[j-1];
                    vect[j-1] = vect[j];
                    vect[j] = temp;
                }
            }
        }
    }
}

void reader(vector<Hydrocarbon>& vect, ifstream& myfile){
    bool nextline = true;
    while (nextline){
        string name;
        char C;
        int carbos;
        char H;
        int hydros;
        myfile >> name >> C >> carbos >> H >> hydros;
        if (name == ""){
            nextline = false;
        }
        else{
            Hydrocarbon molecule;
            molecule.name.push_back(name);
            molecule.carbons = carbos;
            molecule.hydrogens = hydros;
            bool copy_status = false;
            for(Hydrocarbon& i : vect){
                if((i.carbons == carbos) && (i.hydrogens == hydros)){
                    copy_status = true;
                    i.name.push_back(name);
                }
            }
            if (!copy_status){
                vect.push_back(molecule);
            }
        }
    }
    myfile.close();
}
