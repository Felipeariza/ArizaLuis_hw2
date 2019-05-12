Resultados_hw2.pdf: Resultados_hw2.tex Edificio.cpp Plots_hw2.py w0.dat w1.dat w2.dat w3.dat w4.dat w.dat
	python Plots_hw2.py
	pdflatex Resultados_hw2.tex
	make clean

%.dat : a.out
	./a.out 

a.out: Edificio.cpp
	g++ Edificio.cpp

clean:
	rm -rf a.out *.dat *~ *.out *.aux *.log 
	
cleanplots:
	rm *.png

