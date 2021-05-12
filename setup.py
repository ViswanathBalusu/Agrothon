from setuptools import setup, find_packages
from agrothon import __VERSION__ as VER
setup(
    name='Agrothon',
    version=VER,
    packages=find_packages(),
    url='https://github.com/viswanathbalusu/agrothon',
    license='GPL3.0',
    author='viswanathbalusu',
    author_emai='ckvbalusu@gmail.com',
    include_package_data=True,
    description='A Field Monitoring Bot',
    platforms="any",
    install_requires=[
        "pyrogram==1.2.9",
        "tgcrypto==1.2.2",
        "motor==2.4.0",
        "fastapi[all]==0.64.0",
        "requests==2.25.1",
        "python-dotenv==0.17.0",
        "aiohttp==3.7.4.post0",
        "python-telegram-bot==13.5",
        "pandas==1.2.4",
        "numpy==1.19.5",
        "tensorflow==2.4.1",
        "prettytable==2.1.0",
        "opencv-python==4.5.1.48",
        "pillow==8.2.0",
        "seaborn==0.11.1",
        "Keras==2.4.3",
        "scikit-learn==0.22.2.post1",
        "telegraph==1.4.1",
        "psutil==5.8.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts":[
            "agrothon = agrothon.__main__:main",
            "agroserver = agrothon.API:Agrothon"
        ]
    }
)
