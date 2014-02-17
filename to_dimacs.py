def write_cnf(clauses, path):
    n_vars = max(max(abs(lit) for lit in clause)
                 for clause in clauses)
    with open(path, 'w') as fo:
        fo.write('p cnf %d %d\n' % (n_vars, len(clauses)))
        for clause in clauses:
            for lit in clause:
                fo.write('%d ' % lit)
            fo.write('0\n')

def write_opb(clauses, path):
    # A clause like [1, -3, 5] is the same as +1 x1 +1 ~x3 +1 x5 >= 1
    n_vars = max(max(abs(lit) for lit in clause)
                 for clause in clauses)
    with open(path, 'w') as fo:
        fo.write("* #variable= %d #constraint= %d\n" % (n_vars, len(clauses)))
        fo.write("* Add min condition here, like\n")
        fo.write("* min: 1*x1 -1*x3;\n")
        for clause in clauses:
            for lit in clause:
                fo.write("+1*x%d " % lit)
            fo.write(">= 1;\n")
