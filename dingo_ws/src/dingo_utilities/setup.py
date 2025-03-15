from setuptools import find_packages, setup

package_name = 'dingo_utilities'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_dir={'':'src'},
    #py_modules=[
    #    'scripts.Keyboard'
    #],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='seek',
    maintainer_email='see-k@gmx.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    
)
