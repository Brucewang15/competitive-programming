/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head) {
    int length = 0;
    struct ListNode* start = head;
    while(head) {
        ++length;
        head = head->next;
    }
    head = start;
    int ans = 0;
    --length;
    while (head) {
        ans += head->val * pow(2, length);
        --length;
        head = head->next;
    }
    return ans;
}