#include "lists.h"
/**
 * is_palindrome - Function that compare if is a palindrome
 * @head: pointer to linked list
 * Return: 0 if it is not, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head, *tail = *head;
	int n;

	while (first->next)
	{
		tail = first;
		n = first->n;
		while (tail->next->next)
			tail = tail->next;
		if (n == tail->next->n)
		{
			first = first->next;
			tail->next = NULL;
		}
		else
			return (0);
	}
	return (1);
}
