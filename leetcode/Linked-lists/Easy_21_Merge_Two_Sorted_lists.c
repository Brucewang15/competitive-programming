
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* cur = malloc(sizeof(struct ListNode));
    cur->next = NULL;
    struct ListNode* start = cur;
    
    while (list1 || list2) {
        if (!list1) {
            cur->next = list2;
            break;
        }
        if (!list2) {
            cur->next = list1;
            break;
        }
        if (list1->val <= list2->val) {
            cur->next = list1;
            list1 = list1->next;
            cur = cur->next;
        }
        else {
            cur->next = list2;
            list2 = list2->next;
            cur = cur->next;
        }

    }
    return start->next;
}