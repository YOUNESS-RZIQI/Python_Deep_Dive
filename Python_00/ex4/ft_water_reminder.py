# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_water_reminder.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: yrziqi <yrziqi@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/27 08:27:13 by yrziqi            #+#    #+#             #
#    Updated: 2025/12/27 08:27:14 by yrziqi           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_water_reminder() -> None:
    days_since_last_watering = int(input("Days since last watering: "))
    if days_since_last_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
