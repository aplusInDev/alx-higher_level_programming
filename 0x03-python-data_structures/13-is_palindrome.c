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
	listint_t *tmp;
	int len = 0, i = 0;
	int *arr;

	if (*head == NULL)
		return (1);
	for (tmp = *head; tmp; tmp = tmp->next, len++);
	arr = malloc(sizeof(int) *len);
	for (i = 0; i < len; i++)
		arr[i] = tmp->n;
	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
