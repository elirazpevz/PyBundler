from inputs import get_option


class Settings:
    _python_versions = [
        "cp39",
        "cp310",
        "cp311",
        "cp312"
    ]

    _platforms = [
        "none-any",
        "win_amd64",
        "musllinux_1_1_x86_64",
        "musllinux_1_2_x86_64",
        "manylinux_2_28_x86_64",
        "manylinux2014_x86_64"
    ]

    def __init__(self):
        self.selected_python_versions = []
        self.selected_platforms = []

    def get_platforms(self):
        return self.selected_platforms

    def set_platforms(self):
        self.selected_platforms = get_option(self._platforms)

    def get_python_versions(self):
        return self.selected_python_versions

    def set_python_versions(self):
        self.selected_python_versions = get_option(self._python_versions)