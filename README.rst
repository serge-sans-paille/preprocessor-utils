A collection of utilities to work with C and C++ preprocessor
=============================================================

``count-preprocessed-lines`` counts the number of preprocessed lines involved in a
project build, based on the content of a `Compilation Database <https://clang.llvm.org/docs/JSONCompilationDatabase.html>`_.

``preprocessed-lines-history`` counts the number of preprocessed lines involved
in a project build based on git (for VCS) and cmake (for build configuration).

``pp_histogram`` displays an histogram of the number of lines included perf
included file.

``iwyu-diff`` runs `include-what-you-use <https://include-what-you-use.org/>`_
on two different commits based on the content of a `Compilation Database
<https://clang.llvm.org/docs/JSONCompilationDatabase.html>`_. It the prints a
formatted diff of the result, allowing to track include regression.
