#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks a cycle in a singly linked list
 * @list: the linked list to be checked
 *
 * Return: 0 for no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}

