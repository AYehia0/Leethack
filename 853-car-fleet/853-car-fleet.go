import "fmt"
func carFleet(target int, position []int, speed []int) int {
    timeArr := make([]float64, target + 1)
    max := 0.0
    
    for i:=0; i<len(position); i++ {
        timeArr[position[i]] = float64(target - position[i]) / float64(speed[i])
    }
    
    count := 0
    for i:=target;i>=0; i-- {
        if timeArr[i] > max {
            max = timeArr[i]
            count++
        }
    }
    
    return count
}