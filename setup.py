import re
from setuptools import setup


setup(
    name='iphy',
    version='1.0',
    url='https://github.com/mihneasim/iphy',
    license='Mozilla Public License',
    author='Mihnea Simian',
    author_email='contact@mesimian.com',
    description='hip nanoblogging',
    packages=['iphy'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['Flask==0.9',
                      'Jinja2==2.6',
                      'Werkzeug==0.8.3',
                      'Flask-Script==0.5.3',
                      'Flask-WTF==0.8.3',
                      'Flask-Assets==0.8',
                      'Flask-Uploads==0.1.3',
                      'Flask-Login==0.1.3',
                      'Flask-PyMongo==0.2.1',
                      'Flask-Admin==1.0.5',
                      'webassets==0.8',
                      'pymongo==2.4.2',
                      'WTForms==1.0.3',
                      'path.py==3.0.1',
                      'jsmin==2.0.2-1',
                      'cssmin==0.1.4',
                    ],
    entry_points={'console_scripts': ['manage = iphy.manage:main']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
