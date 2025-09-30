from setuptools import setup, find_packages

package_name = 'my_beadando_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name,
         ['package.xml']),
        ('share/' + package_name + '/launch',
         ['launch/talker_listener.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aj',
    maintainer_email='aj@todo.todo',
    description='Kis beadandó ROS2 package.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_beadando_pkg.publisher_node:main',
            'listener = my_beadando_pkg.subscriber_node:main',
        ],
    },
)
