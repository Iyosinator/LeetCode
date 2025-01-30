class Solution:
    def interpret(self, command: str) -> str:
        result = []
        i = 0
        for i in range(len(command)):
            if command[i] == 'G':
                result.append('G')
            elif command[i] == '(':
                if command[i+1] == ')':
                    result.append('o')
                    i += 1
                else:
                    result.append('al')
                    i += 3
        return "".join(result)
        

