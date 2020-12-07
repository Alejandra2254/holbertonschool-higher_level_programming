#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check the cycle in the singly linked list
 * @list: arguments input
 * Return: 0 if no cycle or 1 if its a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *current;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	current1 = list->next;
	while (current != NULL && current1->next != NULL && current1->next->next != NULL)
	{
		if (current1 == current)
			return (1);
		current1 = current1->next->next;
		current = current->next;
	}
	return (0);
}
