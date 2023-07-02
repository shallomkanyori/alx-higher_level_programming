#include "Python.h"

/**
 * print_python_string - prints Python strings
 * @p: a pointer to the PyObject that is the Python string
 *
 * Returns: nothing.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	char *type;
	const char *value;
	PyObject *string;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = PyUnicode_GET_LENGTH(p);
	type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" :
		"compact unicode object";
	string = PyUnicode_AsEncodedString(p, "utf-8", "strict");
	value = PyBytes_AS_STRING(string);

	printf("  type: %s\n", type);
	printf("  length: %ld\n", len);
	printf("  value: %s\n", value);

	Py_DECREF(string);
}
