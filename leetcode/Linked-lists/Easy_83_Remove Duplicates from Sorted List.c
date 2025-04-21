/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* p = head;

    if(!head) {
        return NULL;
    }

    struct ListNode* prev = head;
    head = head->next;
    while(head) {
        if(prev->val == head->val) {
            prev->next = head->next;
            head = head->next;
            continue;
        }
        prev = head;
        head = head->next;
    }
    return p;
}