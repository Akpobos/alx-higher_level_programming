#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: points to pointer to head node
 * @number: number to insert
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev_node, *head_node;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(*new));
	if (new == NULL)
		return (NULL);
	new->next = NULL;
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	head_node = *head;
	prev_node = *head;
	while ((*head)->next)
	{
		if ((*head)->n > number)
		{
			new->next = *head;
			prev_node->next = new;
			break;
		}
		prev_node = *head;
		head = &((*head)->next);
	}
	if (prev_node->next == NULL)
	{
		if (prev_node->n > number && prev_node == head_node)
		{
			new->next = prev_node;
			head_node = new;
		}
		else
			prev_node->next = new;
	}

	return (new);
}
