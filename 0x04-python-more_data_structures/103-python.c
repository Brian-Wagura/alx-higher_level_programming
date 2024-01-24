#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about python lists
 * @p: PyObject representing the Python list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}
	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: PyObject representing the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", str);

	printf(" first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i < 9 && i < size - 1)
		{
			printf(" ");
		}
	}
	printf("\n");
}
