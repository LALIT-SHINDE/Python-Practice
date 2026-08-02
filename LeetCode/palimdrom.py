num = int(input("Enter the number: "))
n = num
reverse = 0

while num != 0:
    current = num % 10
    reverse = reverse * 10 + current

    num//=10

if n == reverse:
    print(f"{n} Is a Palimdrome")
else:
    print(f"{n} is not a Palimdrome")

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        reverse = 0

        while num != 0:
            current = num % 10
            reverse = reverse * 10 + current

            num //= 10

        return x == reverse

