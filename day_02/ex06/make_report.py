from config import *
from analytics import Research
import json
import logging

def main():
    logging.basicConfig(filename='report.log', format='%(asctime)s %(message)s', level=logging.DEBUG)
    class_object = Research(sys.argv[1])
    try:
        class_object.parsing()
    except Exception:
        print("Parsing Error")
        # requests.post(hook, json.dumps(error))
        exit(1)
    output = class_object.file_reader()
    calculation_class = class_object.Calculations(output)
    count_heads, count_tails = calculation_class.counts()
    heads_percents, tails_percents = calculation_class.fractions(count_heads, count_tails)
    list_predict_random = class_object.Analytics(output).predict_random(num_of_steps)
    next_count_heads, next_count_tails = class_object.Analytics(list_predict_random).counts()
    report_output = report.format(
		count_observations=len(output),
		count_heads=count_heads,
		count_tails=count_tails,
		heads_percent=heads_percents * 100,
		tails_percent=tails_percents * 100,
		count_next_observations=num_of_steps,
		count_next_heads=next_count_heads,
		count_next_tails=next_count_tails
	)
    print(report_output)
    class_object.Analytics.save_file(report_output, report_filename, type_of_file)
    # requests.post(hook, json.dumps(success))

if __name__ == '__main__':
    main()