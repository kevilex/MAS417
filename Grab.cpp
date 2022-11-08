#include <iostream>
#include <restclient-cpp/restclient.h>

RestClient::Response r = RestClient::get("https://api.met.no/weatherapi/locationforecast/2.0/classic?altitude=0&lat=58.344681&lon=8.594840");


int main(){
    std::string tempStart ="value=";
    std::string tempEnd = "</temperature>";

    int startval = r.body.find(tempStart) + 7;
    int stopval = r.body.find(tempEnd);
    std::string temp;

    for(startval; startval<startval+(stopval-startval)-2; startval++){
        temp = temp + r.body[startval];
    }

    int tempint = stoi(temp);
    tempint = tempint - 18;
    
    if(tempint<-9){
        tempint = -9;
    } else if(tempint>9){
        tempint = 9;
    }
    std::cout<<tempint;
    return tempint;
}