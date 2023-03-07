#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the list.
 * @number: The number to insert.
 *
 * Return: The address of the new node, or NULL if it failed.
 */

/* Function to insert a new node into a sorted singly linked list */
listint_t* insert_node(listint_t** head, int number) {
    /* Allocate memory for the new node */
    listint_t* new_node = (listint_t*)malloc(sizeof(listint_t));
    if (new_node == NULL) {
        /* Allocation failed, return NULL */
        return NULL;
    }
    /* Set the data for the new node */
    new_node->n = number;
    new_node->next = NULL;
    /* If the list is empty, the new node becomes the head */
    if (*head == NULL) {
        *head = new_node;
        return new_node;
    }
    /* If the new node is smaller than the head, it becomes the new head */
    if (number < (*head)->n) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }
    /* Traverse the list to find the correct position to insert the new node */
    listint_t* current = *head;
    while (current->next != NULL && current->next->n < number) {
        current = current->next;
    }
    /* Insert the new node after the current node */
    new_node->next = current->next;
    current->next = new_node;
    return new_node;
}