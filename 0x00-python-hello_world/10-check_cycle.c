#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle
 * @list: A pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
