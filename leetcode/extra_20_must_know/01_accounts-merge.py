# [ Name: Accounts Merge ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/accounts-merge/ ]

"""
Given a list of accounts where each account contains a name and emails, 
merge accounts that share common emails and return the merged accounts.
Each account is a list with the name as the first element followed by email strings.
Constraints: 1 <= accounts.length <= 1000, 1 <= accounts[i].length <= 10, email strings are unique per person.
Return a list with each account's name followed by sorted unique emails. 
Example: Input: [["John","johnsmith@mail.com","john00@mail.com"],["John","johnnybravo@mail.com"],["John","johnsmith@mail.com","john_newyork@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["John","johnnybravo@mail.com"]]
"""

from typing import List

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    pass

if __name__ == "__main__":
    assert sorted([set(acc) for acc in accountsMerge([["John","johnsmith@mail.com","john00@mail.com"],["John","johnnybravo@mail.com"],["John","johnsmith@mail.com","john_newyork@mail.com"]])]) == sorted([set(["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"]), set(["John","johnnybravo@mail.com"])])
    assert sorted([set(acc) for acc in accountsMerge([["Alex","alex5@mail.com"],["Alex","alex3@mail.com","alex5@mail.com"],["Earl","earl@mail.com"]])]) == sorted([set(["Alex","alex5@mail.com","alex3@mail.com"]), set(["Earl","earl@mail.com"])])
    assert sorted([set(acc) for acc in accountsMerge([["Mary","mary@mail.com"],["Mary","mary2@mail.com"]])]) == sorted([set(["Mary","mary@mail.com"]), set(["Mary","mary2@mail.com"])])
    assert sorted([set(acc) for acc in accountsMerge([["A","a1@mail.com","a2@mail.com"],["A","a2@mail.com","a3@mail.com"],["A","a3@mail.com","a4@mail.com"]])]) == [set(["A","a1@mail.com","a2@mail.com","a3@mail.com","a4@mail.com"])]
    assert sorted([set(acc) for acc in accountsMerge([["Bob","bob@mail.com","bob2@mail.com"],["Bob","bob3@mail.com"]])]) == sorted([set(["Bob","bob@mail.com","bob2@mail.com"]), set(["Bob","bob3@mail.com"])])
    assert sorted([set(acc) for acc in accountsMerge([["Jane","jane@mail.com","jane2@mail.com"],["Jane","jane2@mail.com","jane3@mail.com"],["Jake","jake@mail.com"]])]) == sorted([set(["Jane","jane@mail.com","jane2@mail.com","jane3@mail.com"]), set(["Jake","jake@mail.com"])])
    assert accountsMerge([["A","a@mail.com"]]) == [["A","a@mail.com"]]
    assert sorted([set(acc) for acc in accountsMerge([["Foo","foo@mail.com","foo2@mail.com","foo3@mail.com"],["Foo","foo3@mail.com","foo4@mail.com"],["Bar","bar@mail.com"]])]) == sorted([set(["Foo","foo@mail.com","foo2@mail.com","foo3@mail.com","foo4@mail.com"]), set(["Bar","bar@mail.com"])])
