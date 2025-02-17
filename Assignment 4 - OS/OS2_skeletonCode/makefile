JAVAC = usr/bin/javac/
.SUFFIXES :.java .class
BINDIR = OS2_skeletonCode/bin
SRCDIR = OS2_skeletonCode/src

$(BINDIR)/%.class:$(SRCDIR)/ma%.java
	$(JAVAC) -d $(BINDIR)/ -cp $(BINDIR) $<

CLASSES=\
	Barman.class\
	DrinkOrder.class\
	Patron.class\
	SchedulingSimulation.class\

CLASS_FILES=$(CLASSES:%.class=$(BINDIR)/%.class)
default:$(CLASS_FILES)

clean:
	rm -r $(BINDIR)/*.class

runFCFS:
	java -cp $(BINDIR) SchedulingSimulation 250 0

runSJF:
	java -cp $(BINDIR) SchedulingSimulation 250 1

analysis:	
	python3 pyAnalysis.py