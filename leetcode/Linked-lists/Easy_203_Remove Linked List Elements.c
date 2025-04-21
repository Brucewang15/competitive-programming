/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* prev = malloc(sizeof(struct ListNode));
    struct ListNode* p = prev;
    prev->next = head;

    while(head) {
        if (head->val == val) {
            prev->next = head->next;
            head = head->next;
            continue;
        }
        prev = head;
        head = head->next;
    }
    return p->next;
}