#include <Python.h>

PyMethodDef methods[] = {
  {NULL, NULL},
};

void initdemo()
{
  (void)Py_InitModule("demo", methods);
}
