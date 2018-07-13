from conans import ConanFile, CMake, tools
import shutil
import os


class XtensorblasConan(ConanFile):
    name = "xtensor-blas"
    version = "master"
    license = "BSD-3"
    url = "https://github.com/darcamo/conan-xtensor-blas"
    description = "BLAS extension to xtensor "
    no_copy_source = True
    homepage = "https://github.com/QuantStack/xtensor-blas"
    generators = "cmake"
    # No settings/options are necessary, this is header only

    def requirements(self):
        self.requires("xtensor/0.16.4@darcamo/stable")
        self.requires("openblas/0.3.0@darcamo/stable")

    def source(self):
        # tools.get("https://github.com/QuantStack/xtensor-blas/archive/{0}.zip".format(self.version))
        # shutil.move("xtensor-blas-{0}".format(self.version), "sources")

        git = tools.Git(folder=".")
        git.clone("https://github.com/QuantStack/xtensor-blas.git")

        tools.replace_in_file("CMakeLists.txt", "project(xtensor-blas)",
                              """project(xtensor-blas)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()""")

    def build(self):
        cmake = CMake(self)
        os.mkdir("build")
        shutil.move("conanbuildinfo.cmake", "build/")
        cmake.configure(build_folder="build")
        cmake.build()
        cmake.install()
