#include "lists.h"

int check_loop(int idx, listint_t *curr, listint_t *arr[])
{
	int i = 0;

	while (i < idx)
	{
		if (arr[i] == curr)
			return (-1);
		i++;
	}
	return (1);
}
int check_cycle(listint_t *list)
{
	listint_t *arr[1024], *curr;
	int index = 0;

	curr = list->next;
	arr[index++] = list;
	while (curr)
	{
		if (check_loop(index, curr, arr) == -1)
			return (1);
		arr[index++] = curr;
		curr = curr->next;
	}
	return (0);
}
