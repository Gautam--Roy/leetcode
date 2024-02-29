class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # ```
        # [0,0,0,1]
        # [0,0,1,0]
        # [0,1,0,1]
        # [1,0,1,1]
        # [0,1,1,1]
        # [1,1,1,2]
        # ```
        members = [0] * forget
        members[-1] += 1
        # print(f"members: {members}")
        for i in range(1, n):
            # print(f"----Start----")
            members = members[1:]
            # print(f"Sliced member: {members}")
            new_member = sum(members[0 : (len(members) - delay + 1)])
            # print(f"spreaders: {members[0: (len(members) - delay + 1)]}")
            # print(f"New member: {new_member}")
            members.append(new_member)
            # print(f"Updated members: {members}")
        # print(members)
        return sum(members) % (10**9 + 7)


"""
[0,0,1]
[0,1,1]
[1,1,2]
[1,2,3]
"""
