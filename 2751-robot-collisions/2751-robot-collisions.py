class Solution:
    def survivedRobotsHealths(self, positions: List[int], health: List[int], directions: str) -> List[int]:
        n=len(directions)
        order=sorted(range(n),key=lambda i: positions[i])
        s=[]
        alive=[True]*n
        for i in order:
            if directions[i]=='R':
                s.append(i)
            else:
                while s:
                    t=s[-1]
                    if health[i]<health[t]:
                        alive[i]=False
                        health[t]-=1
                        break
                    elif health[i]>health[t]:
                        health[i]-=1
                        alive[t]=False
                        s.pop()
                        # s.append(i)
                    else:
                        alive[i]=alive[t]=False
                        s.pop()
                        break
            print(s)
        return [health[i] for i in range(n) if alive[i]]
        # n=len(directions)
        # order=sorted(range(n),key=lambda i: positions[i])
        # s=[]
        # alive=[True]*n
        # for i in order:
        #     if directions[i]=='R':
        #         s.append(i)
        #     else:
        #         while s:
        #             t=s.pop()
        #             if health[i]<health[t]:
        #                 alive[i]=False
        #                 health[t]-=1
        #                 s.append(t)
        #                 break
        #             elif health[i]>health[t]:
        #                 health[i]-=1
        #                 alive[t]=False
        #                 s.append(i)
        #             else:
        #                 alive[i]=alive[t]=False
        #                 break
        #     print(s)
        # return [health[i] for i in range(n) if alive[i]]
