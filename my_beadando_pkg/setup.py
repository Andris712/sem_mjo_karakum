from setuptools import find_packages, setup

package_name = 'my_beadando_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ajr',
    maintainer_email='ajr@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
entry_points={
    'console_scripts': [
        'talker = my_beadando_pkg.publisher_node:main',
        'listener = my_beadando_pkg.subscriber_node:main',
    ],
},
)
