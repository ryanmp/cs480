#--------------------------------------------
# INSTRUCTION
# Quoted strings are to be filled in by student
#
CCC = 
CCFLAGS = 
OBJS = 
SOURCE = 
RUNFLAGS = 

PASSTESTPATH = ./testfiles/pass_test/
FAILTESTPATH = ./testfiles/fail_test/

# Usage
# compiler [option] [files] 
#    option '-g' Display grammar only
#    option '-t' Display parse tree only
#    option '-b' Display both parse tree and grammar

USEROPTIONS = t

$(OBJS): $(SOURCE)
	$(CCC) $(CCFLAGS) -c $(SOURCE)

default: stutest.out

compiler: $(OBJS)
	$(CCC) $(CCFLAGS) -o compiler $(OBJS)

clean:
	rm -f *.out *.pyc
	ls

# stutest.out: compiler
stutest.out:
# pass test
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest1.in > pass_stutest1.out
	cat pass_stutest1.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest2.in > pass_stutest2.out
	cat pass_stutest2.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest3.in > pass_stutest3.out
	cat pass_stutest3.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest4.in > pass_stutest4.out
	cat pass_stutest4.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest5.in > pass_stutest5.out
	cat pass_stutest5.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest6.in > pass_stutest6.out
	cat pass_stutest6.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest7.in > pass_stutest7.out
	cat pass_stutest7.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest8.in > pass_stutest8.out
	cat pass_stutest8.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest9.in > pass_stutest9.out
	cat pass_stutest9.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest10.in > pass_stutest10.out
	cat pass_stutest10.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest11.in > pass_stutest11.out
	cat pass_stutest11.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest12.in > pass_stutest12.out
	cat pass_stutest12.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest13.in > pass_stutest13.out
	cat pass_stutest13.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest14.in > pass_stutest14.out
	cat pass_stutest14.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest15.in > pass_stutest15.out
	cat pass_stutest15.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest16.in > pass_stutest16.out
	cat pass_stutest16.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest17.in > pass_stutest17.out
	cat pass_stutest17.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest18.in > pass_stutest18.out
	cat pass_stutest18.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest19.in > pass_stutest19.out
	cat pass_stutest19.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest20.in > pass_stutest20.out
	cat pass_stutest20.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest21.in > pass_stutest21.out
	cat pass_stutest21.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest22.in > pass_stutest22.out
	cat pass_stutest22.out
	python compiler.py -$(USEROPTIONS) $(PASSTESTPATH)stutest23.in > pass_stutest23.out
	cat pass_stutest23.out
	
#fail test
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest1.in > fail_stutest1.out
	cat fail_stutest1.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest2.in > fail_stutest2.out
	cat fail_stutest2.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest3.in > fail_stutest3.out
	cat fail_stutest3.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest4.in > fail_stutest4.out
	cat fail_stutest4.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest5.in > fail_stutest5.out
	cat fail_stutest5.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest6.in > fail_stutest6.out
	cat fail_stutest6.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest7.in > fail_stutest7.out
	cat fail_stutest7.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest8.in > fail_stutest8.out
	cat fail_stutest8.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest9.in > fail_stutest9.out
	cat fail_stutest9.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest10.in > fail_stutest10.out
	cat fail_stutest10.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest11.in > fail_stutest11.out
	cat fail_stutest11.out
	python compiler.py -$(USEROPTIONS) $(FAILTESTPATH)stutest12.in > fail_stutest12.out
	cat fail_stutest12.out

	
test:
	python test_driver.py > test_driver.out

proftest.out:
	cat proftest.in
	python compiler.py -$(USEROPTIONS) proftest.in > proftest.out
	cat proftest.out
