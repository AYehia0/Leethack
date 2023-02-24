import "fmt"

func validate(list []byte) bool {
    set := make(map[string]bool)
    for _, item := range list {
        n := string(item)
        if n != "." {
            if set[n] {
                return false
            }else {
                set[n] = true
            }
        }
    }
    return true
}

func isValidSudoku(board [][]byte) bool {
    ROWS := 9
    
    // validating rows
    for _, row := range board {
        if !validate(row) {
            return false
        }
    }
    
    // Creating the cols as list 
    for j:=0;j<ROWS;j++ {
        tmp := make([]byte, 0)
        for i:=0;i<ROWS;i++ {
            tmp = append(tmp, board[i][j])
        }
                    
        if !validate(tmp) {
            return false
        }
    }
    
    for i := 0; i < ROWS; i += 3 {
        for j := 0; j < ROWS; j += 3 {
            cell := make([]byte, 0)
            for k := i; k < i+3; k++ {
                for l := j; l < j+3; l++ {
                    cell = append(cell, board[k][l])
                }
            }
            if !validate(cell) {
                return false
            }
        }
    } 
    return true    
}