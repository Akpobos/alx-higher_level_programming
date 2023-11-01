#include "lists.h"

#include<stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: points to pointer to head node
 * @number: number to insert
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *head_node;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(*new));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	head_node = *head;
	prev = *head;
	while ((*head)->next)
	{
		if (number < (*head)->n)
		{
			new->next = *head;

			if (head_node != *head)
				prev->next = new;
			break;
		}
		prev = *head;
		head = &((*head)->next);
	}
	prev = *head;
	if (prev->next == NULL)
	{
		if (number < prev->n)
			new->next = prev;
		else
			prev->next = new;
	}
	if (*head == head_node)
		*head = new;
	return (new);
}
