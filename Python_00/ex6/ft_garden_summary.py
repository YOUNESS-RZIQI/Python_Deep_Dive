# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_summary.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: yrziqi <yrziqi@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/27 10:49:38 by yrziqi            #+#    #+#             #
#    Updated: 2025/12/27 10:49:39 by yrziqi           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_garden_summary() -> None:
    garden_name = input("Enter garden name: ")
    plants_number = input("Enter number of plants: ")
    print("Garden: " + garden_name)
    print("Plants: " + plants_number)
    print("Status: Growing well!")
