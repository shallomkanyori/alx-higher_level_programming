#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: pointer to pointer to first node in list
 * @number: the integer data of the new node
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr;
	listint_t *prev;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	curr = *head;
	prev = NULL;
	while (curr)
	{
		if (curr->n > number)
			break;

		prev = curr;
		curr = curr->next;
	}

	if (curr == *head)
	{
		new->next = curr;
		*head = new;
		return (new);
	}

	prev->next = new;
	new->next = curr;
	return (new);
}
