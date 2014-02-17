#!/usr/bin/env python

from collections import defaultdict
from conda.resolve import Package
from sat_test_data import (base_clauses1, all_solutions_clauses1, base_clauses2,
    all_solutions_clauses2, base_clauses_to_packages1,
    base_clauses_to_packages2, all_solutions_clauses_to_packages1,
    all_solutions_clauses_to_packages2, base_packages_to_clauses1,
    base_packages_to_clauses2, all_solutions_packages_to_clauses1,
    all_solutions_packages_to_clauses2, index)

def min_expr(c2p, p2c):
    packages_by_name = defaultdict(list)
    for p in p2c:
        name = p.rsplit('-', 2)[0]
        P = Package(p, index[p])
        print(P.norm_version)
        packages_by_name[name].append(P)

    for name in packages_by_name:
        # XXX: This works with np and py by sorting the build string
        packages_by_name[name].sort()

    return packages_by_name

if __name__ == '__main__':
    import to_dimacs
    to_dimacs.write_cnf(base_clauses1, 'base_clauses1.cnf')
    to_dimacs.write_cnf(all_solutions_clauses1, 'all_solutions_clauses1.cnf')
    to_dimacs.write_opb(base_clauses1, 'base_clauses1.opb')
    to_dimacs.write_opb(all_solutions_clauses1, 'all_solutions_clauses1.opb')

    to_dimacs.write_cnf(base_clauses2, 'base_clauses2.cnf')
    to_dimacs.write_cnf(all_solutions_clauses2, 'all_solutions_clauses2.cnf')
    to_dimacs.write_opb(base_clauses2, 'base_clauses2.opb')
    to_dimacs.write_opb(all_solutions_clauses2, 'all_solutions_clauses2.opb')

    import pprint
    pprint.pprint(min_expr(base_clauses_to_packages1, base_packages_to_clauses1))
