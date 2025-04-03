import pprint  # 导入 pprint 模块，用于以格式化方式打印数据结构


class Maze:
    def __init__(self):
        # 定义三种颜色对应的数值：
        # "white": 0 —— 表示未访问的路径（白色区域）
        # "gray": 1  —— 表示正在探索的路径（灰色区域）
        # "black": 2 —— 表示已探索完毕或者是障碍物（黑色区域）
        self.color = {
            "white": 0,
            "gray": 1,
            "black": 2,
        }
        # 通过 get_maze 函数构造迷宫，同时传入颜色字典，生成一个 7 行 8 列的迷宫
        self.maze = get_maze(self.color)

    def tst_0(self):
        # 测试函数，从起点 (1, 1) 开始进行深度优先搜索（DFS）
        self.dfs_maze(1, 1)
        # 使用 pprint 模块打印迷宫的最终状态
        pprint.pprint(self.maze)

    def dfs_maze(self, source_x, source_y):
        # 调用递归探索函数 explore 从起点 (source_x, source_y) 开始搜索路径
        self.explore(source_x, source_y)

    def explore(self, x, y):
        # 检查目标位置是否已经被访问（灰色），这里目标位置定为 (5,6)
        # 如果 (5,6) 被标记为灰色，表示已经找到了到达终点的路径，直接返回 True
        if self.maze[5][6] == self.color["gray"]:
            return True

        # 判断当前坐标 (x, y) 是否超出迷宫边界，
        # 迷宫行的索引范围为 0 到 6，列的索引范围为 0 到 7
        if x < 0 or x > 6 or y < 0 or y > 7:
            return False

        # 将当前位置标记为灰色，表示正在探索这条路径
        self.maze[x][y] = self.color["gray"]

        # 获取当前位置 (x, y) 的所有邻居（上、右、下、左）
        for (i, j) in get_neighbor_list(x, y):
            # 如果邻居未访问（白色），并且从该邻居出发的探索最终能够到达终点，则返回 True
            if self.maze[i][j] == self.color["white"] and self.explore(i, j):
                return True

        # 如果所有邻居都无法找到通往终点的路径，则将当前点标记为黑色，表示这是一条死路
        self.maze[x][y] = self.color["black"]
        return False


def get_maze(color):
    # 初始化一个 7 行 8 列的迷宫，所有单元格的初始值都为 0（代表白色）
    maze = [[0 for _ in range(8)] for _ in range(7)]  # 7行8列
    pprint.pprint(maze)  # 打印初始化后的迷宫（全部为白色）

    # 设置迷宫的边界为障碍（黑色），使迷宫外围不可通行
    for j in range(8):
        maze[0][j] = color["black"]  # 第一行设置为黑色
        maze[6][j] = color["black"]  # 最后一行设置为黑色
    for i in range(7):
        maze[i][0] = color["black"]  # 第一列设置为黑色
        maze[i][7] = color["black"]  # 最后一列设置为黑色

    # 在迷宫内部增加障碍物
    # 例如，将第三行（索引为 2）的前 3 个单元格设置为黑色，作为内部障碍
    for j in range(3):
        maze[2][j] = color["black"]

    print()  # 输出一个空行，便于区分打印内容
    pprint.pprint(maze)  # 打印设置边界和障碍后的迷宫
    return maze  # 返回生成好的迷宫


def get_neighbor_list(x, y):
    # 返回当前位置 (x, y) 的四个相邻位置（上、右、下、左）
    return [
        (x - 1, y),  # 上面的邻居
        (x, y + 1),  # 右侧的邻居
        (x + 1, y),  # 下面的邻居
        (x, y - 1),  # 左侧的邻居
    ]


if __name__ == '__main__':
    # 当本模块作为主程序运行时，创建 Maze 类实例并调用 tst_0 测试函数
    m = Maze()
    m.tst_0()
