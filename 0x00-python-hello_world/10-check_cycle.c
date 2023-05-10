#include "lists.h"
/**
 * check_cycle - checks list has a cycle or not
 * @list: pointer to the head of the list
 * Return: bool 0 or 1
 */
int check_cycle(listint_t *list)
{
listint_t *lnode;
listint_t *prev;
lnode = list;
prev = list;
while (list && lnode && lnode->next)
{
list = list->next;
lnode = lnode->next->next;
if (list == lnode)
{
list = prev;
prev = lnode;
while (1)
{
lnode = prev;
while (lnode->next != list && lnode->next != prev)
{
lnode = lnode->next;
}
if (lnode->next == list)
{
break;
}
list = list->next;
}
return (1);
}
}
return (0);
}
