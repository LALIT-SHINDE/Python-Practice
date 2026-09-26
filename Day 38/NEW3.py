def anagram(a,b):
    def sort(txt):
        txt = txt.lower()
        t = list(txt)
        new = []

        while len(t) != 0:
            mini = t[0]

            for i in t:
                if mini > i:
                    mini = i

            new += [mini]
            t.remove(mini)

        txt = "".join(new)
        return txt

    m = sort(a)
    n = sort(b)

    if m==n:
        return f"{a} and {b} are Anagrams"
    else:
        return f"{a} and {b} are not Anagrams"

i = "lalIt"
j = "Allti"
print(anagram(i,j))

# 10. String compression

string = "aaabbcccc"
new = ""

for i in string:
    if i not in new:
        count = 0

        for j in string:
            if i == j:
                count += 1

        print(f"{i}{count}",end="")
        new += i



