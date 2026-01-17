import tkinter as tk


class HanoiGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("汉诺塔演示 (Tower of Hanoi)")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        # --- 配置参数 ---
        self.width = 800
        self.height = 500
        self.peg_xs = [200, 400, 600]  # A, B, C 柱子的X坐标
        self.peg_y_bottom = 450  # 柱子底部Y坐标
        self.peg_height = 300  # 柱子高度
        self.disk_height = 20  # 圆盘高度
        self.max_disk_width = 180  # 最大圆盘宽度
        self.min_disk_width = 40  # 最小圆盘宽度

        # 映射 A, B, C 到 索引 0, 1, 2
        self.peg_map = {"A": 0, "B": 1, "C": 2}

        # 状态变量
        self.num_disks = 0
        self.disks = [[], [], []]  # 存储每个柱子上的圆盘对象
        self.is_running = False
        self.move_generator = None

        # --- 界面布局 ---
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack(side=tk.TOP)

        # 底部控制面板
        control_frame = tk.Frame(self.master)
        control_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # 圆盘数量输入
        tk.Label(control_frame, text="圆盘数量:").pack(side=tk.LEFT, padx=5)
        self.disk_entry = tk.Entry(control_frame, width=5)
        self.disk_entry.insert(0, "5")
        self.disk_entry.pack(side=tk.LEFT, padx=5)

        # 速度控制
        tk.Label(control_frame, text="速度(快-慢):").pack(side=tk.LEFT, padx=10)
        self.speed_scale = tk.Scale(control_frame, from_=50, to=1000, orient=tk.HORIZONTAL, length=150)
        self.speed_scale.set(300)
        self.speed_scale.pack(side=tk.LEFT, padx=5)

        # 按钮
        self.btn_start = tk.Button(control_frame, text="开始演示", command=self.start_demo, bg="#dddddd")
        self.btn_start.pack(side=tk.LEFT, padx=20)

        self.btn_reset = tk.Button(control_frame, text="重置", command=self.reset_scene, bg="#dddddd")
        self.btn_reset.pack(side=tk.LEFT, padx=5)

        self.lbl_info = tk.Label(control_frame, text="准备就绪", fg="blue")
        self.lbl_info.pack(side=tk.RIGHT, padx=20)

        # 初始化场景
        self.reset_scene()

    def draw_pegs(self):
        """绘制柱子和底座"""
        self.canvas.delete("all")
        # 底座
        self.canvas.create_rectangle(50, self.peg_y_bottom, 750, self.peg_y_bottom + 20, fill="#8B4513")
        # 柱子
        for x in self.peg_xs:
            self.canvas.create_line(x, self.peg_y_bottom, x, self.peg_y_bottom - self.peg_height, width=6, fill="#8B4513")

        # 标签
        labels = ["A", "B", "C"]
        for i, x in enumerate(self.peg_xs):
            self.canvas.create_text(x, self.peg_y_bottom + 40, text=labels[i], font=("Arial", 14, "bold"))

    def create_disks(self, n):
        """初始化圆盘 (修正版：大盘在下，小盘在上)"""
        self.disks = [[], [], []]
        colors = ["#FF5733", "#C70039", "#900C3F", "#581845", "#2874A6", "#1ABC9C", "#F1C40F", "#E67E22"]

        # 从底部(i=0)往顶部(i=n-1)生成
        for i in range(n):
            # 1. 宽度：i=0(底)最宽，i=n-1(顶)最窄
            width = self.max_disk_width - (i * (self.max_disk_width - self.min_disk_width) / max(1, n - 1))

            # 2. 颜色
            color = colors[i % len(colors)]

            # 3. 位置：i=0 在 peg_y_bottom，i 越大越靠上
            x_center = self.peg_xs[0]
            y_bottom = self.peg_y_bottom - (i * self.disk_height)

            tag = f"disk_{i}"
            rect = self.canvas.create_rectangle(
                x_center - width / 2,
                y_bottom - self.disk_height,
                x_center + width / 2,
                y_bottom,
                fill=color,
                outline="black",
                width=1,
                tags=tag,
            )

            # 4. 加入栈
            self.disks[0].append({"id": rect, "width": width})

    def reset_scene(self):
        """重置画面"""
        self.is_running = False
        try:
            n = int(self.disk_entry.get())
            if n > 12:
                n = 12
                self.disk_entry.delete(0, tk.END)
                self.disk_entry.insert(0, "12")
                self.lbl_info.config(text="圆盘限制最大12个", fg="red")
        except ValueError:
            n = 3

        self.num_disks = n
        self.draw_pegs()
        self.create_disks(n)
        self.lbl_info.config(text=f"准备就绪 ({n} 个圆盘)", fg="blue")

    def hanoi_generator(self, num, src, to, other):
        if num == 1:
            yield (src, to)
        else:
            yield from self.hanoi_generator(num - 1, src, other, to)
            yield (src, to)
            yield from self.hanoi_generator(num - 1, other, to, src)

    def start_demo(self):
        if self.is_running:
            return

        self.is_running = True
        self.lbl_info.config(text="正在演示...", fg="green")
        self.move_generator = self.hanoi_generator(self.num_disks, "A", "B", "C")
        self.process_next_move()

    def process_next_move(self):
        if not self.is_running:
            return

        try:
            src_name, to_name = next(self.move_generator)
            self.animate_move(src_name, to_name)
            delay = self.speed_scale.get()
            self.master.after(delay, self.process_next_move)

        except StopIteration:
            self.is_running = False
            self.lbl_info.config(text="演示完成！", fg="blue")

    def animate_move(self, src_name, to_name):
        src_idx = self.peg_map[src_name]
        to_idx = self.peg_map[to_name]

        if not self.disks[src_idx]:
            return  # 安全检查

        # 逻辑移动：从源柱子顶部拿走
        disk_data = self.disks[src_idx].pop()
        # 放到目标柱子顶部
        self.disks[to_idx].append(disk_data)

        # 视觉移动
        rect_id = disk_data["id"]
        width = disk_data["width"]

        # 计算新位置：目标柱子上现有的数量
        count_on_target = len(self.disks[to_idx])

        new_x_center = self.peg_xs[to_idx]
        # 注意：这里也是从底部向上堆叠
        # 第1个盘子(count=1) -> i=0 -> y_bottom - 0*h
        # 第2个盘子(count=2) -> i=1 -> y_bottom - 1*h
        new_y_bottom = self.peg_y_bottom - (count_on_target - 1) * self.disk_height

        self.canvas.coords(rect_id, new_x_center - width / 2, new_y_bottom - self.disk_height, new_x_center + width / 2, new_y_bottom)
        self.canvas.update()
        print(f"move disk from {src_name} to {to_name}")


if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiGUI(root)
    root.mainloop()
