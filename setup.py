from setuptools import setup, find_packages

setup(
    name="fractal",
    version="0.4.0",
    keywords=["fractal", "分形"],
    description="分形绘图库，支持Julia集、Mandelbrot集、IFS、L-System等",
    license="MIT",
    author="L.Chen",
    author_email="1570184051@qq.com",
    packages=find_packages(),
    install_requires=[
        "Pillow>=8.0.0",
        "numpy>=1.20.0",
    ],
    platforms="any",
    url="https://github.com/pysrc/fractal",
    zip_safe=False,
)