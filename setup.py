import setuptools
import stackhttp

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stackhttp",
    version=stackhttp.__version__,
    author = 'João Lucas Bernardi',
    author_email="joao_bernardi@outlook.com",
    description="Simpĺe http server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/jaobernardi/stack',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    include_package_data=True,
    python_requires=">=3.6",
)