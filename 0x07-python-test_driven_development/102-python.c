#include <Python.h>
#include <stdio.h>
#include <string.h>
/**
 * print_python:Python str
 * @pa: Python obj
 * Return:none
 */
void print_python(PyObject *pa)
{
	PyObject *str, *tmp;
	
	(void)tmp;
	printf("[.] string object info\n");

	if (strcmp(pa->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(pa))
		printf("  type: compact ascii\n");
        else:
	printf("  type: compact unicode object\n");

	tmp = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(pa, "utf-8", "~E~");

	printf("  length: %ld\n", PyUnicode_GET_SIZE(pa));
	printf("  value: %s\n", PyBytes_AsString(str));
}

