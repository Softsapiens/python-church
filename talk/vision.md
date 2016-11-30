
Python-Church
=============

Church Encoding
---------------
Is a means of representing data and operators in the lambda calculus. 
The Church-Turing thesis asserts that any computable operator (and its operands) can be represented under Church encoding. In the untyped lambda calculus the only primitive data type is the function.


Why/Uses
--------

This corresponds to continuation-passing style with multiple continuations, and is done for performance: 
the explicit construction and destruction of data is avoided, instead passing control directly based on the output
of the pattern-match that would be immediately done instead. This doesn't always result in improved performance, 
but when it does it can be fairly significant.
Basically, you can think of it as data vs. control. If what you're doing is essentially similar to control 
in nature — such as the success and failure branches of a parser — then the control-based representation 
might well be superior. Otherwise, stick with data.


References
----------

* https://en.wikipedia.org/wiki/Church_encoding
* http://stackoverflow.com/questions/9806729/practical-reasons-for-%D0%A1hurch-encoding

