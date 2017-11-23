from distutils.core import setup, Extension

setup(
    name='fractension',
    version='1.0',
    description='C extension for fractal module',
    ext_modules=[
        Extension(
            'fractension',
            sources=[
                'fractension.c',
            ]
        ),
    ]
)
