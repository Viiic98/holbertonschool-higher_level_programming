#include "lists.h"
/**
 * check_cycle - Check if a linked list is a cycle
 * @list: pointer to a linked list
 * Return: 0 if not is a cycle, 1 if is a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *head = list, *tail = head;

  while (tail)
    {
      tail = tail->next->next;
      head = head->next;
      if (tail == head)
	return (1);
    }
  return(0);
}
