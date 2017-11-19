/**
	Calculate Julia set and Mandelbrot set by C.
	TDM-GCC 4.8.1 64 -bit Release
**/
#ifndef _DLL_H_
#define _DLL_H_

#if BUILDING_DLL
#define DLLIMPORT __declspec(dllexport)
#else
#define DLLIMPORT __declspec(dllimport)
#endif

int jCalc(double *args);
int mCalc(double *args);

#endif

