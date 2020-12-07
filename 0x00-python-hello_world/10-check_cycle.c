#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check the cycle in the singly linked list
 * @list: arguments input
 * Return: 0 if no cycle or 1 if its a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (slow != NULL && fast->next != NULL && fast->next->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
