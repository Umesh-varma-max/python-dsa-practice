class Solution:
    def get_day(self, day):
        switch = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        return switch.get(day, "Invalid Day")

s = Solution()
print(s.get_day(3))  # Expected Output: Wednesday
