# 6125
This project implements Strassen algorithm (http://en.wikipedia.org/wiki/Strassen_algorithm) for fast (O(n^2.81)) matrix multiplication in a cache efficient way and compare it to naive matrix multiplication. We may also do Coppersmith-Winograd, which has a running time of O(n^2.38) but with a large constant that cannot be balanced with a matrix size that can be handled by a computer.
