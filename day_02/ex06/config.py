import sys
# import requests

num_of_steps = 3

if (len(sys.argv) != 2):
    exit(1)
try:
    fd_file = open(sys.argv[1])
    file_name = sys.argv[1]
except BaseException:
    # requests.post(hook, json.dumps(error))
    print("File not found")
    exit(1)

report_filename, type_of_file = 'hello', 'txt'

report = """\
We have made {count_observations} observations from tossing a coin: {count_tails} of them were tails and {count_heads} of
them were heads. The probabilities are {tails_percent:0.2f}% and {heads_percent:0.2f}%, respectively. Our
forecast is that in the next {count_next_observations} observations we will have: {count_next_tails} tail and {count_next_heads} heads."""

hook = None
success = 'The report has been successfully created'
error = "The report hasn't been created due to an error"