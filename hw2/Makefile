#--------------------------------------------
# INSTRUCTION
# Quoted strings are to be filled in by student
#
CCC = 
CCFLAGS = 
OBJS = 
SOURCE = 
RUNFLAGS = 

$(OBJS): $(SOURCE)
	$(CCC) $(CCFLAGS) -c $(SOURCE)

compiler: $(OBJS)
	$(CCC) $(CCFLAGS) -o compiler $(OBJS)

clean:
	rm -f *.out
	ls

# stutest.out: compiler
stutest.out:
#	cat stutest1.in
#	-compiler $(RUNFLAGS) stutest1.in > stutest1.out
	python compiler.py stutest1.in > stutest.out
	cat stutest.out
# Notice the next line. The `-' says to ignore the return code. This
# is a way to have multiple tests of errors that cause non-zero return
# codes.
#	cat stutest2.in
#	-compiler stutest2.in > stutest2.out
#	cat stutest2.out

test:
	python test_driver.py > test_driver.out

proftest.out: compiler
	cat $(PROFTEST)
	compiler $(PROFTEST) > proftest.out
	cat proftest.out
