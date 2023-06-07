#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert node
 * @head: list root
 * @number: giving number for new node
 *
 * Return: new_node if success, NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *curr, *prev;

	if (*head == NULL || head == NULL)
		return (NULL);
	curr = *head;
	prev = NULL;
	while (curr != NULL)
	{
		if (curr->n < number)
		{
			prev = curr;
			curr = curr->next;
		}
		else
			break;
	}
	new_node = (listint_t *) malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	prev->next = new_node;
	new_node->next = curr;
	return (new_node);
}