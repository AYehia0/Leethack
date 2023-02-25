type MinStack struct {
    vals []int
    minVals []int // using a min stack to keep track of the current min val to be appended
}


func Constructor() MinStack {
    return MinStack{}
}


func (this *MinStack) Push(val int)  {
    min := val
    this.vals = append(this.vals, val)
    
    if len(this.minVals) != 0 {
        min = this.minVals[len(this.minVals)-1]
    }
    
    if val < min {
        min = val
    }
    
    this.minVals = append(this.minVals, min)
}


func (this *MinStack) Pop()  {
    this.vals = this.vals[:len(this.vals)-1]
    this.minVals = this.minVals[:len(this.minVals)-1]
}


func (this *MinStack) Top() int {
    return this.vals[len(this.vals)-1]
}


func (this *MinStack) GetMin() int {
    return this.minVals[len(this.minVals)-1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */