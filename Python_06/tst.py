# ⚗️      ⚗️
#  ⚗️    ⚗️
#   ⚗️  ⚗️
#    ⚗️⚗️     ⚗️⚗️⚗️     ⚗️      ⚗️   ⚗️      ⚗️   ⚗️⚗️⚗️⚗️   ⚗️⚗️⚗️   ⚗️⚗️⚗️
#     ⚗️     ⚗️     ⚗️   ⚗️      ⚗️   ⚗️⚗️    ⚗️   ⚗️        ⚗️       ⚗️
#     ⚗️     ⚗️     ⚗️   ⚗️      ⚗️   ⚗️ ⚗️   ⚗️   ⚗️⚗️⚗️     ⚗️⚗️⚗️   ⚗️⚗️⚗️
#     ⚗️     ⚗️     ⚗️   ⚗️      ⚗️   ⚗️  ⚗️  ⚗️   ⚗️             ⚗️      ⚗️
#     ⚗️      ⚗️⚗️⚗️      ⚗️⚗️⚗️⚗️    ⚗️   ⚗️ ⚗️   ⚗️⚗️⚗️⚗️  ⚗️⚗️⚗️   ⚗️⚗️
#
#
#
# 1) check if alredy exist in modules ?
# 2) if not , check if exist in the builtin modules
# 3) load it .
# 4) excute it .
# 5) add it as loaded in the sys.madules.
def prnt():
    x = 10
    y = "hello"
    print(locals())

# The global namespace IS a dictionary:
prnt()