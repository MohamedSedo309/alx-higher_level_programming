#include "lists.h"

/**
 * reverse_list - reverse 2nd part of list
 * @h_r: second half header
 * Return: void
 */
void reverse_list(listint_t **h_r)
{
  listint_t *prev;
  listint_t *crr;
  listint_t *next;

  prev = NULL;
  crr = *h_r;

  while (crr != NULL)
    {
      next = crr->next;
      crr->next = prev;
      prev = crr;
      crr = next;
    }
  *h_r = prev;
}

/**
 * compare - compare the 2 lsits
 * @h1: first half head
 * @h2: second half head
 * Return: 1 or 0
 */
int compare(listint_t *h1, listint_t *h2)
{
  listint_t *temp1;
  listint_t *temp2;

  temp1 = h1;
  temp2 = h2;

  while (temp1 != NULL && temp2 != NULL)
    {
      if (temp1->n == temp2->n)
        {
	  temp1 = temp1->next;
	  temp2 = temp2->next;
        }
      else
        {
	  return (0);
        }
    }

  if (temp1 == NULL && temp2 == NULL)
    {
      return (1);
    }

  return (0);
}

/**
 * is_palindrome - checks if a list is palindrome
 * @head: list header
 * Return: 0 false or 1 true
 */
int is_palindrome(listint_t **head)
{
  listint_t *sl, *last, *prev_slow;
  listint_t *scnd_half, *mid;
  int ispalindrome;

  sl = last = prev_slow = *head;
  mid = NULL;
  ispalindrome = 1;

  if (*head != NULL && (*head)->next != NULL)
    {
      while (last != NULL && last->next != NULL)
        {
	  last = last->next->next;
	  prev_slow = sl;
	  sl = sl->next;
        }

      if (last != NULL)
        {
	  mid = sl;
	  sl = sl->next;
        }

      scnd_half = sl;
      prev_slow->next = NULL;
      reverse_list(&scnd_half);
      ispalindrome = compare(*head, scnd_half);

      if (mid != NULL)
        {
	  prev_slow->next = mid;
	  mid->next = scnd_half;
        }
      else
        {
	  prev_slow->next = scnd_half;
        }
    }

  return (ispalindrome);
}
