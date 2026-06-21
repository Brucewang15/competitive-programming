export module min_heap;

import <vector>;
using namespace std;

export struct MinHeap {
    vector<int> heap;

    MinHeap(vector<int> heap);
    void insert(int num);
    int extract(void);
    int get_min(void);

    void _swap(int& a, int& b);
    void _siftup(int i);
    void _siftdown(int i);
};