#include "lists.h"

/**
 * check_cycle - check if loop found in giving list
 * @list: giving list root
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *curr;

	tmp = list;
	while (tmp->next)
	{
		curr = tmp->next;
		while (curr)
		{
			if (tmp == curr)
				return (1);
			curr = curr->next;
		}
		tmp = curr->next;
	}
	return (0);
}
