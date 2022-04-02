# /bin/sh
cat ../ex01/hh.csv | head -n 1 > hh_sorted.csv;
cat ../ex01/hh.csv | tail -n +2 | sort -t ',' -k 2 -k 1n >> hh_sorted.csv;