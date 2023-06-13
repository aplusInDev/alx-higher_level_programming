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
	listint_t *temp = *head;
	int len = 0, i = 0;
	int arr[4096];

	if (*head == NULL)
		return (1);

	while (temp != NULL)
	{
		arr[len] = temp->n;
		len++;
		temp = temp->next;
	}

	while (i < len / 2)
	{
		if (arr[i] != arr[len - i - 1])
			return (0);
		i++;
	}
	return (1);
}
