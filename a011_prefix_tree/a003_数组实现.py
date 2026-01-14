# noinspection DuplicatedCode
class Solution:
    def __init__(self):

        """
        初始化函数，初始化字典树的基本参数和结构
        """
        self.capacity = 100000  # 字典树的最大容量
        self.keys_num = 26      # 字符集大小，26个英文字母
        # 初始化字典树节点，使用二维列表表示
        self.node: list[list[int]] = [[0 for _ in range(self.keys_num)] for _ in range(self.capacity)]
        # 记录经过每个节点的单词数量
        self.pass_ = [0 for _ in range(self.capacity)]
        # 记录以每个节点结尾的单词数量
        self.end = [0 for _ in range(self.capacity)]
        self.cnt = 1            # 当前已使用的节点数量

    def entry(self):
        """
        入口函数，用于调用主要解决方案
        :return: 调用solve()函数的结果
        """
        return self.solve()

    def solve(self):
        """
        主要解决方案函数（当前为空实现）
        :return: 无返回值
        """

    def increase(self, string):
        """
        向字典树中插入一个字符串
        :param string: 要插入的字符串
        """
        cur = 1
        self.pass_[cur] += 1  # 根节点经过次数加1
        # 遍历字符串中的每个字符
        for c in string:
            loc = ord(c) - ord("a")  # 计算字符对应的索引
            # 如果当前字符对应的子节点不存在，则创建新节点
            if self.node[cur][loc] == 0:
                self.cnt += 1
                self.node[cur][loc] = self.cnt
            cur = self.node[cur][loc]  # 移动到子节点
            self.pass_[cur] += 1      # 经过次数加1
        self.end[cur] += 1  # 单词结束标记加1

    def search_pass(self, string):
        """
        搜索以给定字符串为前缀的所有字符串数量
        :param string: 要搜索的前缀字符串
        :return: 以该字符串为前缀的字符串数量
        """
        cur = 1
        # 遍历字符串中的每个字符
        for c in string:
            loc = ord(c) - ord("a")  # 计算字符对应的索引
            # 如果当前字符对应的子节点不存在，返回0
            if self.node[cur][loc] == 0:
                return 0
            cur = self.node[cur][loc]  # 移动到子节点
        return self.pass_[cur]  # 返回经过该节点的数量

    def search_end(self, string):
        """
        搜索完全匹配给定字符串的单词数量
        :param string: 要搜索的字符串
        :return: 完全匹配的字符串数量
        """
        cur = 1
        for c in string:
            loc = ord(c) - ord("a")  # 计算字符对应的索引
            # 如果当前字符对应的子节点不存在，返回0
            if self.node[cur][loc] == 0:
                return 0
            cur = self.node[cur][loc]  # 移动到子节点
        return self.end[cur]  # 返回以该节点结尾的单词数量

    def decrease(self, string):
        """
        从字典树中删除一个字符串
        :param string: 要删除的字符串
        :return: 删除成功返回True，字符串不存在返回False
        """
        if self.search_end(string) == 0:
            return False
        cur = 1
        for c in string:
            loc = ord(c) - ord("a")  # 计算字符对应的索引
            nxt = self.node[cur][loc]  # 获取下一个节点
            self.pass_[nxt] -= 1  # 经过次数减1
            # 如果经过次数为0，删除该节点
            if self.pass_[nxt] == 0:
                self.node[cur][loc] = 0
                return True
            cur = nxt  # 移动到下一个节点
        self.end[cur] -= 1  # 结尾标记减1
        return True


def tst_1():
    """
    测试函数，测试字典树的基本操作
    """
    sol = Solution()
    sol.increase("abc")  # 插入字符串"abc"
    print(sol.search_end("abc"))  # 搜索完全匹配"abc"的字符串数量
    print(sol.search_pass("a"))   # 搜索以"a"为前缀的字符串数量
    print(sol.decrease("a"))     # 尝试删除字符串"a"


if __name__ == "__main__":
    tst_1()  # 运行测试函数
