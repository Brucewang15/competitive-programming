/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* temp = NULL;

    struct ListNode* start = head;

    while(head) {
        temp = malloc(sizeof(struct ListNode));
        temp->val = head->val;
        temp->next = prev;
        prev = temp;
        head = head->next;        
    }
    head = start;
    while(head) {
        if (head->val != temp->val) {
            return false;
        }
        head = head->next;
        struct ListNode* tptr = temp;
        temp = temp->next;
        free(tptr);
    }
    return true;

}

