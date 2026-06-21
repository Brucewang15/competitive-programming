module min_heap;

import <vector>;
using namespace std;


void MinHeap::_swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void MinHeap::_siftup(int i) {
    while (i > 1 && this->heap[i] < this->heap[i/2]) {
        _swap(this->heap[i], this->heap[i/2]);
        i /= 2;
    }
}

void MinHeap::_siftdown(int i) {
    int n = this->heap.size() - 1;
    while (true) {
        int smallest = i;
        int left = 2*i;
        int right = 2*i+1;

        // min(i, left, right) = min(right, min(i, left))
        if (left <= n && this->heap[smallest] > this->heap[left]) {
            smallest = left;
        }
        
        if (right <= n && this->heap[smallest] > this->heap[right]) {
            smallest = right;
        }

        // if smallest is the current node i, this means min heap property is satisfied
        // and siftdown is finished. otherwise, _swap, set current node to whichever child node is smaller and repeat
        if (smallest == i) {
            break;
        }
        else {
            _swap(this->heap[i], this->heap[smallest]);
            i = smallest;
        }
    }
}

MinHeap::MinHeap(vector<int> heap = {}) {
    // copy array into this->heap for 1 based indexing
    for (size_t i = 0; i < heap.size(); ++i) {
        this->heap.push_back(heap[i]);
    }
    // siftdown all elements
    for (size_t i = (this->heap.size() - 1) / 2; i > 0; --i) {
        _siftdown(i);
    }
}

void MinHeap::insert(int num) {
    this->heap.push_back(num);
    _siftup(this->heap.size()-1);
}

int MinHeap::extract(void) {
    int min = this->heap[1];

    _swap(this->heap[1], this->heap[this->heap.size()-1]);
    this->heap.pop_back();
    _siftdown(1);
    return min;
}

int MinHeap::get_min(void) {
    return this->heap[1];
}
