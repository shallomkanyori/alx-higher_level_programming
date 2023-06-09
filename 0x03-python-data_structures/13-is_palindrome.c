#include "lists.h"

/**
 * list_len - returns the length of a listint_t list
 * @head: pointer to the first node in the list
 *
 * Return: the length of the list.
 */
int list_len(listint_t *head)
{
	int len = 0;

	while (head)
	{
		head = head->next;
		len++;
	}

	return (len);
}

/**
 * reverse_list - reverses a listint_t list
 * @head: pointer to a pointer to the first node in the list
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *curr, *prev;

	if (head == NULL)
		return (NULL);

	curr = *head;
	prev = NULL;

	while (curr != NULL)
	{
		*head = curr->next;
		curr->next = prev;
		prev = curr;
		curr = *head;
	}

	*head = prev;
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked listint_t list is a palindrome.
 * @head: a pointer to a pointer to the first node in the list
 *
 * Return: 0 if list is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int len;
	int mid; /* the index of the midpoint */
	listint_t *head_a, *head_b, *headb_cpy;

	if (head == NULL)
		return (0);

	len = list_len(*head);
	if (len <= 1)
		return (1);

	mid = (len % 2 == 0) ? (len / 2) : (len / 2) + 1;

	/* reverse 2nd half of list */
	head_b = *head;
	for (; mid > 0; mid--)
		head_b = head_b->next;

	reverse_list(&head_b);

	headb_cpy = head_b;
	head_a = *head;
	while (headb_cpy)
	{
		if (headb_cpy->n != head_a->n)
		{
			reverse_list(&head_b);
			return (0);
		}

		headb_cpy = headb_cpy->next;
		head_a = head_a->next;
	}

	reverse_list(&head_b);
	return (1);
}
