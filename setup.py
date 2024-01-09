"""A document with package specifications"""


from setuptools import setup

setup(
    name="authors_clasiffier",
    version="0.1",
    description="A Python package for classify words into authors",
    url="https://github.com/DianaVG3110/authors_classiffier",
    author="Diana Vera, Ana Olmedo, Luis Ríos, Iván García",
    author_email="ve333269@uaeh.edu.mx, \
      ol333736@uaeh.edu.mx, ri353856@uaeh.edu.mx, ga419623@uaeh.edu.mx",
    license="MIT",
    packages=["authors_clasiffier"],
    include_package_data = True,
    package_data = {
         '' : ['*.txt']
    },
    zip_safe=False,
)
