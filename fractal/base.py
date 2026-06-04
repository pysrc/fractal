"""
    基类
    功能说明：
    - 保存图片：点击"保存"按钮 或 Ctrl+P
    - 放大：点击放大部分鼠标左键
    - 缩小：点击缩小部分鼠标右键
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import threading

# 尝试导入Pillow和numpy用于高性能绘图
try:
    from PIL import Image, ImageTk, ImageDraw
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


class Base(object):

    def __init__(self, size, callRun, title=""):
        """
            size: 画布尺寸
            callRun: 子类的绘画函数回调
            title: 画布标题
        """
        self._run = callRun
        self.title = title if title else "Fractal"
        self.width = size[0]
        self.height = size[1]

        # 绘图模式标记：'pixel'为像素绘图，'line'为线条绘图
        self._draw_mode = 'pixel'

        # 创建像素数组（用于存储计算结果）
        if HAS_NUMPY:
            self._pixel_array = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            self._pixel_array.fill(255)  # 白色背景
        else:
            self._pixel_array = None

        # 创建主窗口
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.resizable(False, False)

        # 创建主框架
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=5, pady=5)

        # 创建画布
        self.canvas = tk.Canvas(self.main_frame, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        # 创建按钮框架
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill=tk.X, padx=5, pady=5)

        # 保存按钮
        self.save_btn = tk.Button(self.button_frame, text="保存图片", command=self._on_save_click,
                                   width=12, height=1, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.save_btn.pack(side=tk.LEFT, padx=5)

        # 另存为按钮
        self.save_as_btn = tk.Button(self.button_frame, text="另存为...", command=self._on_save_as_click,
                                      width=12, height=1, bg="#2196F3", fg="white", font=("Arial", 10))
        self.save_as_btn.pack(side=tk.LEFT, padx=5)

        # 状态标签
        self.status_label = tk.Label(self.button_frame, text="就绪", font=("Arial", 9), fg="gray")
        self.status_label.pack(side=tk.RIGHT, padx=10)

        # 创建图像对象
        if HAS_PIL:
            self._pil_image = Image.new('RGB', (self.width, self.height), 'white')
            self._draw = ImageDraw.Draw(self._pil_image)  # PIL绘图对象
            self.image = ImageTk.PhotoImage(self._pil_image, master=self.root)
        else:
            self.image = tk.PhotoImage(width=self.width, height=self.height, master=self.root)
            self.image.put("white", to=(0, 0, self.width, self.height))

        self.canvas_img = self.canvas.create_image(0, 0, anchor="nw", image=self.image)

        self.psave = False
        self.scalaRate = 4  # 放大（缩小）倍数
        self.ctrl = False  # Ctrl键按下
        self.cnt = 1  # 连续命名时标号
        self._running = True
        self._drawing = False
        self._draw_thread = None
        self._selection_rect = None  # 选择框ID

        # 绑定事件
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self.root.bind("<Control-p>", self._on_save)
        self.root.bind("<Control-s>", self._on_save_click)
        self.canvas.bind("<Button-1>", self._on_left_click)  # 左键放大
        self.canvas.bind("<Button-3>", self._on_right_click)  # 右键缩小

    def _on_close(self):
        self._running = False
        self.root.quit()
        self.root.destroy()

    def _update_status(self, text, color="gray"):
        """更新状态标签"""
        self.status_label.config(text=text, fg=color)

    def _on_save(self, event=None):
        """快捷键保存"""
        self._on_save_click()

    def _sync_pil_image(self):
        """同步PIL图像从numpy数组"""
        if HAS_PIL and HAS_NUMPY and self._draw_mode == 'pixel':
            self._pil_image = Image.fromarray(self._pixel_array, 'RGB')
            self._draw = ImageDraw.Draw(self._pil_image)

    def _on_save_click(self):
        """点击保存按钮"""
        if self._drawing:
            messagebox.showwarning("提示", "请等待绘图完成后再保存")
            return
        # 确保PIL图像与像素数组同步（仅对像素绘图模式）
        self._sync_pil_image()
        if self.title == "":
            self.title = "fractal"
        if HAS_PIL:
            filename = self.title + str(self.cnt) + ".png"
            self._pil_image.save(filename)
            self._update_status(f"已保存: {filename}", "green")
            messagebox.showinfo("保存成功", f"图片已保存为 {filename}")
        else:
            filename = self.title + str(self.cnt) + ".ps"
            self.canvas.postscript(file=filename, colormode='color')
            self._update_status(f"已保存: {filename}", "green")
            messagebox.showinfo("保存成功", f"图片已保存为 {filename}\n(PostScript格式)")
        self.cnt += 1

    def _on_save_as_click(self):
        """另存为对话框"""
        if self._drawing:
            messagebox.showwarning("提示", "请等待绘图完成后再保存")
            return
        # 确保PIL图像与像素数组同步
        self._sync_pil_image()
        if HAS_PIL:
            filetypes = [
                ("PNG 图片", "*.png"),
                ("JPEG 图片", "*.jpg"),
                ("BMP 图片", "*.bmp"),
                ("所有文件", "*.*")
            ]
            filename = filedialog.asksaveasfilename(
                title="保存图片",
                initialfile=self.title + ".png",
                filetypes=filetypes,
                defaultextension=".png"
            )
            if filename:
                self._pil_image.save(filename)
                self._update_status(f"已保存: {filename}", "green")
                messagebox.showinfo("保存成功", f"图片已保存为 {filename}")
        else:
            filetypes = [("PostScript", "*.ps"), ("所有文件", "*.*")]
            filename = filedialog.asksaveasfilename(
                title="保存图片",
                initialfile=self.title + ".ps",
                filetypes=filetypes,
                defaultextension=".ps"
            )
            if filename:
                self.canvas.postscript(file=filename, colormode='color')
                self._update_status(f"已保存: {filename}", "green")
                messagebox.showinfo("保存成功", f"图片已保存为 {filename}")

    def _on_left_click(self, event):
        """左键点击放大"""
        if self._drawing or not hasattr(self, "scala"):
            return
        i, j = event.x, event.y
        w = self.width // (2 * self.scalaRate)
        h = self.height // (2 * self.scalaRate)
        # 绘制选择框并保存ID
        self._selection_rect = self.canvas.create_rectangle(i - w, j - h, i + w, j + h, outline="black", width=1)
        self.root.update()
        # 清空像素数组重新绘制
        self._clear_pixels()
        self.scala(i, j, self.scalaRate)
        self._start_draw()

    def _on_right_click(self, event):
        """右键点击缩小"""
        if self._drawing or not hasattr(self, "scala"):
            return
        i, j = event.x, event.y
        # 清空像素数组重新绘制
        self._clear_pixels()
        self.scala(i, j, 1 / self.scalaRate)
        self._start_draw()

    def _clear_pixels(self):
        """清空像素数据"""
        if HAS_NUMPY:
            self._pixel_array.fill(255)
        if HAS_PIL:
            self._pil_image = Image.new('RGB', (self.width, self.height), 'white')
            self._draw = ImageDraw.Draw(self._pil_image)

    def _start_draw(self):
        """开始绘图线程"""
        self._drawing = True
        self._update_status("绘图中...", "orange")
        self._draw_thread = threading.Thread(target=self._run_and_update, daemon=True)
        self._draw_thread.start()

    def _run_and_update(self):
        """绘图并在完成后更新显示"""
        try:
            self._run()
            # 绘图完成后立即同步PIL图像（在线程中执行）
            if HAS_PIL and HAS_NUMPY and self._draw_mode == 'pixel':
                self._pil_image = Image.fromarray(self._pixel_array, 'RGB')
                self._draw = ImageDraw.Draw(self._pil_image)
        except Exception as e:
            print(f"绘图错误: {e}")
        finally:
            self._drawing = False
            # 在主线程中更新显示
            self.root.after(0, self._finish_draw)

    def _finish_draw(self):
        """绘图完成后的处理"""
        # 删除选择框
        if self._selection_rect is not None:
            self.canvas.delete(self._selection_rect)
            self._selection_rect = None
        self._update_display()
        self._update_status("绘图完成", "green")

    def _update_display(self):
        """更新显示（在主线程中调用）"""
        if HAS_PIL and HAS_NUMPY and self._draw_mode == 'pixel':
            # 从numpy数组创建PIL图像
            self._pil_image = Image.fromarray(self._pixel_array, 'RGB')
            self._draw = ImageDraw.Draw(self._pil_image)
        if HAS_PIL:
            self.image = ImageTk.PhotoImage(self._pil_image, master=self.root)
            self.canvas.itemconfig(self.canvas_img, image=self.image)

    def save(self, title):
        """保存图片"""
        if HAS_PIL:
            self._pil_image.save(title)
        else:
            self.canvas.postscript(file=title, colormode='color')

    def set_pixel(self, x, y, color):
        """设置单个像素"""
        if isinstance(color, (list, tuple)):
            r, g, b = int(color[0]), int(color[1]), int(color[2])
        else:
            r, g, b = 0, 0, 0

        x, y = int(x), int(y)
        if 0 <= x < self.width and 0 <= y < self.height:
            if HAS_NUMPY:
                self._pixel_array[y, x] = [r, g, b]
            elif HAS_PIL:
                self._pil_image.putpixel((x, y), (r, g, b))
            else:
                color_str = "#{:02x}{:02x}{:02x}".format(r, g, b)
                self.image.put(color_str, (x, y))

    def set_pixel_fast(self, x, y, r, g, b):
        """快速设置单个像素"""
        x, y = int(x), int(y)
        if 0 <= x < self.width and 0 <= y < self.height:
            if HAS_NUMPY:
                self._pixel_array[y, x] = [r, g, b]
            elif HAS_PIL:
                self._pil_image.putpixel((x, y), (r, g, b))
            else:
                color_str = "#{:02x}{:02x}{:02x}".format(r, g, b)
                self.image.put(color_str, (x, y))

    def set_pixels(self, pixels):
        """批量设置像素"""
        for (x, y), color in pixels.items():
            self.set_pixel(x, y, color)

    def draw_line(self, start, end, color, width=1):
        """
        绘制线条
        同时在Canvas和PIL图像上绘制，确保保存时图像正确
        """
        self._draw_mode = 'line'  # 标记为线条绘图模式

        # 在Canvas上绘制
        if isinstance(color, (list, tuple)):
            r, g, b = int(color[0]), int(color[1]), int(color[2])
            canvas_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        else:
            canvas_color = color
            r, g, b = 0, 0, 0

        self.canvas.create_line(start[0], start[1], end[0], end[1], fill=canvas_color, width=width)

        # 在PIL图像上绘制（用于保存）
        if HAS_PIL:
            self._draw.line([start[0], start[1], end[0], end[1]], fill=(r, g, b), width=width)

    def draw_rect(self, x, y, w, h, color, outline_only=True):
        """绘制矩形"""
        if isinstance(color, (list, tuple)):
            r, g, b = color
            color = "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
        if outline_only:
            self.canvas.create_rectangle(x, y, x + w, y + h, outline=color, width=1)
        else:
            self.canvas.create_rectangle(x, y, x + w, y + h, fill=color, outline=color)

    def fill(self, color):
        """填充背景色"""
        if isinstance(color, (list, tuple)):
            r, g, b = int(color[0]), int(color[1]), int(color[2])
        else:
            r, g, b = 255, 255, 255

        if HAS_NUMPY:
            self._pixel_array[:, :] = [r, g, b]
        if HAS_PIL:
            self._pil_image = Image.new('RGB', (self.width, self.height), (r, g, b))
            self._draw = ImageDraw.Draw(self._pil_image)

    def wait(self):
        """等待用户关闭"""
        self._start_draw()
        self.root.mainloop()