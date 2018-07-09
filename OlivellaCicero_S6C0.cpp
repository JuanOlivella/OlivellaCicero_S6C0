#include <iostream>
#include <cstdlib>


using std::cout;
using std::endl;


float funcion(float x, float y);


int main(){

  float h = 0.01;

  int maxx = 4;

  int minx = 0;

  int puntos = (maxx-minx)/(h);

  float x[puntos];

  float y[puntos];

  x[0] = minx;
  
  y[0] = 1.0;


  for(int i = 1; i < puntos; i++){

  x[i] = x[i-1] + h;

  y[i] = y[i-1] + h*(funcion(x[i-1],y[i-1]));

  cout << x[i] << "  " << y[i] << endl;

  }


}


float funcion(float xx, float yy){

  return yy;


}