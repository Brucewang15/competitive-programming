/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    int length = 0;

    struct ListNode* start = head;
    while(head) {
        ++length;
        head = head->next;
    }
    length = length / 2 + 1;
    head = start;
    while (length > 1) {
        --length;
        head = head->next;
    }
    return head;
}