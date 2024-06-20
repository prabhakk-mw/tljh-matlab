"""
Simplest plugin that exercises all the hooks defined in tljh/hooks.py.
"""

import subprocess
import os
from tljh.hooks import hookimpl


@hookimpl
def tljh_extra_user_pip_packages():
    return ["jupyter-matlab-proxy"]


@hookimpl
def tljh_extra_apt_packages():
    extra_apt_packages = [
        "wget",
        "unzip",
        "ca-certificates",
        "xvfb",
        "git",
    ]

    script = os.path.join(os.path.dirname(__file__), "bash_scripts/get-matlab-deps.sh")
    result = subprocess.call(
        [
            "bash",
            script,
        ],
        env={
            "MATLAB_RELEASE": "R2024a",
            "OS": "ubuntu22.04",
        },
    )

    if result == 0:
        # no error, read file
        with open("base-dependencies.txt") as f:
            matlab_deps = f.read().splitlines()
        print(f"extra libs: ${matlab_deps}")

        return extra_apt_packages + matlab_deps
    else:
        # In case the script above fails, return a list for R2024a
        return [
            "wget",
            "unzip",
            "ca-certificates",
            "xvfb",
            "git",
            "ca-certificates",
            "libasound2",
            "libc6",
            "libcairo-gobject2",
            "libcairo2",
            "libcap2",
            "libcups2",
            "libdrm2",
            "libfontconfig1",
            "libgbm1",
            "libgdk-pixbuf-2.0-0",
            "libgl1",
            "libglib2.0-0",
            "libgstreamer-plugins-base1.0-0",
            "libgstreamer1.0-0",
            "libgtk-3-0",
            "libice6",
            "libltdl7",
            "libnspr4",
            "libnss3",
            "libpam0g",
            "libpango-1.0-0",
            "libpangocairo-1.0-0",
            "libpangoft2-1.0-0",
            "libsndfile1",
            "libudev1",
            "libuuid1",
            "libwayland-client0",
            "libxcomposite1",
            "libxcursor1",
            "libxdamage1",
            "libxfixes3",
            "libxft2",
            "libxinerama1",
            "libxrandr2",
            "libxt6",
            "libxtst6",
            "libxxf86vm1",
            "locales",
            "locales-all",
            "make",
            "net-tools",
            "procps",
            "sudo",
            "unzip",
            "zlib1g",
        ]


@hookimpl
def tljh_post_install():
    # Installs MATLAB
    script = os.path.join(os.path.dirname(__file__), "bash_scripts/install-matlab.sh")
    subprocess.call(
        [
            "bash",
            script,
        ],
        env={
            "MATLAB_RELEASE": "R2024a",
            "MATLAB_PRODUCT_LIST": "MATLAB Symbolic_Math_Toolbox",
        },
    )


# @hookimpl
# def tljh_custom_jupyterhub_config(c):
#     # c.Test.jupyterhub_config_set_by_matlab_plugin = True
#     # c.JupyterHub.services.cull.every = 60
#     # c.JupyterHub.services.cull.timeout = 180
#     # # Dont set a max age, and dont cull users (these are default anyways)
#     # c.JupyterHub.services.cull.max_age = 0
#     # c.JupyterHub.services.cull.users = False
#     # c.JupyterHub.services.cull.users = False


# @hookimpl
# def tljh_config_post_install(config):
#     config["Test"] = {"tljh_config_set_by_matlab_plugin": True}


# @hookimpl
# def tljh_new_user_create(username):
#     with open("test_new_user_create", "w") as f:
#         f.write("file_written_by_simplest_plugin")
#         f.write(username)
