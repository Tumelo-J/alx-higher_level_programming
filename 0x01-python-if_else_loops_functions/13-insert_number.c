#include "lists.h"
/**
 * insert_node - Inserts an element in an sorted singly linked list
 * @head: Linked list head
 * @number: number to be inserted.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	int value;

	current = *head;
	value = current -> n;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (current == NULL)
	{
		current = new;
	}
	else if (value >= number)
	{
		new -> next = current;
		new -> n = number;
	}
	else
	{
		while ((current -> next != NULL) && (value < number))
			current = current -> next;
		new = current;
	}
	return (new);
}
