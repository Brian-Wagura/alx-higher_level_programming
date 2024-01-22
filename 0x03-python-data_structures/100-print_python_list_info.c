#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: A PyObject list
 */

void print_python_list_info(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size, i;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
