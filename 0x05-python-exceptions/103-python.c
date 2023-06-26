#include "Python.h"

/**
 * print_python_float - prints some basic info about a Python float object
 * @p: a pointer to the PyObject that is the Python float object
 *
 * Return: nothing.
 */
void print_python_float(PyObject *p)
{
	double value;
	char *v_str;

	fflush(stdout);

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	v_str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", v_str);

	PyMem_Free((void *)v_str);
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: a pointer to the PyObject that is the Python bytes
 *
 * Return: nothing.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t peek_size;
	Py_ssize_t ind;
	char *byte_str;

	fflush(stdout);

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	peek_size = size > 10 ? 10 : (size + 1);
	byte_str = ((PyBytesObject *)p)->ob_sval;

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

/**
 * print_python_list - prints some basic info about Python lists
 * @p: a pointer to the PyObject that is the list
 *
 * Return: nothing.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_len;
	Py_ssize_t allocated;
	PyObject *item;
	Py_ssize_t ind;
	const char *type;

	fflush(stdout);

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_len = PyList_GET_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", allocated);

	for (ind = 0; ind < list_len; ind++)
	{
		item = PyList_GET_ITEM(p, ind);
		type = item->ob_type->tp_name;

		printf("Element %ld: %s\n", ind, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
		else if (strcmp(type, "float") == 0)
			print_python_float(item);
	}
}
