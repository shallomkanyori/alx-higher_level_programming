#include "Python.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: a pointer to the PyObject that is the list to print info about
 *
 * Return: nothing.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_len = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t ind;
	const char *type;

	printf("[*] Size of the Python List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", allocated);

	for (ind = 0; ind < list_len; ind++)
	{
		type = Py_TYPE(PyList_GetItem(p, ind))->tp_name;
		printf("Element %ld: %s\n", ind, type);
	}
}
