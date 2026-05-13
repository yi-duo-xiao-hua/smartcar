import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'test_carcontrol'

launch_files = glob(os.path.join('launch', '*.launch.py'))
config_files = glob(os.path.join('config', '*'))
data_files = [
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
]
if launch_files:
    data_files.append((os.path.join('share', package_name, 'launch'), launch_files))
if config_files:
    data_files.append((os.path.join('share', package_name, 'config'), config_files))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='long',
    maintainer_email='1226843690@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_carcontrol    = test_carcontrol.test_carcontrol:main',
            'test_pidcontroller     = test_carcontrol.test_car_pid:main',
            'test_resnet    =test_carcontrol.test_resnet:main',
            'test_qrcode    =test_carcontrol.test_qrcode:main',
            'test_yolo_echo   = test_carcontrol.test_yolo_echo:main',
            'test_yolo    =test_carcontrol.test_yolo:main',
            'test_llm    =test_carcontrol.test_llm:main',
            'new_carctrl    =test_carcontrol.new_pidctrl:main',
            'test_llm_local     =test_carcontrol.test_llm_local:main',
            'new_resnet     =test_carcontrol.new_resnet:main',
            'new_yolo      =test_carcontrol.new_yolo:main',
            'new_videologger    =test_carcontrol.new_videologger:main',
            'new_videologger_v2 =test_carcontrol.new_videologger_v2:main',
            'depth_image    =test_carcontrol.depth_image:main',
            'new_yolo_d     =test_carcontrol.new_yolo_d:main',
            'new_ctrlpub   =test_carcontrol.new_ctrlpub:main',
            'qrcode_wechat    =test_carcontrol.qrcode_wechat:main',
            'image_com      =test_carcontrol.image_comp:main',
            'car_keyboard   =test_carcontrol.car_keyboard:main'
        ],
    },
)
