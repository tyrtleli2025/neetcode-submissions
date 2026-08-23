class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        left = 0
        current_max = 0
        max_window = 0
        right = 0
        while right < len(s):
            if s[right] not in frequencies:
                frequencies[s[right]] = 1
            else:
                frequencies[s[right]] += 1
            if frequencies[s[right]] > current_max:
                current_max = frequencies[s[right]]
            window = right - left + 1
            if window - k - current_max > 0:
                frequencies[s[left]] -= 1
                left += 1
                window = right - left + 1

            if window > max_window:
                max_window = window

            right += 1
        return max_window