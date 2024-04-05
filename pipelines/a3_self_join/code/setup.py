from setuptools import setup, find_packages
setup(
    name = 'a3_self_join',
    version = '1.0',
    packages = find_packages(include = ('a3_self_join*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.8.13'],
    entry_points = {
'console_scripts' : [
'main = a3_self_join.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
