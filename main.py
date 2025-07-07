from inputs import get_single_option
from package import download_package
from settings import Settings


def main():
    print("Welcome to PyBundler! \nPlease Input your preferences.")

    settings = Settings()

    settings.set_platforms()
    settings.set_python_versions()

    menu_options = ["Download Package", "Adjust Platforms", "Adjust Python Versions", "Exit"]
    while True:
        action = get_single_option(menu_options)
        match action:
            case "Download Package":
                download_package(settings)
            case "Adjust Platforms":
                settings.set_platforms()
            case "Adjust Python Versions":
                settings.set_python_versions()
            case "Exit":
                print("Thank you for using PyBundler. Goodbye!")
                break


if __name__ == '__main__':
    main()
