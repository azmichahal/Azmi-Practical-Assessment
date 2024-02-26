# Azmi-Practical-Assessment
CSCK541 January 2024 B Practical Assessment: Programming

A repo with a recursive Floyd-Warshall implementation in the recursive_floyd_final.py file.
To run the tests, access the recursive_test_final.py file

# Notes
In the recursive_floyd_final.py file, we use a graph of 5 nodes to represent our input. 
Users will be able to input any graph, but ensure the input graph parameters and number of nodes (N) are changed respectively.

For the tests, the **unittest** module is used to assert certain matrices.
The tests will help you identify if the matrices are matching the expected value, however you will need to change the expected output matrix in the recursive_test_final.

There will be two input graphs in the test file: <br>

1. **input_graph** : Represents the correct input <br>
2. **error_input_graph** : Some indices are changed to provide a false input matrix <br>

Both are used to assert the final result.
