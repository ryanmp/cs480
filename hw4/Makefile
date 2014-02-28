#--------------------------------------------
# INSTRUCTION
# Quoted strings are to be filled in by student
#
CCC = 
CCFLAGS = 
OBJS = 
SOURCE = 
RUNFLAGS = 

TESTPATH = ./testfiles/

# Usage
# compiler [option] [files] 
#    option '-g' Display grammar only
#    option '-t' Display parse tree only
#    option '-b' Display both parse tree and grammar
# 	 option '-f' Display gforth code

USEROPTIONS = f

$(OBJS): $(SOURCE)
	$(CCC) $(CCFLAGS) -c $(SOURCE)

default: stutest.out

compiler: $(OBJS)
	$(CCC) $(CCFLAGS) -o compiler $(OBJS)

clean:
	rm -f *.out *.pyc $(TESTPATH)*.fs
	ls

stutest.out:
	python compiler.py -$(USEROPTIONS) $(TESTPATH)stutest1.in > stutest1.out
	cat stutest1.out
	@chmod 755 $(TESTPATH)stutest1.fs
	@echo ""
	@echo "gforth output:"
	cat $(TESTPATH)stutest1.fs
	@echo ""
	@echo ""
	gforth $(TESTPATH)stutest1.fs
	@echo ""
test:
	python test_driver.py > test_driver.out

proftest.out:
	cat proftest.in
	python compiler.py -$(USEROPTIONS) proftest.in > proftest.out
	cat proftest.out
