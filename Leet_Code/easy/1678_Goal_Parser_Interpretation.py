"""
You own a Goal Parser that can interpret a string command. The command 
consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal 
Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" 
as the string "al". The interpreted strings are then concatenated 
in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.

Takeaway:

Do not forget str.replace(old, new, count)

also traversing and mapping is cool

my_str = "asdaaa"
new_str = my_str.replace("a", "b", 2)
print(my_str) # asdaaa
print(new_str) # bsdbaa

"""

class Solution:
    def interpret(self, command: str) -> str:
        # make a dictionary - you dont really need this.
        # parser = {"G" : "G",
        #          "()": "o",
        #          "(al)": "al"}
        result = ""
        for i in range(len(command)):
            if command[i] == "G":
                result += "G"
            elif command[i] == "(" and command[i+1] == ")":
                result += "o" 
            elif command[i] == "(" and command[i+1] == "a":
                result += "al"
            else:
                pass
        return result
    
    
    def interpret__(self, command: str) -> str:
        # from a homie
        
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command
