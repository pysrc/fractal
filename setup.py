from setuptools import setup, find_packages

# 读取README作为长描述
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except:
    long_description = "分形绘图库，支持Julia集、Mandelbrot集、IFS、L-System等"

setup(
    name="fractal",
    version="0.5.0",
    keywords=["fractal", "分形", "Julia", "Mandelbrot", "IFS", "L-System"],
    description="分形绘图库，支持Julia集、Mandelbrot集、IFS、L-System等",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Multimedia :: Graphics",
    ],
)