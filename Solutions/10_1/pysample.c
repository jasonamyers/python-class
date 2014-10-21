#include "Python.h"

extern int isprime(int n);
extern int gcd(int x, int y);

/* Prime number check */
PyObject* py_isprime(PyObject *self, PyObject *args) {
  int n,r;
  if (!PyArg_ParseTuple(args,"i",&n)) {
    return NULL;
  }
  r = isprime(n);
  return Py_BuildValue("i",r);
}

/* Compute the greatest common divisor */
PyObject* py_gcd(PyObject *self, PyObject *args) {
  int x,y,r;
  if (!PyArg_ParseTuple(args,"ii",&x,&y)) {
    return NULL;
  }
  r = gcd(x,y);
  return Py_BuildValue("i",r);
}

/* Method table for extension module */
static PyMethodDef samplemethods[] = {
   {"isprime", py_isprime, METH_VARARGS},
   {"gcd", py_gcd, METH_VARARGS},
   {NULL,NULL}
};

/* initialization function */
void initsample() {
   Py_InitModule("sample",samplemethods);
}
