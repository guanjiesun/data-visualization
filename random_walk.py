from random import choice


class RandomWalk:
    """生成随机漫步数据"""

    def __init__(self, num_points=5000, max_step=None):
        """初始化随机漫步
        num_points表示最大漫步次数
        max_step表示每一漫步的最大距离(沿着x轴或者y轴)
        """

        # num_points表示随机漫步次数
        self.num_points = num_points

        # 随机漫步的起点、为(0, 0)
        self.x_values = [0]
        self.y_values = [0]

        # 自定义步长选项（默认0到4）
        if max_step is None:
            max_step = 4

        self.step_options = max_step

    def fill_walk(self):
        """计算随机漫步中所有的点"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及开始前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标, 当前点是(x_values[-1], y_values[-1])
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # 保存下一个点的坐标
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        # 决定前进方向以及开始前进的距离
        direction = choice([1, -1])
        distance = choice(range(self.step_options+1))
        step = direction * distance
        return step
