#include "lists.h"

/**
 * check_cycle -checks if a singly linked list has a cycle in it
 * @list: list root
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr, *tmp;

	if (!list)
		return (0);
	curr = list;
	while (curr)
	{
		tmp = curr->next;
		while (tmp)
		{
			if (tmp == curr)
				return (1);
			tmp = tmp->next;
		}
		curr = curr->next;
	}
	return (0);
}
