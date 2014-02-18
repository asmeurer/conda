#!/usr/bin/env python

import sys

from os.path import basename

from pycosat import itersolve

# From test_pycosat.py

def read_cnf(path):
    """
    read a DIMACS cnf formatted file from `path`, and return the clauses
    and number of variables
    """
    clauses = []
    for line in open(path):
        parts = line.split()
        if not parts or parts[0] == 'c':
            continue
        if parts[0] == 'p':
            assert len(parts) == 4
            assert parts[1] == 'cnf'
            n_vars, n_clauses = [int(n) for n in parts[2:4]]
            continue
        if parts[0] == '%':
            break
        assert parts[-1] == '0'
        clauses.append([int(lit) for lit in parts[:-1]])
    assert len(clauses) == n_clauses
    return clauses, n_vars

def process_cnf_file(path):
    sys.stdout.write('%30s:  ' % basename(path))
    sys.stdout.flush()

    clauses, n_vars = read_cnf(path)
    sys.stdout.write('vars: %6d   cls: %6d   ' % (n_vars, len(clauses)))
    sys.stdout.flush()
    n_sol = 0
    with open(path + '.sols', 'w') as f:
        for sol in itersolve(clauses, n_vars):
            f.write(str(sol) + '\n')
            sys.stdout.write('.')
            sys.stdout.flush()
            assert evaluate(clauses, sol)
            n_sol += 1
    sys.stdout.write("%d\n" % n_sol)
    sys.stdout.flush()
    return n_sol

def evaluate(clauses, sol):
    """
    evaluate the clauses with the solution
    """
    sol_vars = {} # variable number -> bool
    for i in sol:
        sol_vars[abs(i)] = bool(i > 0)
    return all(any(sol_vars[abs(i)] ^ bool(i < 0) for i in clause)
               for clause in clauses)

if __name__ == '__main__':
    for path in sys.argv[1:]:
        process_cnf_file(path)
