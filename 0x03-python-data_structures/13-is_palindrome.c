#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if giving liked
 * list is palindrom
 * @head: the list root
 *
 * Return: 1 if linked list is palindrom
 * 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *p1, *p2, *curr;

	if (*head == NULL)
		return (1);
	curr = *head, p1 = *head;
	while (curr->next)
		curr = curr->next;
	p2 = curr;
	while (p1 != p2)
	{
		curr = p1;
		if (p1->n != p2->n)
			return (0);
		while (curr->next != p2)
			curr = curr->next;
		if (p1->next == p2)
			break;
		p2 = curr;
		p1 = p1->next;
	}
	return (1);
}
