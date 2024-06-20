from setuptools import setup, find_packages, find_namespace_packages

setup(
    name="tljh-matlabplugin",
    entry_points={"tljh": ["matlabplugin = tljh_matlabplugin.tljh_matlabplugin"]},
    version="0.0.1",
    # py_modules=["tljh_matlabplugin"],
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={"tljh_matlabplugin.bash_scripts": ["*.sh"]},
    include_package_data=True,
)
