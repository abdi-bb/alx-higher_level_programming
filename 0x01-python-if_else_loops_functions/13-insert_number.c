/*
#include <stdlib.h>
#include "lists.h"


 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the list.
 * @number: The number to insert.
 *
 * Return: The address of the new node, or NULL if it failed.
 
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
*/

#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to address of head of list
 * @number: integer to be include in new node
 * Return: address of new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	if (*head == NULL)
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else if (number <= (*head)->n)
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && number > temp->next->n)
		{
			temp = temp->next;
		}
		newnode->n = number;
		newnode->next = temp->next;
		temp->next = newnode;
		return (newnode);
	}
	return (NULL);
}
