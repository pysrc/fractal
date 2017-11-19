/**
	Calculate Julia set and Mandelbrot set by C.
	TDM-GCC 4.8.1 32 -bit Release
**/
#include "calc.h"
#include <windows.h>
#include<math.h>

typedef struct Complex{
	double x;
	double y;
} cpl;

cpl add(cpl x, cpl y){
	cpl z = {
		x.x+y.x,
		x.y+y.y
	};
	return z;
}

cpl mul(cpl x, cpl y){
	cpl z = {
		x.x*y.x - x.y*y.y,
		x.x*y.y+x.y*y.x
	};
	return z;
}

int jCalc(double *args){
	//i, j, zx,zy,cx, cy, width, height, xmax, ymax, N,  expc, R
	//0, 1, 2, 3, 4,  5,  6,     7,      8,    9,    10, 11,   12
	
	cpl C = { args[4], args[5] };
	cpl z = {
		(args[0] / args[6] - 0.5) * args[8] + args[2],
		(args[1] / args[7] - 0.5) * args[9] + args[3]
	};
	cpl tep;
	cpl c = { args[4], args[5] };
	int k = 0;
	int d = 1;
	while(k++ < args[10]){
		if(z.x*z.x+z.y*z.y > args[12]*args[12])
			break;
		d = 1;
		tep = z;
		while(d++ < args[11])
			tep = mul(tep, z);
		z = add(tep, c);
	}
	args[0] = sqrt(z.x*z.x+z.y*z.y);
	return k;
	
}

int mCalc(double *args){
	//i, j, z0x,z0y,zx, zy, width, height, xmax, ymax, N,  expc, R
	//0, 1, 2,   3, 4,  5,  6,     7,      8,    9,    10, 11,   12
	
	cpl z = { args[2], args[3] };
	cpl c = {
		(args[0] / args[6] - 0.5) * args[8] + args[4],
		(args[1] / args[7] - 0.5) * args[9] + args[5]
	};
	cpl tep;
	int k = 0;
	int d = 1;
	while(k++ < args[10]){
		if(z.x*z.x+z.y*z.y > args[12]*args[12])
			break;
		d = 1;
		tep = z;
		while(d++ < args[11])
			tep = mul(tep, z);
		z = add(tep, c);
	}
	args[0] = sqrt(z.x*z.x+z.y*z.y);
	return k;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL,DWORD fdwReason,LPVOID lpvReserved)
{
	switch(fdwReason)
	{
		case DLL_PROCESS_ATTACH:
		{
			break;
		}
		case DLL_PROCESS_DETACH:
		{
			break;
		}
		case DLL_THREAD_ATTACH:
		{
			break;
		}
		case DLL_THREAD_DETACH:
		{
			break;
		}
	}
	
	/* Return TRUE on success, FALSE on failure */
	return TRUE;
}
