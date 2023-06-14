#include "Python.h"

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about a Python list
 * @p: a pointer to the PyObject that is the Python list
 *
 * Return: nothing.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_len = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyObject *item;
	Py_ssize_t ind;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", allocated);

	for (ind = 0; ind < list_len; ind++)
	{
		item = PyList_GET_ITEM(p, ind);
		type = item->ob_type->tp_name;

		printf("Element %ld: %s\n", ind, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - prints some basic info about a Python bytes object
 * @p: a pointer to the PyObject that is the Python bytes object
 *
 * Return: nothing.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t peek_size;
	Py_ssize_t ind;
	char *byte_str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) != 1)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	peek_size = size > 10 ? 10 : (size + 1);
	byte_str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", byte_str);
	printf("  first %ld bytes: ", peek_size);

	for (ind = 0; ind < peek_size; ind++)
	{
		printf("%02x", byte_str[ind] & 0xff);

		if (ind == (peek_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
