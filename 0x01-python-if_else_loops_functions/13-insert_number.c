#include "lists.h"
/**
 * insert_node - insert a sorted node
 * @head: Pointer to a linked list
 * @number: number that will be inserted
 * Return: Pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tail;

	if (!head || !*head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	tail = *head;
	if (tail->n > number)
	{
		new->next = tail;
		*head = new;
	}
	else
	{
		while (tail->next)
		{
			if (tail->next->n < number)
				tail = tail->next;
			else
				break;
		}
		new->next = tail->next;
		tail->next = new;
	}
	return (new);
}
