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
TESTPATHFILES = ./testfiles/*
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
	rm -f *.out *.pyc $(TESTPATH)*.fs *.fs
	ls

stutest.out:
	python compiler.py -$(USEROPTIONS) $(TESTPATHFILES) > stutest.out
	@echo "=========== Results =============="
	cat stutest.out
ifeq ($(USEROPTIONS),f)
	@chmod 755 stutest.out
	@echo "========== gForth Results ========"
	gforth stutest.out
	@echo ""
endif
	
test:
	python test_driver.py > test_driver.out

proftest.out:
	cat proftest.in
	python compiler.py -$(USEROPTIONS) proftest.in > proftest.out
	@echo "=========== Results =============="
	cat proftest.out
ifeq ($(USEROPTIONS),f)
	@chmod 755 proftest.out
	@echo "========== gForth Results ========"
	gforth proftest.out
	@echo ""
endif

