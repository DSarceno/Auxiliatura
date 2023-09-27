# mar 26 sep 2023 21:14:40 CST 
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
set output "pruebafit1.pdf"
set grid
set title "Fit Movimiento de Proyectiles"
set ytics nomirror
set y2tics
set xlabel "Tiempo"
set ylabel "x"
set y2label "y"
set key right bottom box



f1(x) = a*x # movimiento rectilineo uniforme
f2(x) = b + c*x + d*x**2 # caida libre

fit f1(x) "data1.dat" u 1:2 via a
fit f2(x) "data1.dat" u 1:3 via b,c,d

plot "data1.dat" u 1:2 axis x1y1 w lp t "Mov x", f1(x) axis x1y1 w l lc "black" t "fit mov x", "data1.dat" u 1:3 axis x1y2 w lp t "Mov y", f2(x) axis x1y2 w l lc "blue" t "fit mov y"   

