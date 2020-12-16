#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: pointer to the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *newhead, *current;

	current = *head; 
	newhead = reversel(head);

	while (newhead && head )
	{
		if (newhead->n != current->n)
				return 0;
		newhead = newhead->next;
		current = current->next;
	}
	return(newhead == NULL && current == NULL);
}
listint_t *reversel(listint_t **head)
{
	listint_t *temp, *newhead, *current;

	current = *head; 
	if (*head == NULL)
		return 0;
	while (*head)
	{
		temp = malloc(sizeof(listint_t));
		temp->n = current->n;
		temp->next = newhead;
		newhead = temp;
		current = current->next;
	}
	return (newhead);
}
