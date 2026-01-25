# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_seed_inventory.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: yrziqi <yrziqi@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/27 10:56:42 by yrziqi            #+#    #+#             #
#    Updated: 2025/12/27 10:56:43 by yrziqi           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    wordseed_frsletuprcs = seed_type.capitalize()
    if unit == "packets":
        print(wordseed_frsletuprcs, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(wordseed_frsletuprcs, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(wordseed_frsletuprcs, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
