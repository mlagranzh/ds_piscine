# /bin/sh
# date_for_slice=2022-04-01
# head -n 1 "../ex02/hh_sorted.csv" > "$date_for_slice".csv
# cat "../ex02/hh_sorted.csv" | grep "$date_for_slice" >> "$date_for_slice"


awk -F '\",\"|T' 'NR==1 {a=$0; next} {b=$2".csv"} !($2 in c) {c[$2]; print a > b} {print >> b}' "../ex03/hh_positions.csv"
