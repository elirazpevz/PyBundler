import subprocess

import requests
from packaging.version import parse
from inputs import get_option
from settings import Settings

DOWNLOAD_DIR = './wheels'


def get_all_versions(package_name: str, pyvers: list[str], platforms: list[str]):
    url = f"https://pypi.org/pypi/{package_name}/json"
    res = requests.get(url)
    if res.status_code != 200:
        raise ValueError(f"Package {package_name} not found.")
    data = res.json()['releases']

    versions = []
    for ver in data:
        for file in data[ver]:
            is_wheel = file['filename'].endswith('.whl')

            is_required_python_version = file['python_version'] in pyvers

            platform = next((sub for sub in platforms if sub in file['filename']), None)
            is_required_platform = any(sub in file['filename'] for sub in platforms)

            if is_wheel and is_required_python_version and is_required_platform:
                versions.insert(0,
                                {"version": ver, "filename": file['filename'], 'python_version': file['python_version'],
                                 'platform': platform})

    return versions


def download_files(package, version, filename, python_version, platform):
    cmd = [
        "pip", "download",
        f"{package}=={version}",
        "--only-binary=:all:",
        "--dest", f"{DOWNLOAD_DIR}",
        "--platform", platform,
        "--python-version", python_version[2:]
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Failed to download {package}=={version}")
        print("Error:", result.stderr.strip())
    else:
        print(f"Downloaded {package}=={version} on platform {platform}, python version {python_version}")


def download_package(settings: Settings):
    package = input("Please provide the package name: ")

    pyvers = settings.get_python_versions()
    platforms = settings.get_platforms()

    versions = (get_all_versions(package, pyvers, platforms))
    version_set = sorted(list(set(v['version'] for v in versions)), key=parse, reverse=True)

    version_platforms = []
    for version in version_set:
        supported_platforms = [f"{detail['platform']}-{detail['python_version']}" for detail in versions if
                               detail['version'] == version]
        version_platforms.append(f"{version}: {supported_platforms}")

    selected_version_names = get_option(version_platforms)
    cleaned_selected_versions_name = [option.split(':')[0] for option in selected_version_names]
    selected_versions = [ver for ver in versions if ver['version'] in cleaned_selected_versions_name]

    for version in selected_versions:
        download_files(package, **version)
