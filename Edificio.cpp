#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;


double u[3];
double v[3];


double uTemp[3];
double vTemp[3];


double m = 1000.0;
double k = 2000.0;
double gammy = 0;

int i = 0;

double dt = 0.001;
double uMax[100][3];
double w = 0;


double a0(double t){
return ( -gammy*v[0] - 2*k*u[0] +k*u[1] + sin(w*t) ) / m;
}

double a1(double t){
return ( -gammy*v[1] + k*u[0] - 2*k*u[1] +k*u[2] ) / m;
}

double a2(double t){
return ( -gammy*v[2] + k*u[1] - k*u[2] ) / m;
}


double * leapfrog(double tmax){
static double uMax[3];
for (i = 0; i<3;i++){
	u[i]=0;
	v[i]=0;
	uTemp[i]=0;
	vTemp[i]=0;
	uMax[i]=0;
}

double t = 0;

vTemp[0] += 0.5*a0(0)*dt;
vTemp[1] += 0.5*a1(0)*dt;
vTemp[2] += 0.5*a2(0)*dt;
i = 0;

while(t<tmax){


	u[0] += vTemp[0]*dt;
	u[1] += vTemp[1]*dt;	
	u[2] += vTemp[2]*dt;

	v[0] = vTemp[0] + 0.5*a0(t)*dt;
	v[1] = vTemp[1] + 0.5*a1(t)*dt;
	v[2] = vTemp[2] + 0.5*a2(t)*dt;

	vTemp[0] = v[0]+0.5*a0(t)*dt;
	vTemp[1] = v[1]+0.5*a1(t)*dt;
	vTemp[2] = v[2]+0.5*a2(t)*dt;


	for(i = 0;i<3;i++){
			if(abs(u[i]) > uMax[i]){
				uMax[i] = abs(u[i]);
			}
		}
	t += dt;
	i+=1;
	}

	return uMax;

}


double * leapfrogP(double tmax, string file){
static double uMax[3];


ofstream out(file);

for (i = 0; i<3;i++){
	u[i]=0;
	v[i]=0;
	uTemp[i]=0;
	vTemp[i]=0;
	uMax[i]=0;
}

double t = 0;

vTemp[0] += 0.5*a0(0)*dt;
vTemp[1] += 0.5*a1(0)*dt;
vTemp[2] += 0.5*a2(0)*dt;
i = 0;

while(t<tmax){
		out << t << " ";
		for(i = 0;i<3;i++){
			out << u[i] << " ";
		}
		out << "\n";

	u[0] += vTemp[0]*dt;
	u[1] += vTemp[1]*dt;	
	u[2] += vTemp[2]*dt;

	v[0] = vTemp[0] + 0.5*a0(t)*dt;
	v[1] = vTemp[1] + 0.5*a1(t)*dt;
	v[2] = vTemp[2] + 0.5*a2(t)*dt;

	vTemp[0] = v[0]+0.5*a0(t)*dt;
	vTemp[1] = v[1]+0.5*a1(t)*dt;
	vTemp[2] = v[2]+0.5*a2(t)*dt;


	for(i = 0;i<3;i++){
			if(abs(u[i]) > uMax[i]){
				uMax[i] = abs(u[i]);
		}
	}


	t += dt;
	i+=1;

}
		out.close();

	return uMax;

}


int main(){
  

  double tmax = 100;
  w = 1.0*sqrt(k/m);
  //cout << w << "\n";
  double *umax = leapfrogP(tmax,"w0.dat");



  ofstream outW("w.dat");
  w = 0.2*sqrt(k/m);
  double wfinal = 3.0;
  double dw = (wfinal-0.2)/100*sqrt(k/m);
  while(w < wfinal*sqrt(k/m) ){

  	umax = leapfrog(tmax);
  	outW << w << " ";
	for(i = 0;i<3;i++){
		outW << umax[i] << " ";
	}
	outW << "\n";
	w += dw;
  }

  // se elegirá 0.2, 0.452, 1.236, 1.796. Los últimos tres corresponden a resonancias. El primero es un punto normal.

  w = 1.796*sqrt(k/m);
  //cout << w << "\n";
  umax = leapfrogP(tmax, "w4.dat");

  w = 1.236*sqrt(k/m);
  //cout << w << "\n";
  umax = leapfrogP(tmax, "w3.dat");

  w = 0.452*sqrt(k/m);
  //cout << w << "\n";
  umax = leapfrogP(tmax, "w2.dat");

  w = 0.2*sqrt(k/m);
  //	cout << w << "\n";
  umax = leapfrogP(tmax, "w1.dat");
  
  outW.close();
  return 0;
}











