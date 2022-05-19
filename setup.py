from setuptools import setup

setup(
    name="text-to-marquee",
    version="0.0.1",
    python_requires=">=3.7",
    install_requires=["pydantic", "pillow"],
    packages=["text_to_marquee"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "text-to-marquee=text_to_marquee.__main__:main"
        ]
    },
)
