# /bin/sh

# cat ../ex02/hh_sorted.csv | head -n 1 > hh_positions.csv;
# cat ../ex01/hh.csv | tail -n +2 | sort -t ',' -k 2 -k 1n >> hh_positions.csv;

# cat hh_positions.csv | tail -n +2 | awk -F'[,]' '{print $3}' | grep "Junior"

# awk -F ',' '{gsub("Junior","1",$3); print}' OFS="," ../ex02/hh_sorted.csv > hh_sorted1.csv
# awk -F ',' '{gsub("Middle","2",$3); print}' OFS="," hh_sorted1.csv > hh_sorted2.csv
# awk -F ',' '{gsub("Senior","3",$3); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
# awk ' {print $1,$2,$3,$4,$3} ' hh_sorted1.csv > hh_sorted2.csv
# awk -F ',' '{gsub(/([^0-9][^0-9]*)/,"",$3); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
# awk -F ',' '{gsub("","-",$3); print}' OFS="," hh_sorted1.csv > hh_sorted2.csv
# awk -F ',' '{gsub("-1-","Junior",$3); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
# awk -F ',' '{gsub("-2-","Middle",$3); print}' OFS="," hh_sorted1.csv > hh_sorted2.csv
# awk -F ',' '{gsub("-3-","Senior",$3); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
# awk -F ',' '{gsub("1-","/Junior",$3); print}' OFS="," hh_sorted1.csv > hh_sorted2.csv
# awk -F ',' '{gsub("2-","/Middle",$3); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
# awk -F ',' '{gsub("3-","/Senior",$3); print}' OFS="," hh_sorted1.csv > hh_positions.csv
# rm hh_sorted2.csv hh_sorted1.csv


cleaner()
{
  awk -F "\"," 'BEGIN{OFS = FS}{
  if (tolower($3) ~ "junior" && tolower($3) ~ "middle" && tolower($3) ~ "senior")
    $3 = "\"Junior/Middle/Senior"
  else if (tolower($3) ~ "junior" && tolower($3) ~ "middle")
    $3 = "\"Junior/Middle"
  else if (tolower($3) ~ "junior" && tolower($3) ~ "senior")
    $3 = "\"Junior/Senior"
  else if (tolower($3) ~ "middle" && tolower($3) ~ "senior")
    $3 = "\"Middle/Senior"
  else if (tolower($3) ~ "junior")
    $3 = "\"Junior"
  else if (tolower($3) ~ "middle")
    $3 = "\"Middle"
  else if (tolower($3) ~ "senior")
    $3 = "\"Senior"
  else
    $3 = "\"-"
  print $0}'
}

# Cleaner without argument
head -n 1 "../ex02/hh_sorted.csv" > hh_positions.csv
cat "../ex02/hh_sorted.csv" | while read -r; do cleaner >> hh_positions.csv; done

