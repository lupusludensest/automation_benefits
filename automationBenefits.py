# # Automation benefits

t_m = int(input('Enter the time for build testing manual: '))  # 30
t_a = int(input('Enter the time for build testing automation: '))  # 5 five time quicker than manually
t_a_d = int(input('Enter the time for project automation development: '))  # 300
number_of_builds = int(input('Enter the builds number: '))  # 12 builds is the treshhold

def is_aut_worth(t_m, t_a, t_a_d, number_of_builds):
    tm_fr_mnl = number_of_builds * t_m
    tm_fr_autmtn = number_of_builds * t_a + t_a_d
    effect = tm_fr_autmtn - tm_fr_mnl
    if tm_fr_mnl >= tm_fr_autmtn:
        return f'Time to start automation! Effect is : "{-effect}" hours'
    else:
        print(f'Manual is still efficient')
    return f'Time for manual: "{tm_fr_mnl}" hours\nTime for automation: "{tm_fr_autmtn}" hours'

print(is_aut_worth(t_m, t_a, t_a_d, number_of_builds))


