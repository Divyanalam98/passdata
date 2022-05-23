#!/bin/bash
/Users/pbchandra1/Documents/passdata/app.py && /Users/pbchandra1/Documents/passdata/ABAC.py

file_list=("/Users/pbchandra1/Documents/passdata/app.py" "Users/pbchandra1/Documents/passdata/ABAC.py")

for py_file in "${file_list[@]}"
do
    python ${py_file}
done