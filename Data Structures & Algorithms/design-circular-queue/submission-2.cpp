class MyCircularQueue {

private:
    vector<int> data; // Vector is the needed Data Structure for the Ring Buffer, starts with size 0
    int front;        // this will point to the index of the  
    int count;        // This will help with enque 
public:
    MyCircularQueue(int k) {
        data.resize(k); // Make it size k 
        front = 0;
        count = 0;
    }
    

    bool enQueue(int value) {
        if (this->isFull()) {
            return false;
        }
        // We need to put the value where front + 1 is and then say where front + 1 equals 
        // Is there space in the Ring Buffer
        data[(front + count) % data.size()] = value;
        count++;
        return true;
    }
    
    bool deQueue() {
        if (this->isEmpty()) {
            return false;
        }
        // Do not need to do anything to the value, just move the front pointer
        front = (front + 1) % data.size();
        count -= 1;
        return true;
    }
    
    int Front() {
        if (this->isEmpty()) {
            return -1;
        }
        return data[front];
    }
    // Rear is a bit trickier, technically rear would be front + 1 index 
    int Rear() {
        if (this->isEmpty()) {
            return -1;
        }
        return data[((front + count) - 1) % data.size()];
        
    }
    
    bool isEmpty() {
        if (count == 0) { // only time they would be equal is when they are empty 
            return true;
        }
        return false;
    }
    
    bool isFull() {
        if (count == data.size()) {
            return true;
        }
        return false;    
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */