from setuptools import setup, find_packages

setup(
    name='django-schedule',
    version='0.1.0',
    description='This is a simple yet powerful event scheduling application.',
    author='Tony Hauber',
    author_email='thauber@gmail.com',
    url='http://django-schedule.googlecode.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
