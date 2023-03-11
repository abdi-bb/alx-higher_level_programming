#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


/**
 * is_palindrome - checks if a singly linked list of integers is a palindrome
 *
 * @head: pointer to the head node of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t *head)
{
	if (head == NULL || head->next == NULL)
	{
		return (1);
	}

	listint_t* slow = head;
	listint_t* fast = head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t* prev = NULL;
	listint_t* curr = slow->next;
	listint_t* next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	listint_t* p1 = head;
	listint_t* p2 = prev;

	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			return (0);
		}
		p1 = p1->next;
		p2 = p2->next;
	}

	return (1);
}

