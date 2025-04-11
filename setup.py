from setuptools import setup

package_name = 'my_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name + '_py'],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your@email.com',
    description='My wheeled robot package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ultrasonic_relay = my_bot_py.ultrasonic_relay:main',
        ],
    },
)
