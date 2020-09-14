# 01 - Unique Email Addresses
# https://leetcode.com/explore/featured/card/google/67/sql-2/3044/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        # How many unique email addresses are there?
        # Dots "." don't count in address names, as well as anything
        # beyond "+" sign, if any.
        def strip_email(email : str) -> str:
            name, domain = email.split("@")
            name = name.replace(".", "")
            name = name.split("+")[0]
            return name + "@" + domain

        # unique_emails = set(map(strip_email, emails)) 
        unique_emails = set([strip_email(email) for email in emails])

        return len(unique_emails)
