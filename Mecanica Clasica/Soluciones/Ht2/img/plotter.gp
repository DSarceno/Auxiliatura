# PROGRAM
# Idioma
set encoding utf8
# terminal
unset label
clear
set terminal pdf
set output "ej1-1.pdf"
set grid
set title "Graficas v-t y x-t"
set ytics nomirror # para desligar los 2 ejes y
set y2tics # 2 ejes y
set xlabel "Tiempo"
set ylabel "Posicion"
set y2label "Velocidad"
set xrange [1:100]
set yrange [-1:100]
set y2range [-1:10]
set key right top box

v(x) = 10*exp(-0.1*x)
y(x) = (10/0.1)*(1-exp(-0.1*x))

# se plotean los dos conjuntos de datos en una sola grafica, pero con ejes
# y's independientes.
plot y(x) axis x1y1 w l lc "blue" t "Posicion", v(x) axis x1y2 w l lc "red" t "Velocidad"
