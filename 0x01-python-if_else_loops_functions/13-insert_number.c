#include "lists.h"
/**
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tail = *head;

	if (!*head)
		return (NULL);
	while (tail->next->n < number)
		tail = tail->next;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = tail->next;
	tail->next = new;
	return (new);
}
