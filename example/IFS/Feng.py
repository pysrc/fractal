from fractal import IFS

code = [
    [0.14, 0.01, 0, 0.51, -0.08, -1.31, 0.1],
    [0.43, 0.52, -0.45, 0.50, 1.49, -0.75, 0.35],
    [0.45, -0.49, 0.47, 0.47, -1.62, -0.74, 0.35],
    [0.49, 0, 0, 0.51, 0.02, 1.62, 0.2]
]

ifs = IFS([500, 500])
ifs.setCoordinate()
ifs.setPx(50, 250, 250)
ifs.setIfsCode(code)
ifs.doIFS(200000)
ifs.wait()
