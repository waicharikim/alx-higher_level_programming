#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *next;
    /* Empty list is considered a palindrome */
	if (*head == NULL)
		return (1);
	/* Find the middle node using two pointers (slow and fast) */
	slow = *head;
	fast = *head;
	prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;

		slow->next = prev;
		prev = slow;
		slow = next;
	}
	/* If the list has an odd number of nodes, move slow to the next node */
	if (fast != NULL)
		slow = slow->next;
	/* Compare the first half (prev) with the second half (slow) */
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}
	return (1); /* It's a palindrome */
}
