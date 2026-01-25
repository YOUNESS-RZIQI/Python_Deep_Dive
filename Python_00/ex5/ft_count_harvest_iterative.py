# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: yrziqi <yrziqi@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/27 08:27:01 by yrziqi            #+#    #+#             #
#    Updated: 2025/12/27 08:27:02 by yrziqi           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_count_harvest_iterative() -> None:
    until = int(input("Days until harvest: "))
    for i in range(1, until + 1):
        print(f"Day {i}")
    print("Harvest time!")
