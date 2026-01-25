# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: yrziqi <yrziqi@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/27 08:27:07 by yrziqi            #+#    #+#             #
#    Updated: 2025/12/27 08:27:08 by yrziqi           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

Days_until_harvest = 0
current_day = 1


def ft_count_harvest_recursive() -> None:
    global Days_until_harvest, current_day

    if current_day == 1:
        Days_until_harvest = int(input("Days until harvest: "))

    if current_day <= Days_until_harvest:
        print("Day", current_day)
        current_day += 1
        ft_count_harvest_recursive()

    elif current_day > Days_until_harvest:
        print("Harvest time!")
