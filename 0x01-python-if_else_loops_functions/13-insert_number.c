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
	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);


	if (current == NULL)
	{
		new -> next = NULL;
		new -> n = number;
	}
	else if ((current -> n) >= number)
	{
		new -> next = current;
		new -> n = number;
	}
	else
	{
		while ((current -> next != NULL) && ((current -> n) < number))
			current = current -> next;
		new = current;
		new -> n = number;
	}
	return (new);
}
