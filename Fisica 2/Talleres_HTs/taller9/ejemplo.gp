# fitgnu.gp 
# Diego Sarceno (dsarceno68@gmail.com) 

# Resumen 

# Codificado del texto: UTF8 
# Compiladores probados: GNUPLOT (Ubuntu 20.04 Linux) 5.2 
# Instruciones de Ejecución: no requiere nada mas 
# gnuplot fitgnu.gp 


# PROGRAM 
# Idioma 
set encoding utf8 

# Terminal 
unset label 
clear 
set terminal pdf
set output "prueba.pdf"
set grid
set title "Proyectil"
set ytics nomirror
set y2tics
set xlabel "t"
set ylabel "x"
set y2label "y"
set key right bottom box

f1(x) = a*x # movmiento en el eje x
f2(x) = b*x + c*x**2 # caida libre

fit f1(x) "data1.dat" u 1:2 via a
fit f2(x) "data1.dat" u 1:3 via b,c

plot "data1.dat" u 1:2 axis x1y1 w lp t "Mov x", f1(x) axis x1y1 w l lc "black" t "fit x", "data1.dat" u 1:3 axis x1y2 w lp t "Mov y", f2(x) axis x1y2 w l lc "blue" t "fit y"










