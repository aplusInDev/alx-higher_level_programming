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

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	curr = *head, p1 = *head;
	while (curr->next)
		curr = curr->next;
	p2 = curr;
	while (p1 != p2 && p1->next != p2)
	{
		if (p1->n != p2->n)
			return (0);
		p1 = p1->next;
		curr = p1;
		while (curr->next != p2)
			curr = curr->next;
		p2 = curr;
	}
	if (p1->n != p2->n)
		return (0);
	return (1);
}
