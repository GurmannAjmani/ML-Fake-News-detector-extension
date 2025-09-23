import pkg_resources

# List of libraries you want to check
libraries = [
    "fastapi",
    "uvicorn",
    "scikit-learn",
    "joblib",
    "pandas",
    "numpy",
    "nltk",
    "tensorflow"
]

# Get installed versions
installed_versions = {}
for lib in libraries:
    try:
        version = pkg_resources.get_distribution(lib).version
        installed_versions[lib] = version
    except pkg_resources.DistributionNotFound:
        installed_versions[lib] = "Not installed"

# Write to requirements.txt
with open("requirements.txt", "w") as f:
    for lib, version in installed_versions.items():
        if version != "Not installed":
            f.write(f"{lib}=={version}\n")
        else:
            print(f"{lib} is not installed, skipping...")

print("requirements.txt updated with installed library versions:")
for lib, version in installed_versions.items():
    print(f"{lib}: {version}")
