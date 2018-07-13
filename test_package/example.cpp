#include <iostream>
#include <xtensor/xarray.hpp>
#include "xtensor-blas/xlinalg.hpp"


int main(int argc, char *argv[])
{
    xt::xtensor<double, 2> m = {{1.5, 0.5}, {0.7, 1.0}};
    std::cout << "Matrix m:\n" << m << std::endl;
    std::cout << "Matrix rank: " << xt::linalg::matrix_rank(m) <<"\n";

    std::cout << "Matrix inverse:\n" << xt::linalg::inv(m) << "\n";

    std::cout << "Eigen values:\n" << xt::linalg::eigvals(m) << "\n";

    xt::xarray<double> arg1 = xt::arange<double>(9);
    xt::xarray<double> arg2 = xt::arange<double>(18);
    arg1.reshape({3, 3});
    arg2.reshape({2, 3, 3});
    std::cout << xt::linalg::dot(arg1, arg2) << std::endl;

    return 0;
}
