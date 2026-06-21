#!/bin/bash

g++20h iostream vector
g++20 -c heap.cc
g++20 -c heap-impl.cc
g++20 -c main.cc
g++20 heap.o heap-impl.o main.o -o program
rm heap.o heap-impl.o main.o
./program
