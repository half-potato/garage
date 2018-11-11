import setuptools

setuptools.setup(name='garage',
    version='0.0.1',
    # install_requires=['gym', 'mujoco-py']  # And any other dependencies foo needs
    author="RL Workgroup",
    description="A framework for reproducible reinforcement learning research",
    url="https://github.com/rlworkgroup/garage",
    # packages=setuptools.find_packages(),
    packages = [package for package in setuptools.find_packages() if package.startswith('garage')],
    # include_package_data=True,
    package_data={'garage': [
        'vendor/mujoco_models/*.xml',
        'vendor/mujoco_models/ant.xml',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    zip_safe=False,
)
