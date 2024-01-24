class Solution:
    def interpret(self, command: str) -> str:
        s = {
            "(al)": "al",
            "()": "o"
        }
        for k,v in s.items():
            command = command.replace(k, v)
        
        return command