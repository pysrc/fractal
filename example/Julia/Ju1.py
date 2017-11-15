from fractal import Julia
ju = Julia([500, 500])  # 设置画布尺寸
ju.setC(-0.835 - 0.232j)  # Julia复常数项
ju.doJulia(400)  # 最大迭代400次
# ju.save("ju1.jpg") # 保存图片
ju.wait()
