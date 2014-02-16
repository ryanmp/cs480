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

default: stutest.out

compiler: $(OBJS)
	$(CCC) $(CCFLAGS) -o compiler $(OBJS)

clean:
	rm -f *.out
	ls

# stutest.out: compiler
stutest.out:
	python compiler.py -p stutest1.in > stutest1.out
	cat stutest1.out
	python compiler.py -p stutest2.in > stutest2.out
	cat stutest2.out
	python compiler.py -p stutest3.in > stutest3.out
	cat stutest3.out

	
test:
	python test_driver.py > test_driver.out

proftest.out: compiler
	cat proftest.in
	compiler proftest.in > proftest.out
	cat proftest.out
