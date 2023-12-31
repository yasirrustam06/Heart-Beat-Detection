from setuptools import setup

setup(name='yarppg',
      version='0.1',
      description='Remote Photoplethysmography in Python',
      url='https://github.com/SamProell/yarppg',
      author='SamProell',
      license='MIT',
      packages=['yarppg'],
      install_requires=["mediapipe",
                        "numpy",
                        "opencv_python",
                        "pandas",
                        "PyQt5",
                        "pyqtgraph",
                        "scipy",
                        ],
      entry_points={"console_scripts": ["run-yarppg=yarppg.main:main"]},
      zip_safe=False,
      )
