#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *  * is_palindrome - implements main
 *   *
 *    * Return: 0 if is not a palindrome and 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j;
	struct node *front, *rear;
	
	while(i != 10)
	{
		front = rear = n;
		for (j =0; j<i; j++)
		{
			front = front->*next;
		}
		for (j=0; j<n - (i+1); j++)
		{
			rear = rear->*next;
		}
		if (front->num != rear->num)
		{
			return 0;
		}
		else
		{
			i++;
		}
	}
	return 1;
}
