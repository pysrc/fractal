import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import sys


def main():
    root = tk.Tk()
    root.title("取色器")

    # 加载图片
    try:
        img = Image.open("reds.jpg")
        img = img.resize((500, 500))
        photo = ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"无法加载图片: {e}")
        print("请确保reds.jpg文件存在，或安装Pillow库: pip install Pillow")
        root.destroy()
        return

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo)

    res = []

    def on_left_click(event):
        # 左键取色
        y = event.y
        pixels = img.load()
        for i in range(500):
            try:
                r, g, b = pixels[i, y][:3]
                if (r, g, b) != (0, 0, 0):
                    res.append([r, g, b])
                else:
                    print("end")
                    break
            except:
                break

    def on_right_click(event):
        # 右键保存
        with open("res.txt", "a") as f:
            f.write(str(res) + "\n")
        res.clear()
        print("颜色已保存到res.txt")

    canvas.bind("<Button-1>", on_left_click)
    canvas.bind("<Button-3>", on_right_click)

    root.mainloop()


if __name__ == "__main__":
    main()