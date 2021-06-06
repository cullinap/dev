# run practice warm exercise

def run_practice():
    times = 0
    i = 0
    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break

        i += 1 
        times += float(one_run)

    average_time = times / i 

    print(f'Average of {average_time: 2f}, over {i} runs')


run_practice()    
