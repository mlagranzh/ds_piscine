import cProfile, pstats
import financial

import sys

def main():
    result = cProfile.run("financial.main()", sort=1, filename='profiling-tottime.txt')
    result = cProfile.run("financial.another_http_library()", sort=1, filename='profiling-http.txt')
    result = cProfile.run("financial.main()", sort=0, filename='profiling-http.txt')

    profiler = cProfile.Profile()
    profiler.enable()
    financial.main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    sys.stdout = open('pstats-cumulative.txt', 'w')
    p = pstats.Stats(profiler)
    p.print_stats(5)
 
if __name__ == '__main__':
    main()