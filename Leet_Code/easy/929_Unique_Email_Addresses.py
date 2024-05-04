"""
Every valid email consists of a local name and a 
domain name, separated by the '@' sign. 

Besides lowercase letters, the email may 
contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the 
local name, and "leetcode.com" is the domain name.

If you add periods '.' between some characters in the 
local name part of an email address, mail sent there 
will be forwarded to the same address without dots 
in the local name. Note that this rule does not 
apply to domain names.

For example, "alice.z@leetcode.com" and 
"alicez@leetcode.com" forward to the same email address.

If you add a plus '+' in the local name, everything 
after the first plus sign will be ignored. 

This allows certain emails to be filtered. 

Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be
forwarded to "my@email.com".

It is possible to use both of these rules 
at the same time.

Given an array of strings emails where 
we send one email to each emails[i], return 
the number of different addresses that 
actually receive mails.

Example 1:

    Input: emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com",
              "testemail+david@lee.tcode.com"]

    Output: 2

    Explanation: "testemail@leetcode.com" and 
                  "testemail@lee.tcode.com" actually 
                  receive mails.

Example 2:

    Input: emails = ["a@leetcode.com",
                    "b@leetcode.com",
                    "c@leetcode.com"]

    Output: 3
 
Constraints:

    1 <= emails.length <= 100

    1 <= emails[i].length <= 100

    emails[i] consist of lowercase English 
      letters, '+', '.' and '@'.

    Each emails[i] contains exactly one '@' character.
    
    All local and domain names are non-empty.
    
    Local names do not start with a '+' character.

    Domain names end with the ".com" suffix.

Takeaway:

    good string training

"""

class Solution:
    def numUniqueEmails_(self, emails: List[str]) -> int:
        # this works
        # first solution
        
        # we have to check every email
        # we have to check characters before @
        # also have to check domain names too.
        
        # for every email
        # find @
        # find . after @
        # in localname
        # ignore .'s
        # if there is + in local, drop everything
        # from that point
        
        s = set()
        for mail in emails:
            at_index = mail.find("@")
            local = mail[:at_index]
            domain = mail[at_index:mail.find(".com", at_index)]
            temp = []
            for i, elem in enumerate(local):
                if elem not in (".", "+"):
                    temp.append(elem)
                elif elem == ".":
                    continue
                elif elem == "+":
                    # temp = local[:i]
                    break
                    
            s.add("".join(temp) + domain)
            
        return len(s)
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        # this is cool
        unique = set()

        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
            
        return len(unique)
