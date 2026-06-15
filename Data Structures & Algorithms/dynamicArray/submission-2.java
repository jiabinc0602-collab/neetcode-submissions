class DynamicArray {
    public int[] arr;
    public int[] copy;
    public int size;
    public int capacity;
    public DynamicArray(int capacity) {
        arr = new int[capacity];
        this.size = 0;
        this.capacity = capacity;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if(this.size == this.capacity){
            resize();
        }
        arr[size] = n;
        this.size = this.size + 1;
    }

    public int popback() {
        int dummy = arr[size-1];
        arr[size-1] = 0;
        this.size = size-1;
        return dummy;
    }

    private void resize() {
        copy = new int[2*capacity];
        for(int i = 0; i < arr.length; i++){
            copy[i] = arr[i];
        }
        arr = copy;
        this.capacity = 2 * this.capacity;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
