#include "lists.h"
/**
 * insert_node - Inserts an element in an sorted singly linked list
 * @head: Linked list head
 * @number: number to be inserted.
 */

#include "lists.h"
#define L listint_t

listint_t *insert_node(listint_t **head, int number)
{
  L *new;
  L *current = *head;
  int inserted = 0;

  /* Memory allocation */
  new = malloc(sizeof(L));

  /* Base case */
  /* Append to the beggining if *head points to NULL or value stored >= number */
  if (current -> next == NULL || current -> n >= number)
  {
    new -> next = current;
    new -> n = number;
    current -> next = new;
  }
  else
  {
    /* Excluding the base case */
    current = current -> next;

    /* Compare number with values stored in nodes */
    while(!inserted)
    {
      if (current -> n > number)
      {
        new -> next = current -> next;
        new -> n = current -> n;
        current -> n = number;
        current -> next = new;
        inserted = 1;
        return (new);
      }
      current = current -> next;
    }
  }
  new -> next = NULL;
  current = new -> next;
  return (new);
}
