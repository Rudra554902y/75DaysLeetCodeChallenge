class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        s='L' if moves.count('L')>moves.count('R') else 'R'
        moves=moves.replace('_', s)
        c=0
        for i in moves:
            if i=='L':
                c+=1
            else:
                c-=1
        return abs(c)