import os
from glob import glob
from setuptools import find_packages , setup

package_name = 'dingo_peripheral_interfacing'

setup(
    name=package_name,
    version='0.0.0',

 #   packages=find_packages(exclude=['test']),
    packages=[package_name],
    package_dir={'':'src'},
#    py_modules=[
#        'scripts.battery_voltage_checking','scripts.dingo_lcd_interfacing',
#        'scripts.LCD_1inch47','scripts.lcdconfig'
#    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='seek',
    maintainer_email='see-k@gmx.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dingo_lcd_interfacing = dingo_peripheral_interfacing.dingo_lcd_interfacing:main'
        ],
    },
)
