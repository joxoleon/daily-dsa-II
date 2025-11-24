# [ Name: Reconstruct Itinerary ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 9 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/reconstruct-itinerary/ ]

"""
Given a list of airline tickets represented as pairs of departure and arrival airports [from, to], reconstruct the itinerary in order using all tickets exactly once. The itinerary must begin at "JFK".
Return the itinerary that has the smallest lexical order when choices are available.
Input: tickets as List of Lists of strings.
Output: List of strings representing the itinerary.
Constraints: All tickets form at least one valid itinerary.
Example: Input: [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
         Output: ["JFK","MUC","LHR","SFO","SJC"]
"""

from typing import List

def findItinerary(tickets: List[List[str]]) -> List[str]:
    pass

if __name__ == "__main__":
    assert findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]) == ["JFK","MUC","LHR","SFO","SJC"]
    assert findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"]
    assert findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ["JFK","NRT","JFK","KUL"]
    assert findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]) == ['JFK', 'ANU', 'EZE', 'AXA', 'TIA', 'ANU', 'JFK', 'TIA', 'JFK', 'ANU', 'TIA']
    assert findItinerary([["JFK","A"],["A","B"],["B","C"],["C","A"]]) == ["JFK","A","B","C","A"]
    assert findItinerary([["JFK","ATL"],["ATL","JFK"]]) == ["JFK","ATL","JFK"]
    assert findItinerary([["JFK","A"],["A","B"],["B","JFK"],["JFK","A"]]) == ["JFK","A","B","JFK","A"]
    assert findItinerary([["JFK","SFO"]]) == ["JFK","SFO"]
