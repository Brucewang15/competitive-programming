import min_heap;
import <iostream>;
import <vector>;

using namespace std;

int main() {
    cout << "--- Testing MinHeap Initialization ---" << endl;
    vector<int> initial_data = {15, 3, 17, 10, 84, 19, 6, 22, 9};
    MinHeap h(initial_data);

    cout << "Min should be 3: " << h.get_min() << endl;
    
    cout << "\n--- Testing Extract ---" << endl;
    cout << "Extracting (should be 3): " << h.extract() << endl;
    cout << "Extracting (should be 6): " << h.extract() << endl;
    cout << "Extracting (should be 9): " << h.extract() << endl;

    cout << "\n--- Testing Insert ---" << endl;
    cout << "Inserting 1 and 4..." << endl;
    h.insert(1);
    h.insert(4);

    cout << "Min should now be 1: " << h.get_min() << endl;
    cout << "Extracting (should be 1): " << h.extract() << endl;
    cout << "Extracting (should be 4): " << h.extract() << endl;
    cout << "Extracting (should be 10): " << h.extract() << endl;

    return 0;
}