from setuptools import setup, find_packages

setup(
    name="fractal",
    version="0.0.3",
    keywords=["fractal", "分形"],
    description="对分形比较感兴趣，看pypi上没有相关库，自己撸着玩",
    license="MIT",
    author="陈粮",
    author_email="1570184051@qq.com",
    packages=find_packages(),
    install_requires=["pygame>=1.9.3"],
    platforms="any",
    url = "https://github.com/ChenL1994/fractal",
    zip_safe=False
)
