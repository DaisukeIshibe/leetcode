class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        keyIndex = 0
        if ruleKey == "color":
            keyIndex = 1
        elif ruleKey == "name":
            keyIndex = 2
        return sum(1 for item in items if item[keyIndex] == ruleValue)
