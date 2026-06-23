class Solution {
public:
    void printStack(deque<string> dq) {
        while (!dq.empty()) {
            cout << dq.front() << " ";
            dq.pop_front();
        }
        cout << endl;
    }
    string decodeString(string s) {
        string decoded = "";
        deque<string> dq;

        int i = 0;

        while (i < s.length()) {
            string temp = "";
            printStack(dq);

            if (s[i] >= '0' && s[i] <= '9') {
                while (s[i] >= '0' && s[i] <= '9') {
                    temp += s[i];
                    ++i;
                }
                ++i; // for [
                dq.push_back(temp);
                continue;
            }
            if (s[i] >= 'a' and s[i] <= 'z') {
                while (s[i] >= 'a' and s[i] <= 'z') {
                    temp += s[i];
                    ++i;
                }
                dq.push_back(temp);
                continue;
            }
            if (s[i] == ']') {
                string encoded;;
                while (dq.back()[0] < '0' || dq.back()[0] > '9') {
                    encoded = dq.back() + encoded;
                    dq.pop_back();
                }
                int k = stoi(dq.back());
                dq.pop_back();

                string to_add = "";
                for (int r = 0; r < k; ++r) {
                    to_add += encoded;
                }
                dq.push_back(to_add);
                ++i;
            }
        }

        while (!dq.empty()) {
            decoded += dq.front();
            dq.pop_front();
        }

        return decoded;
    }
};