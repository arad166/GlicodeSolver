from collections import deque

class Pos:
    def __init__(self, y=-1, x=-1):
        self.y = y  # 現在の行
        self.x = x  # 現在の列

class State:
    def __init__(self, pos, board_type, board_height, operations=None, visited_friends=None):
        self.pos = pos
        self.board_type = board_type
        self.board_height = board_height
        self.operations = operations or []  # 操作履歴（コピー対応）
        self.visited_friends = visited_friends or [[False] * len(board_height[0]) for _ in range(len(board_height))]

    def __eq__(self, other):
        return isinstance(other, State) and (
            self.pos.y == other.pos.y and
            self.pos.x == other.pos.x and
            self.board_type == other.board_type and
            self.board_height == other.board_height
        )

    def __hash__(self):
        return hash((
            self.pos.y,
            self.pos.x,
            tuple(tuple(row) for row in self.board_type),
            tuple(tuple(row) for row in self.board_height),
            tuple(tuple(row) for row in self.visited_friends)
        ))


    def copy(self):
        """状態をコピーして返す"""
        return State(
            pos=Pos(self.pos.y, self.pos.x),
            board_type=[row[:] for row in self.board_type],
            board_height=[row[:] for row in self.board_height],
            operations=self.operations[:],
            visited_friends=[row[:] for row in self.visited_friends]
        )

def check_all_friends(state):
    for y in range(len(state.board_height)):
        for x in range(len(state.board_height[0])):
            if state.board_type[y][x] != '3' and state.board_type[y][x] != 'w':
                continue
            if state.visited_friends[y][x]:
                continue
            return False
    return True

def findPath(board_type, board_height):
    startpos = Pos()
    height = len(board_height)
    width = len(board_height[0])

    for y in range(height):
        for x in range(width):
            if board_type[y][x] == '2':
                startpos = Pos(y, x)
                board_type[y][x] = '1'

    start = State(startpos, board_type, board_height)

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    dir = ['R', 'D', 'L', 'U']

    visited = set()

    que = deque([start])

    while len(que) > 0:
        nowstate = que.popleft()

        if nowstate in visited:
            continue

        visited.add(nowstate)

        # 全ての友達の元に行ったら終了
        if check_all_friends(nowstate):
            return nowstate.operations
        
        nowpos = nowstate.pos

        for d in range(4):
            nextstate = nowstate.copy()
            max_next_height = nextstate.board_height[nextstate.pos.y][nextstate.pos.x]

            if nextstate.board_type[nowpos.y][nowpos.x] in ['1', '3', '7', 'd', 'e', 'f', 'g', 'h', 'i', 'w']:
                nextstate.pos.y = nowpos.y + dy[d]
                nextstate.pos.x = nowpos.x + dx[d]

            if nextstate.board_type[nowpos.y][nowpos.x] in ['7']:
                if 0 <= nextstate.pos.y < height and 0 <= nextstate.pos.x < width:
                    if nextstate.board_height[nextstate.pos.y][nextstate.pos.x] <= nextstate.board_height[nowpos.y][nowpos.x]:
                        nextstate.pos.y = nextstate.pos.y + dy[d]
                        nextstate.pos.x = nextstate.pos.x + dx[d]
                    else:
                        max_next_height += 1

            if nextstate.pos.y < 0 or nextstate.pos.y >= height or nextstate.pos.x < 0 or nextstate.pos.x >= width:
                continue

            if nextstate.board_type[nextstate.pos.y][nextstate.pos.x] in ['0', '4', '5', '6']:
                continue

            if nextstate.board_height[nextstate.pos.y][nextstate.pos.x] > max_next_height:
                continue

            if nextstate.board_type[nextstate.pos.y][nextstate.pos.x] in ['3', 'w']:
                nextstate.visited_friends[nextstate.pos.y][nextstate.pos.x] = True
            
            nextstate.operations.append(dir[d])
            que.append(nextstate)
        
    print("No path found")
    return []


        
        

    
    
