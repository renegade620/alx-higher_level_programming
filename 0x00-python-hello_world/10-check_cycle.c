#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list has a cycle in it
 * @list: singly-linked list
 *
 * Return: 0 - no cycle, 1 - there's a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *x,  *y;

	if (list == NULL || list->next == NULL)
		return (0);

	x = list;
	y = list->next;

	while (x && y && y->next)
	{
		if (x == y)
			return (1);

		x = x->next;
		y = y->next->next;
	}
	return (0);
}

