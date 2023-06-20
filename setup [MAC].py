from setuptools import setup

APP = ['autoclicker.py']
OPTIONS = {
    'iconfile': '/assets/egg.ico',
    'plist': {
        'CFBundleName': 'eggs-autoclicker',
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
