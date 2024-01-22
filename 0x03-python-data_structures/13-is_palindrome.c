#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointet to the head of a linked list
 *
 * Return: 0 if it is not a plaindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	size_t count = 0;
	listint_t *current = *head;
	int arr[count];

	current = *head;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	for (size_t i = 0; i < count; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}
	for (size_t i = 0; i < count / 2; i++)
	{
		if (arr[i] != arr[count - 1 - i])
		{
			return (0);
		}
	}

	return (1);
}
