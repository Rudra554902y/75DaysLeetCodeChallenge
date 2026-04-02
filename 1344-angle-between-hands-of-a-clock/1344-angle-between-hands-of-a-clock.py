class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12:
            hour=0
        hourd=hour*30+minutes*0.5
        mind=minutes*6
        diff=abs(hourd-mind)
        return min(diff,360-diff)

        