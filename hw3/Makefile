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
	python compiler.py -p stutest4.in > stutest4.out
	cat stutest4.out
	python compiler.py -p stutest5.in > stutest5.out
	cat stutest5.out
	python compiler.py -p stutest6.in > stutest6.out
	cat stutest6.out
	python compiler.py -p stutest7.in > stutest7.out
	cat stutest7.out
	python compiler.py -p stutest8.in > stutest8.out
	cat stutest8.out
	python compiler.py -p stutest9.in > stutest9.out
	cat stutest9.out
	python compiler.py -p stutest10.in > stutest10.out
	cat stutest10.out
	python compiler.py -p stutest11.in > stutest11.out
	cat stutest11.out
	python compiler.py -p stutest12.in > stutest12.out
	cat stutest12.out
	
test:
	python test_driver.py > test_driver.out

proftest.out: compiler
	cat proftest.in
	compiler proftest.in > proftest.out
	cat proftest.out
