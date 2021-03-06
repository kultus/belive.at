from setuptools import setup, find_packages

setup(
    name='beliveat',
    version='0.0',
    description = 'Open source platform for citizen journalists.',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Pylons',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
    author='James Arthur',
    author_email='username: thruflo, domain: gmail.com',
    url = 'http://github.com/Actualise/belive.at',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'alembic',
        'argparse',
        'assetgen',
        'beanstalkc',
        'coverage',
        'fabric',
        'formencode', 
        'gevent',
        'gevent_socketio',
        'gunicorn',
        'mock',
        'nose',
        'psycogreen',
        'psycopg2', 
        'pyDNS', 
        'pyramid', 
        'pyramid_assetgen', 
        'pyramid_basemodel>=0.1.1', 
        'pyramid_beaker', 
        'pyramid_debugtoolbar', 
        'pyramid_simpleauth>=0.2.1', 
        'pyramid_simpleform', 
        'pyramid_socketio',
        'pyramid_twitterauth>=0.2',
        'pyramid_tm', 
        'pyramid_weblayer', 
        'python-dateutil', 
        'python-postmark', 
        'redis',
        'setuptools-git', 
        'transaction', 
        'tweepy',
        'waitress', 
        'zope.sqlalchemy',
        'SQLAlchemy',
        'Paste',
        'WebTest',
    ],
    entry_points = """\
        [setuptools.file_finders]
        ls = setuptools_git:gitlsfiles
        [paste.app_factory]
        main = beliveat:main
        [console_scripts]
        beliveat_stream_consumer = beliveat.stream:main
        beliveat_queue_processor = beliveat.queue:main
    """
)
