/**
    采用C Extension 方式加速计算
    之前用的ctypes包裹dll方式在循环体中的调用效率不太高
    因此现改用原生C拓展方式
    编译环境：
        Windows: Visual Studio 2017 and python
        Linux: gcc and python-dev
        Mac: gcc and python-dev
    编译命令：
        python setup.py build
-----------------------------------------------------------
The DLL interface of ctypes:
    int jCalc(double *args);
    int mCalc(double *args);
*/


#include <Python.h>
#include<math.h>

/**
    The C function define.
    If you want to build Dynamic Link Library (.dll or .so) file , this is all.
**/

typedef struct{ //复数结构
    double x;
    double y;
} cpl;

cpl add(cpl x, cpl y){ // 复数加法
    cpl z = {
        x.x+y.x,
        x.y+y.y
    };
    return z;
}

cpl mul(cpl x, cpl y){ // 复数乘法
    cpl z = {
        x.x*y.x - x.y*y.y,
        x.x*y.y+x.y*y.x
    };
    return z;
}

int jCalc(double *args){ // 计算J集
    //i, j, zx,zy,cx, cy, width, height, xmax, ymax, N,  expc, R
    //0, 1, 2, 3, 4,  5,  6,     7,      8,    9,    10, 11,   12
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

int mCalc(double *args){ // 计算M集
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


/**
    The Python interface define.
**/
static PyObject *fractension_jCalc(PyObject *self, PyObject *args) { // Python函数接口
    // Python只需要传递顺序传入jCalc规定的参数进来就行了(Python 端用 Tuple 方式组织好， 这样比较快)
    double c_args[13];
    if (!PyArg_ParseTuple(args, "(ddddddddddddd)", &c_args[0], &c_args[1], &c_args[2], &c_args[3], &c_args[4], &c_args[5], &c_args[6], &c_args[7], &c_args[8], &c_args[9], &c_args[10], &c_args[11], &c_args[12]))
        return NULL;
    // 返回一个tuple （迭代次数，逃逸半径），注意参数类型，int, double
    int res = jCalc(c_args);
    return Py_BuildValue("(i,d)", res, c_args[0]);
}

static PyObject *fractension_mCalc(PyObject *self, PyObject *args) {
    double c_args[13];
    if (!PyArg_ParseTuple(args, "(ddddddddddddd)", &c_args[0], &c_args[1], &c_args[2], &c_args[3], &c_args[4], &c_args[5], &c_args[6], &c_args[7], &c_args[8], &c_args[9], &c_args[10], &c_args[11], &c_args[12]))
        return NULL;
    int res = mCalc(c_args);
    return Py_BuildValue("(i,d)", res, c_args[0]);
}

static PyMethodDef FractensionMethods[] = {
    { "jCalc", fractension_jCalc, METH_VARARGS,"Calculate the Julia Set." },
    {"mCalc", fractension_mCalc, METH_VARARGS, "Calculate the Mandelbrot Set." },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fractensionmodel = {
    PyModuleDef_HEAD_INIT,
    "fractension",
    "Extension by C for speed the calculation.",
    -1,
    FractensionMethods
};
 
PyMODINIT_FUNC PyInit_fractension(void)
{
    return PyModule_Create(&fractensionmodel);
}
