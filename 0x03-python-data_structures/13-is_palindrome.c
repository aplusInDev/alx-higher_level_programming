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
	listint_t *slow = *head, *fast = *head;
	int stack[2048];
	int top = 0;

	while (fast && fast->next)
	{
		stack[top++] = slow->n;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (stack[--top] != slow->n)
			return 0;
		slow = slow->next;
	}
	return 1;
}
